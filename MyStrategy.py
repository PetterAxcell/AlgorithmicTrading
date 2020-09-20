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
        #keep a reference to the close
        self.dataclose = self.datas[0].close
        
        #add a BBand and RSI
        self.rsi=bt.indicators.RSI_SMA(period=self.p.RSIperiod,plotname='mysma')
        self.bband = bt.indicators.BollingerBands(period=self.p.BBandsperiod, devfactor=self.p.devfactor)


        #keep track of pending orders and buy price/commission
        self.order = None
        self.buyprice = None
        self.buycomm = None


    def notify_order(self, order):
        if order.status in [order.Submitted, order.Accepted]:
            # Buy/Sell order submitted/accepted to/by broker - Nothing to do
            return

        # Check if an order has been completed
        # Attention: broker could reject order if not enougth cash
        if order.status in [order.Completed, order.Canceled, order.Margin]:
            if order.isbuy():
                self.log(
                    'BUY EXECUTED, Price: %.2f, Cost: %.2f, Comm %.2f' %
                    (order.executed.price,
                     order.executed.value,
                     order.executed.comm))

                self.buyprice = order.executed.price
                self.buycomm = order.executed.comm
            else:  # Sell
                self.log('SELL EXECUTED, Price: %.2f, Cost: %.2f, Comm %.2f' %
                         (order.executed.price,
                          order.executed.value,
                          order.executed.comm))

            self.bar_executed = len(self)

        # Write down: no pending order
        self.order = None
    

    def notify_trade(self, trade):
        if not trade.isclosed:
            return

        self.log('OPERATION PROFIT, GROSS %.2f, NET %.2f' %
                 (trade.pnl, trade.pnlcomm))
    
    def next(self):

        if self.order:
            return

        if not self.position:

            
            if self.rsi[0] < 30:
                self.order=self.buy()

        else:

            if self.rsi[0] > 70:
                self.order=self.sell()
                    
                
                
                
                    


# self.log('SELL CREATE, %.2f' % self.dataclose[0])
#                     self.sell()


    # def next(self):
            
    #     for index,row in df.iterrows():
    #         if row['Rsi']<30 and (row['Lower'] > row ['Close']):
    #             self.buy()
