# Installasi :
#  --> pip install requests
#  --> pip install bs4
#  --> pip install pandas

import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {
		"User-Agent":"Mozilla/5.0 (Windows NT 10.0; ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36", 
		"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", # Menginformasikan server tentang jenis data yang dapat dikirim kembali
		"Accept-Encoding":"gzip, deflate", # Algoritma pengkodean
		"Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8,id;q=0.7", # Menginformasikan server tentang bahasa yang dikirim oleh server
		}
keyword = input("Cari barang yang akan di extract : ")
url = "https://www.amazon.com/s?k="+keyword
r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, features="lxml")
all_data = pd.DataFrame()
# print(soup)

for d in soup.findAll('div', {'class':'sg-col-4-of-12 sg-col-8-of-16 sg-col-16-of-24 sg-col-12-of-20 sg-col-24-of-32 sg-col sg-col-28-of-36 sg-col-20-of-28'}):
	# Nama Barang
	if str(d.find('span', {'class':'a-size-medium a-color-base a-text-normal'})) != "None":
		name = d.find('span', {'class':'a-size-medium a-color-base a-text-normal'}).get_text()
	else:
		name = "Unknown Name"

	# Rating
	if str(d.find("div", {"class" : "a-row a-size-small"})) != "None":
		rating = d.find('span', {'class':'a-icon-alt'}).get_text()
		rating = rating.replace(" out of 5 stars", "")
	else:
		rating = "Tidak Ada Rating"

	# Jumlah Barang yang terjual
	if str(d.find('span', {'class':'a-size-base'})) != "None":
		terjual = d.find('span', {'class':'a-size-base'}).get_text()
		terjual = terjual.replace(",", "")
	else:
		terjual = "Belum Terjual"

	# Harga dalam Dolar ($)
	if str(d.find('span', {'class':'a-offscreen'})) != "None":
		price = d.find('span', {'class':'a-offscreen'}).get_text()
		price = price.replace("$", "")
		price = price.replace(",", "")
	else:
		price = "0"

	# Harga dalam Rupiah (Rp)
	kurs = float(price) * float(14806)

	# Data digabung
	all_data = all_data.append({"Harga_Dollar": price, "Harga_Rp": kurs, "Nama_Barang" : name, "Rating" : rating, "Terjual" : terjual}, ignore_index=True)

print(all_data)

all_data.to_csv("data_{}.csv".format(keyword), index=False)
print("\nData Sudah Tersimpan dengan nama : data_{}.csv".format(keyword))