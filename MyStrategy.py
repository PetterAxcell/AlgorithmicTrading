import backtrader as bt
import numpy as np

class MyStrategy (bt.Strategy):

    #Parametros de los indicadores
    params = (('BBandsperiod', 20),('devfactor',2), ('RSIperiod',14))

    def log(self, txt, dt=None):
        ''' Logging function for this strategy'''
        dt = dt or self.datas[0].datetime.date(0)
        print('%s, %s' % (dt.isoformat(), txt))


    def __init__(self):
        self.dataclose = self.datas[0].close
        self.rsi=bt.indicators.RSI_SMA(period=self.p.RSIperiod,plotname='mysma')
        self.bband = bt.indicators.BollingerBands(period=self.p.BBandsperiod, devfactor=self.p.devfactor)
       
    
    def next(self):
        
            if self.rsi[0] < 30:
                self.log('BUY CREATE, %.2f' % self.dataclose[0])
                self.close()
     
            if self.rsi[0] >70:
                self.sell()
                print(self.position)
                self.log('SELL CREATE, %.2f' % self.dataclose[0])
                
                
                
                
                    


# self.log('SELL CREATE, %.2f' % self.dataclose[0])
#                     self.sell()


    # def next(self):
            
    #     for index,row in df.iterrows():
    #         if row['Rsi']<30 and (row['Lower'] > row ['Close']):
    #             self.buy()
