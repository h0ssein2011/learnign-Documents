
# want to show the central limit theorem in practice here
from random import choices

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

unif_dist = np.random.uniform(0,100,1000)

means_unif_dist = []
for i in range(10,1100 ,10):
    means_unif_dist.append(np.mean(choices(unif_dist,k=i)))
# print(means_unif_dist)
fig ,axs = plt.subplots(2,1)
fig.suptitle('uniform dist vs sample mean distribution')
axs[0].hist(unif_dist)
axs[1].hist(means_unif_dist)
plt.show()


exp_dist = np.random.exponential(size= 1000)
means_exp_dist = []
for i in range(10,1100 ,10):
    means_exp_dist.append(np.mean(choices(exp_dist,k=i)))

fig ,axs = plt.subplots(2,1)
fig.suptitle('exponentional dist vs sample mean distribution')
axs[0].hist(exp_dist)
axs[1].hist(means_exp_dist)
plt.show()



pois_dist = np.random.poisson(size=1000)
means_pois_dist = []
for i in range(10,1100 ,10):
    means_pois_dist.append(np.mean(choices(pois_dist,k=i)))

fig ,axs = plt.subplots(2,1)
fig.suptitle('poisson dist vs sample mean distribution')
axs[0].hist(pois_dist)
axs[1].hist(means_pois_dist)
plt.show()