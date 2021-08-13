# %% [markdown]
# # TPS August 2021
# 
# For this iteration of TPS I wanted to focus more on validation to match LB and CV scores. In this notebook I choose to do an Optuna study for XGBoost that splits the train data 60-40. The high test split is to prevent the study from overfitting. Early iterations of this notebook scored the model through cross validation in the study. However, I've found that method to be painfully slow, and not much better compared to the KFold validation used later. I chose to use KFold instead of StratifiedKFold since I was getting instances where there was not enough classes to fit each split. 
# 
# I've you've found this notebook useful, please don't forget to upvote! 🙂

# %% [code] {"execution":{"iopub.status.busy":"2021-08-11T17:09:43.779532Z","iopub.execute_input":"2021-08-11T17:09:43.779854Z","iopub.status.idle":"2021-08-11T17:09:43.787496Z","shell.execute_reply.started":"2021-08-11T17:09:43.779828Z","shell.execute_reply":"2021-08-11T17:09:43.786438Z"}}
# Data processing
%matplotlib inline
import numpy as np
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt

# Machine Learning
import optuna
import xgboost as xgb
from optuna.samplers import TPESampler
from sklearn.preprocessing import RobustScaler, StandardScaler, MinMaxScaler
from sklearn.model_selection import train_test_split, cross_val_score, StratifiedKFold, KFold
from sklearn.metrics import mean_squared_error

# %% [code] {"execution":{"iopub.status.busy":"2021-08-11T17:09:43.789162Z","iopub.execute_input":"2021-08-11T17:09:43.789793Z","iopub.status.idle":"2021-08-11T17:09:50.239666Z","shell.execute_reply.started":"2021-08-11T17:09:43.789672Z","shell.execute_reply":"2021-08-11T17:09:50.238847Z"}}
input_dir = Path('../input/tabular-playground-series-aug-2021/')
train_df = pd.read_csv(input_dir / 'train.csv')
test_df = pd.read_csv(input_dir / 'test.csv')
sample_submission = pd.read_csv(input_dir / 'sample_submission.csv')

# %% [code] {"execution":{"iopub.status.busy":"2021-08-11T17:09:50.241319Z","iopub.execute_input":"2021-08-11T17:09:50.241651Z","iopub.status.idle":"2021-08-11T17:09:50.268792Z","shell.execute_reply.started":"2021-08-11T17:09:50.241624Z","shell.execute_reply":"2021-08-11T17:09:50.267846Z"}}
train_df.head()

# %% [code] {"execution":{"iopub.status.busy":"2021-08-11T17:09:50.270392Z","iopub.execute_input":"2021-08-11T17:09:50.270738Z","iopub.status.idle":"2021-08-11T17:09:50.298451Z","shell.execute_reply.started":"2021-08-11T17:09:50.270704Z","shell.execute_reply":"2021-08-11T17:09:50.297663Z"}}
test_df.head()

# %% [code] {"execution":{"iopub.status.busy":"2021-08-11T17:09:50.299588Z","iopub.execute_input":"2021-08-11T17:09:50.299916Z","iopub.status.idle":"2021-08-11T17:09:50.308755Z","shell.execute_reply.started":"2021-08-11T17:09:50.299881Z","shell.execute_reply":"2021-08-11T17:09:50.307679Z"}}
sample_submission.head()

# %% [code] {"execution":{"iopub.status.busy":"2021-08-11T17:09:50.310383Z","iopub.execute_input":"2021-08-11T17:09:50.310905Z","iopub.status.idle":"2021-08-11T17:09:50.452875Z","shell.execute_reply.started":"2021-08-11T17:09:50.310865Z","shell.execute_reply":"2021-08-11T17:09:50.452046Z"}}
X = train_df.drop(['id', 'loss'], axis=1).values
y = train_df['loss'].values
X_test = test_df.drop(['id'], axis=1).values

# %% [code] {"execution":{"iopub.status.busy":"2021-08-11T17:09:50.454115Z","iopub.execute_input":"2021-08-11T17:09:50.45452Z","iopub.status.idle":"2021-08-11T17:09:50.922157Z","shell.execute_reply.started":"2021-08-11T17:09:50.454479Z","shell.execute_reply":"2021-08-11T17:09:50.921323Z"}}
# I've found many using MinMaxScaling but I've personally had better results with StandardScaling
scaler = StandardScaler()
X = scaler.fit_transform(X)
X_test = scaler.transform(X_test)

# %% [code] {"execution":{"iopub.status.busy":"2021-08-11T17:09:50.924568Z","iopub.execute_input":"2021-08-11T17:09:50.924913Z","iopub.status.idle":"2021-08-11T17:09:50.930934Z","shell.execute_reply.started":"2021-08-11T17:09:50.924877Z","shell.execute_reply":"2021-08-11T17:09:50.929783Z"}}
y_min = y.min()
y_max = y.max()

# While it's probably rare that values will fall outside the y-min-max range, we should probably do it anyway.
def my_rmse(y_true, y_hat):
    y_true[y_true < y_min] = y_min
    y_true[y_true > y_max] = y_max
    
    y_true[y_hat < y_min] = y_min
    y_true[y_hat > y_max] = y_max
    
    return mean_squared_error(y_true, y_hat, squared=False)

# %% [code] {"execution":{"iopub.status.busy":"2021-08-11T17:09:50.932571Z","iopub.execute_input":"2021-08-11T17:09:50.933068Z","iopub.status.idle":"2021-08-11T17:09:50.943488Z","shell.execute_reply.started":"2021-08-11T17:09:50.933033Z","shell.execute_reply":"2021-08-11T17:09:50.942684Z"}}
def objective(trial):
    # Split the train data for each trial.
    X_train, X_valid, y_train, y_valid = train_test_split(X, y, stratify=y, test_size=0.4)

    param_grid = {
        'max_depth': trial.suggest_int('max_depth', 6, 10), # Extremely prone to overfitting!
        'n_estimators': trial.suggest_int('n_estimators', 400, 4000, 400), # Extremely prone to overfitting!
        'eta': trial.suggest_float('eta', 0.007, 0.013), # Most important parameter - the learning rate!
        'subsample': trial.suggest_discrete_uniform('subsample', 0.5, 0.9, 0.1),
        'colsample_bytree': trial.suggest_discrete_uniform('colsample_bytree', 0.5, 0.9, 0.1),
        'min_child_weight': trial.suggest_int('min_child_weight', 5, 20), # I've had trouble with LB score until tuning this.
        'reg_lambda': trial.suggest_int('reg_lambda', 1, 50), # L2 regularization
        'reg_alpha': trial.suggest_int('reg_alpha', 0, 50), # L1 regularization
    } 
    
    reg = xgb.XGBRegressor(
        # These parameters should help with trial speed.
        tree_method='gpu_hist',
        predictor='gpu_predictor',
        n_jobs=4,
        **param_grid
    )
    
    reg.fit(X_train, y_train,
            eval_set=[(X_valid, y_valid)], eval_metric='rmse',
            verbose=False)

    # Returns the best RMSE for the trial.
    # Readers may want to try returning a cross validation score here.
    return my_rmse(y_valid, reg.predict(X_valid))

# %% [code] {"execution":{"iopub.status.busy":"2021-08-11T17:09:50.946155Z","iopub.execute_input":"2021-08-11T17:09:50.946433Z","iopub.status.idle":"2021-08-11T17:20:10.959812Z","shell.execute_reply.started":"2021-08-11T17:09:50.946409Z","shell.execute_reply":"2021-08-11T17:20:10.958971Z"}}
train_time = 1 * 10 * 60 # Train for up to ten minutes.
study = optuna.create_study(direction='minimize', sampler=TPESampler(), study_name='XGBRegressor')
study.optimize(objective, timeout=train_time)

print('Number of finished trials: ', len(study.trials))
print('Best trial:')
trial = study.best_trial

print('\tValue: {}'.format(trial.value))
print('\tParams: ')
for key, value in trial.params.items():
    print('\t\t{}: {}'.format(key, value))

# %% [code] {"execution":{"iopub.status.busy":"2021-08-11T17:20:10.961109Z","iopub.execute_input":"2021-08-11T17:20:10.961463Z","iopub.status.idle":"2021-08-11T17:27:54.850155Z","shell.execute_reply.started":"2021-08-11T17:20:10.961427Z","shell.execute_reply":"2021-08-11T17:27:54.848873Z"}}
# Fetch the best trial parameters and set some settings for the KFold predictions.
xgb_params = trial.params
xgb_params['tree_method'] = 'gpu_hist'
xgb_params['predictor'] = 'gpu_predictor'
xgb_params['n_jobs'] = 4

n_splits = 10
test_preds = None
kf_rmse = []

for fold, (train_idx, valid_idx) in enumerate(KFold(n_splits=n_splits, shuffle=True).split(X, y)):
    # Fetch the train-validation indices.
    X_train, y_train = X[train_idx], y[train_idx]
    X_valid, y_valid = X[valid_idx], y[valid_idx]
    
    # Create and fit a new model using the best parameters.
    model = xgb.XGBRegressor(**xgb_params)
    model.fit(X_train, y_train,
            eval_set=[(X_valid, y_valid)],
            eval_metric='rmse', verbose=False)
    
    # Validation predictions.
    valid_pred = model.predict(X_valid)
    rmse = my_rmse(y_valid, valid_pred)
    print(f'Fold {fold+1}/{n_splits} RMSE: {rmse:.4f}')
    kf_rmse.append(rmse)
    
    # Use the model trained for 1/n_splits of the output predictions.
    if test_preds is None:
        test_preds = model.predict(X_test)
    else:
        # This is kind of naughty for numerical accuracy (may overflow on other problems) but slightly quicker.
        test_preds += model.predict(X_test)

test_preds /= n_splits
print(f'Average KFold RMSE: {np.mean(np.array(kf_rmse)):.5f}')

# %% [code] {"execution":{"iopub.status.busy":"2021-08-11T17:28:00.412451Z","iopub.execute_input":"2021-08-11T17:28:00.412767Z","iopub.status.idle":"2021-08-11T17:28:00.803793Z","shell.execute_reply.started":"2021-08-11T17:28:00.412738Z","shell.execute_reply":"2021-08-11T17:28:00.802808Z"}}
test_preds[test_preds < y_min] = y_min
test_preds[test_preds > y_max] = y_max
sample_submission['loss'] = test_preds
sample_submission.to_csv('submission.csv', index=False)
sample_submission

# %% [code]
