#use historical data

garanti['simple return'] = (garanti['Adj Close'] / garanti['Adj Close'].shift(1)) - 1

print(garanti['simple return'])
