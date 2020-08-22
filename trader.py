import backtrader as bt
import datetime
from bbrsi import MyStrategy 


#Create a cerebro entity
cerebro = bt.Cerebro()

 #Add a strategy
cerebro.addstrategy(MyStrategy)

#Set our desired cash start
cerebro.broker.set_cash(1000)


# Create a Data Feed
data = bt.feeds.YahooFinanceCSVData(
    dataname='BTCUSDT.csv',
    # Do not pass values before this date
    fromdate=datetime.datetime(2020, 8, 20),
    # Do not pass values after this date
    todate=datetime.datetime(2020, 12, 31),
    reverse=False)

#Add Data Feed to Cerebro
cerebro.adddata(data)

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
