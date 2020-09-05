import backtrader as bt
import datetime
#from bbrsi import *
#from TestStrategy import TestStrategy 
from MyStrategy import MyStrategy 

#Create a cerebro entity
cerebro = bt.Cerebro()

 #Add a my strategy
cerebro.addstrategy(MyStrategy)

# Add TestStrategy
#cerebro.addstrategy(TestStrategy)

#Set our desired cash start
cerebro.broker.set_cash(1000)

data = bt.feeds.GenericCSVData(
    dataname='BTCUSDT.csv',

    fromdate=datetime.datetime(2019, 1, 1),
    todate=datetime.datetime(2020, 12, 31),

    nullvalue=0.0,

    dtformat=('%Y-%m-%d'),
    tmformat=('%H:%M:%S'),

    date=0,
    time=6,
    high=2,
    low=3,
    open=1,
    close=4,
    volume=5,
    openinterest=-1,
)

#Add Data Feed to Cerebro
cerebro.adddata(data)

#Set our desired cash start
cerebro.broker.set_cash(1000.0)

#Set the comission
cerebro.broker.setcommission(commission=0.01)

# Print out the starting conditions
print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())

# Run over everything
cerebro.run()

# Print out the final result
print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())

#Plot the result
#cerebro.plot()
