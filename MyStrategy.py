import backtrader as bt
import talib
import numpy as np

class MyStrategy (bt.Strategy):

    #Parametros de los indicadores
    params = (('BBandsperiod', 20),('devfactor',2), ('RSIperiod',14))
    
    
    def __init__(self):
        self.dataclose = self.datas[0].close
        self.RSI=talib.RSI(np.array(self.dataclose), self.p.RSIperiod)
        self.BBUpper,self.BBmiddle,self.BBlower=talib.BBANDS(np.array(self.dataclose), self.p.BBandsperiod,self.p.devfactor,self.p.devfactor)
        print(self.BBUpper)



    # def next(self):
            
    #     for index,row in df.iterrows():
    #         if row['Rsi']<30 and (row['Lower'] > row ['Close']):
    #             self.buy()
