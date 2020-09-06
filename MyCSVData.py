from __future__ import (absolute_import, division, print_function,unicode_literals)
#from backtrader_plotting import Bokeh
import datetime
from bb import *
from MyStrategy import * 
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
# b = Bokeh(style='bar', plot_mode='single')

cerebro.plot(style='candlestick',grid='true', barup='#4db6ac', bardown='#1976d2',)