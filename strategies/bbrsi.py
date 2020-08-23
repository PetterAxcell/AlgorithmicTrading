import matplotlib.pyplot as plt
import datetime as dt
import pandas as pd

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

def BB(data):
    # def bollinger_bands(serie, windows=20, stds=2,pd): 
    df=pd.read_csv(data, usecols= ['Date','Close'])
    # Calculating 30 days moving average
    df['30_MA_Close'] = df['Close'].rolling(window=30).mean()
    # Calculating 20 days rolling standard devtaion
    df['20_std_Close'] = df['Close'].rolling(window=20).std()
    # Upper Bollinger Bands = Mean+2*SD
    df['Upper'] = df['30_MA_Close'] + 2*df['20_std_Close']
    # Lower Bollinger Bands = Mean-2*SD
    df['Lower'] = df['30_MA_Close'] - 2*df['20_std_Close']
    return df[['Date', 'Upper','30_MA_Close','Lower']]

def buy_order(money, data):
    #active = true
    return 0
    
def sell_order(money, data):
    #active = false
    return 0

if __name__ == '__main__':
    money = 10000
    active = False
    data = 'dataframes/BTCUSDT.csv'
    df = pd.merge(BB(data),RSI(data),on = 'Date')
    print(df)

    # Buy condition
    '''The buy condition should act if df['Rsi'] >= 30 and it last position was below 30'''
    if ((df['Rsi'] < 30) & (df['Lower'] < df ['Close']) & active == False):
        buy_order(money, df['Close']) 
        active = True

    # Sell condition
    '''The condition should act when actual_price reaches df['30_MA_Close'], however i am going to test when 
        close_price reaches this position'''
    if(df['Close'] == df['30_MA_Close'] & active == True): 
        sell_order(money,df['Close'])
        active = False

