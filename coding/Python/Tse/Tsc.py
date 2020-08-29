import pytse_client as tse
import pandas as pd
import datetime
from persiantools.jdatetime import JalaliDate

def get_jalali_dates(x):
    return str(JalaliDate(datetime.date(x.year,x.month,x.day)))

symbols =["صبا","شگویا","شکلر","شستا","سدور","زکوثر","خگستر","حکشتی","تملت","تپمپی","تاصیکو","کفپارس","مادیرا","نطرین","ولیز","ونفت"]

df=pd.DataFrame(columns={"symbol","adjClose",'date','last_price','persian_date','prev_price'})

for sym in symbols:
    try: 
        tickers = tse.download(symbols=sym, write_to_csv=False)
        tickers = tickers[sym] # history
        tickers = tickers.reset_index() 
        tickers['date'] = pd.to_datetime(tickers['date'])
        tickers=tickers[tickers.date > '2020-04-01']
        tickers['symbol'] = sym
        tickers['persian_date']=tickers.date.map(get_jalali_dates)

        tickers['last_price']= int(tickers.loc[(tickers.date==max(tickers.date)) & (tickers.symbol==sym),"adjClose"])
        tickers = tickers.sort_values(by='date')
        tickers['prev_price'] = tickers.adjClose .shift(1) 
        tickers=tickers.loc[:,["symbol","adjClose",'date','last_price','prev_price','persian_date']]
 

        df=df.append(tickers )
        print(sym,'done')
    except :
        print(sym,'faild',EnvironmentError)


df.to_csv('symbols.csv',index=False)


print(' All done and df size is:',df.shape)

  