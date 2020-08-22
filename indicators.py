import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#def bollinger_bands(serie, windows=20, stds=2,pd): 
df=pd.read_csv('BTCUSDT.csv', index_col='Date')
df.tail()

#Calculating 30 days moving average
df['30_MA_Close'] = df['Close'].rolling(window=30).mean()
#calculating 20 days rolling standard devtaion
df['20_std_Close'] = df['Close'].rolling(window=20).std()

df.head(31)

# Upper Bollinger Bands = Mean+2*SD
# Lower Bollinger Bands = Mean-2*SD
df['Upper'] = df['30_MA_Close'] + 2*df['20_std_Close']
df['Lower'] = df['30_MA_Close'] - 2*df['20_std_Close']

print(df)

df[['Close','30_MA_Close','Upper','Lower']].plot(figsize=(15,5))


# df['Close'].plot()
plt.show()