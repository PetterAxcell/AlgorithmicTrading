
''' Plot RSI
plt.gcf().autofmt_xdate()
df['Rsi'].plot(figsize=(15,7.5))
plt.ylim(0,100)
plt.axhline(70, color = 'Purple')
plt.axhline(30, color = 'Purple')
plt.axhspan(30, 70,color='purple', alpha = 0.25)
plt.title('RSI')
plt.show()'''

'''Plot BB
df[['Close','30_MA_Close','Upper','Lower']].plot(figsize=(12.5,5))
plt.title('Bollinger bands (BB)')
plt.show()'''
