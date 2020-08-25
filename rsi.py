import pandas as pd
import matplotlib.pyplot as plt

def RSI(data, period = 14):
    # Get Data
    df=pd.read_csv(data, usecols=['Date','Close'])
    chg = df['Close'].diff(1)
    gain = chg.mask(chg < 0,0)
    loss = chg.mask( chg > 0,0)
    avg_gain = gain.ewm(com=period-1,min_periods=period).mean()
    avg_loss = loss.ewm(com=period-1,min_periods=period).mean()
    df['Rsi'] = 100 - (100/(1+abs(avg_gain/avg_loss)))
    return df[['Date', 'Rsi']]
