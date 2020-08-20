import backtrader as bt
import datetime
from strategies import TestStrategy 


#Create a cerebro entity
cerebro = bt.Cerebro()

 #Add a strategy
cerebro.addstrategy(TestStrategy)

# Create a Data Feed
data = bt.feeds.YahooFinanceCSVData(
    dataname='BTCUSDT.csv',
    # Do not pass values before this date
    fromdate=datetime.datetime(2020, 8, 1),
    # Do not pass values after this date
    todate=datetime.datetime(2020, 12, 31),
    adjclose = False,
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
#cerebro.plot()
