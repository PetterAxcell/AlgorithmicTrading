from binance.client import Client
from datetime import datetime
from pandas import DataFrame as df
import key
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import pandas as pd

class BinanceBot:
    
    def __init__(self, s='empty'):
        self.show_data='Error'
        self.data='Error'
        self.symbol=s

    def GetData(self,s='BTCUSDT'): 
        self.symbol=s
        if self.symbol == 'empty':
            print('F')

        else:
            client = Client(api_key=key.api_key, api_secret=key.api_secret)
            candles = client.get_historical_klines(symbol=self.symbol, interval = Client.KLINE_INTERVAL_15MINUTE, start_str="3 Sep, 2020")
            candles_data_frame = df(candles)
            candles_data_frame_date = candles_data_frame[0]
            final_date = []


            for time in candles_data_frame_date.unique(): 
                readable=datetime.fromtimestamp(int(time/1000))
                final_date.append(readable)

            candles_data_frame.pop(0)
            candles_data_frame.pop(11)
            dataframe_final_date = df(final_date)

            final_dataframe=dataframe_final_date.join(candles_data_frame)

            final_dataframe.columns=('Date','Open', 'High', 'Low', 'Close', 'Volume', 'Close_time', 'Asset_volume', 'Trade_number', 'Taker_buy_base', 'Taker_buy_quote')

            # candles_data_frame_date = candles_data_frame[6]
            # for time in candles_data_frame_date.unique(): 
            #         readable=datetime.fromtimestamp(int(time/1000))
            #         final_date.append(readable)
            # dataframe_final_date = df(final_date)

            # final_dataframe['Close_time']=dataframe_final_date

            final_dataframe['Time'] = pd.to_datetime(final_dataframe['Date'], format='%Y:%M:%D').dt.time
            final_dataframe['Date'] = pd.to_datetime(final_dataframe['Date'], format='%Y-%M-%D').dt.date
            
                    
            final_dataframe=final_dataframe.drop(columns=['Close_time'])
            final_dataframe=final_dataframe.drop(columns=['Asset_volume'])
            final_dataframe=final_dataframe.drop(columns=['Trade_number'])
            final_dataframe=final_dataframe.drop(columns=['Taker_buy_base'])
            final_dataframe=final_dataframe.drop(columns=['Taker_buy_quote'])
            self.show_data=candles_data_frame
            self.data=final_dataframe
            print(final_dataframe)
            #Copy data to a .csv file
            final_dataframe.to_csv(path_or_buf="BTCUSDT.csv", index=False)

s="BTCUSDT"
X = BinanceBot(s)
X.GetData() 
