import pandas as pd
import backtrader as bt
import matplotlib.pyplot as plt
import datetime as dt
import talib

#from MyCSVData import *

class BBands(bt.Indicator):
    
    # def bollinger_bands(serie, windows=20, stds=2,pd):
    def __init__(self):
        df=self.data
        print(df)
        #df=pd.read_csv("data", usecols= ['Date','Close'])
        # # Calculating 30 days moving average
        # df['30_MA_Close'] = df['Close'].rolling(window=30).mean()
        # # Calculating 20 days rolling standard devtaion
        # df['20_std_Close'] = df['Close'].rolling(window=20).std()
        # # Upper Bollinger Bands = Mean+2*SD
        # df['Upper'] = df['30_MA_Close'] + 2*df['20_std_Close']
        # # Lower Bollinger Bands = Mean-2*SD
        # df['Lower'] = df['30_MA_Close'] - 2*df['20_std_Close']
