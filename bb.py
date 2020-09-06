
import matplotlib.pyplot as plt

#plt.style.use('bmh')

plt.rcParams["figure.figsize"] = (10, 6)
plt.rcParams['lines.linewidth'] = 1

#SIZE = 7
plt.rcParams['axes.labelsize'] = 1
# plt.rcParams['ytick.labelsize'] = SIZE
# plt.rcParams['xtick.labelsize'] = SIZE
#plt.rcParams["font.size"] = 2

COLOR = '1'
plt.rcParams['text.color'] = '#373c4c'
#plt.rcParams['axes.labelcolor'] = "#96989A"
plt.rcParams['xtick.color'] = COLOR
plt.rcParams['ytick.color'] = COLOR


plt.rcParams['grid.linewidth']=0.1
plt.rcParams['grid.color']="0.3"
# plt.rcParams['lines.color']="0.5"
# plt.rcParams['axes.edgecolor']="0.2"
# plt.rcParams['axes.linewidth']=0.5

plt.rcParams['figure.facecolor']="#131722" #Para la parte de afuera
plt.rcParams['axes.facecolor']="#131722" #Para la parte de dentro
# plt.rcParams["savefig.dpi"]=120
# dpi = plt.rcParams["savefig.dpi"]
# width = 700
# height = 1200
# plt.rcParams['figure.figsize'] = height/dpi, width/dpi
#plt.rcParams["savefig.facecolor"] ="#101622"
# plt.rcParams["savefig.edgecolor"]="#101622"

#plt.rcParams['legend.fontsize'] = SIZE
# plt.rcParams['legend.title_fontsize'] = SIZE + 1
# plt.rcParams['legend.labelspacing'] =0.25
# plt.rcParams['image.cmap']='tab10'
















# #def bollinger_bands(serie, windows=20, stds=2,pd): 
# df=pd.read_csv('ETHUSD.csv', index_col='Date')
# df.tail()

# #Calculating 30 days moving average
# df['30_MA_Close'] = df['Close'].rolling(window=30).mean()
# #calculating 20 days rolling standard devtaion
# df['20_std_Close'] = df['Close'].rolling(window=20).std()

# df.head(31)

# # Upper Bollinger Bands = Mean+2*SD
# # Lower Bollinger Bands = Mean-2*SD
# df['Upper'] = df['30_MA_Close'] + 2*df['20_std_Close']
# df['Lower'] = df['30_MA_Close'] - 2*df['20_std_Close']

# print(df)

# df[['Close','30_MA_Close','Upper','Lower']].plot(figsize=(15,5))


# # df['Close'].plot()
# plt.show()




# def __init__(self):
#         # def bollinger_bands(serie, windows=20, stds=2,pd): 
#         df=pd.read_csv(data, usecols= ['Date','Close'])
#         # Calculating 30 days moving average
#         df['30_MA_Close'] = df['Close'].rolling(window=30).mean()
#         # Calculating 20 days rolling standard devtaion
#         df['20_std_Close'] = df['Close'].rolling(window=20).std()
#         # Upper Bollinger Bands = Mean+2*SD
#         df['Upper'] = df['30_MA_Close'] + 2*df['20_std_Close']
#         # Lower Bollinger Bands = Mean-2*SD
#         df['Lower'] = df['30_MA_Close'] - 2*df['20_std_Close']
#         return df[['Date', 'Upper','30_MA_Close','Lower']]


# import pandas as pd
# import matplotlib.pyplot as plt

# def RSI(data, period = 14):
#     # Get Data
#     df=pd.read_csv(data, usecols=['Date','Close'])
#     chg = df['Close'].diff(1)
#     gain = chg.mask(chg < 0,0)
#     loss = chg.mask( chg > 0,0)
#     avg_gain = gain.ewm(com=period-1,min_periods=period).mean()
#     avg_loss = loss.ewm(com=period-1,min_periods=period).mean()
#     df['Rsi'] = 100 - (100/(1+abs(avg_gain/avg_loss)))
#     return df[['Date', 'Rsi']]

