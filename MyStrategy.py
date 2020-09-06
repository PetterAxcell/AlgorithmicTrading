import backtrader as bt
import numpy as np
import matplotlib.pyplot as plt
class MyStrategy (bt.Strategy):

    #Parametros de los indicadores
    params = (('BBandsperiod', 20),('devfactor',2), ('RSIperiod',14))
    

    def __init__(self):
        self.dataclose = self.datas[0].close
        self.rsi=bt.indicators.RSI_SMA(period=self.p.RSIperiod,plotname='mysma')
        self.bband = bt.indicators.BollingerBands(period=self.p.BBandsperiod, devfactor=self.p.devfactor)
        #self.bband.plotlines=dict(mid=dict(ls='--'),top=dict(_samecolor=True),bot=dict(_samecolor=True),)
        



    # def next(self):
    #     if not self.position:
    #         if self.rsi < 30:
    #             self.buy(size=100)
    #     else:
    #         if self.rsi > 70:
    #             self.sell(size=100)


    # def next(self):
            
    #     for index,row in df.iterrows():
    #         if row['Rsi']<30 and (row['Lower'] > row ['Close']):
    #             self.buy()
