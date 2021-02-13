# Installasi :
#  --> pip install matplotlib

import pandas as pd
import matplotlib.pyplot as plt

nama_file = input("Masukkan nama file csv : ")
dataframe = pd.read_csv(nama_file)
# print(dataframe)

x = dataframe.Harga_Rp
y = dataframe.Terjual

# Add x dan y labels, and set theor font size
plt.xlabel("Harga dalam Rupiah", fontsize=20)
plt.ylabel("Terjual", fontsize=20)

# plot them as a scatter chart
plt.scatter(x, y)

# Show it in Spyder
plt.show()