import backtrader as bt
import numpy as np

class MyStrategy (bt.Strategy):

    #Parametros de los indicadores
    params = (('BBandsperiod', 20),('devfactor',2), ('RSIperiod',14))
    
    def __init__(self):
        self.dataclose = self.datas[0].close
        self.rsi=bt.indicators.RSI_SMA(period=self.p.RSIperiod,plotname='mysma')
        self.bband = bt.indicators.BollingerBands(period=self.p.BBandsperiod, devfactor=self.p.devfactor)
       
    
    def next(self):
        if self.dataclose[0] < self.dataclose[-1]:
            if self.dataclose[-1] < self.dataclose[-2]:
                self.buy()
                
                    


# self.log('SELL CREATE, %.2f' % self.dataclose[0])
#                     self.sell()


    # def next(self):
            
    #     for index,row in df.iterrows():
    #         if row['Rsi']<30 and (row['Lower'] > row ['Close']):
    #             self.buy()
