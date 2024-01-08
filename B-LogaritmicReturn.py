garanti["log return"] = np.log(garanti['Adj Close'] / garanti['Adj Close'].shift(1))

print(garanti["log return"])

# log return visualization

import matplotlib.pyplot as plt

garanti['log return'].plot(figsize = (15, 8))

plt.title("Garanti Logaritmic Return")

plt.xlabel("Time")

plt.ylabel("Logaritmic Return")

plt.show()
