from bbrsi import *
import backtrader as bt

class MyStrategy (bt.Strategy):
        
        def next(self):
            data = 'BTCUSDT.csv'

            df = pd.read_csv(data)
            df = pd.merge(df,BB(data), on = 'Date')
            df = pd.merge(df,RSI(data), on = 'Date')


            df=df[30:]

            for index,row in df.iterrows():
                if row['Rsi']<30 and (row['Lower'] > row ['Close']):
                    self.buy()
