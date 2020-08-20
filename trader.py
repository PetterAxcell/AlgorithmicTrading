import backtrader 

cerebro = backtrader.Cerebro()
cerebro.broker.set_cash(10000000)
print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())

cerebro.run()

print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())
