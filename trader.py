from __future__ import (absolute_import, division, print_function,unicode_literals)
#from backtrader_plotting import Bokeh
import datetime
from plot import *
import backtrader as bt
import datetime
#from bbrsi import *
from TestStrategy import TestStrategy 
#from MyStrategy import MyStrategy 

#Create a cerebro entity
cerebro = bt.Cerebro()

 #Add a my strategy
#cerebro.addstrategy(MyStrategy)

# Add TestStrategy
cerebro.addstrategy(TestStrategy)

#Set our desired cash start
cerebro.broker.set_cash(1000)



# Create a Data Feed
data = bt.feeds.YahooFinanceCSVData(
    dataname='ETHUSD.csv',
    # Do not pass values before this date
    #fromdate=datetime.datetime(2020, 8, 1),
    fromdate=datetime.datetime(2020, 1, 20),
    # Do not pass values after this date
    todate=datetime.datetime(2020, 12, 31),
    reverse = False)

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

cerebro.plot(style='candlestick',grid='true', barup='#4db6ac', bardown='#1976d2',)