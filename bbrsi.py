from bb import BB
from rsi import RSI
import matplotlib.pyplot as plt
import datetime as dt
import numpy as np
import pandas as pd

def buy_order(money, data):
    #a = 0
    return 0

def sell_order(money, data):
    #a = 0
    return 0

def BBRSI():
    money = 100000
    active = False
    data = 'BTCUSDT.csv'
    
    df2 = pd.read_csv(data)
    df = pd.merge(BB(data),RSI(data), on = 'Date')
    df['Close']= df2.loc[:,['Close']]

    df = df[30:-6] #Start at 30 because BB period = 30
    
    # for index,row in df.iterrows():
    #     if row['Rsi']<30 & row['Lower'] < row ['Close']:
    #         print(row['Rsi'])


    # for index, row in df.iterrows():
    #     # BUY CONDITION
    #     '''The buy condition should act if df['Rsi'] >= 30 and it last position was below 30'''
    #     if ((df['Rsi'][row]< 30) & (df['Lower'][row] < df ['Close'][row]) & active == False):
    #         buy_order(money, df['Close']) 
    #         active = True

    # SELL CONDITION
    '''The program should act when actual_price reaches df['30_MA_Close'], however i am going to test when
        close_price reaches this position
    if(df['Close'] == df['30_MA_Close'] & active == True): 
        sell_order(money,df['Close'])
        active = False'''
    print(df)


BBRSI() 