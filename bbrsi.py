import backtrader as bt

#Create a Stratey
class MyStrategy(bt.Strategy):
    params = dict(period=20)