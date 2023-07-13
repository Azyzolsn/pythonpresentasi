import requests
import csv

url = 'https://api.bukalapak.com/multistrategy-products'
key = input('Masukkan kata kunci: ')
count = 0
data_list = []

for page in range(1, 100):
    parameter = {
        'keywords': key,
        'limit': 100,
        'offset': 0,
        'facet': False,
        'page': page,
        'shouldUseSeoMultistrategy': False,
        'isLoggedIn': 'false',
        'show_search_contexts': True,
        'access_token': 'eyJhbGciOiJSUzI1NiIsImtpZCI6ImFjY291bnRzLmp3dC5hY2Nlc3MtdG9rZW4iLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL2FjY291bnRzLmJ1a2FsYXBhay5jb20vIiwic3ViIjoiMjMxZDRhODY5MDVmMGYyNjJjNWUwM2ZjIiwiYXVkIjpbImh0dHBzOi8vYWNjb3VudHMuYnVrYWxhcGFrLmNvbSIsImh0dHBzOi8vYXBpLmJ1a2FsYXBhay5jb20iLCJodHRwczovL2FwaS5zZXJ2ZXJtaXRyYS5jb20iXSwiZXhwIjoxNjg4NzI0NzI1LCJuYmYiOjE2ODg3MTA1MDUsImlhdCI6MTY4ODcxMDUwNSwianRpIjoicmVKN1VsZnJQY2lHX2NDWFR4MlhxUSIsImNsaWVudF9pZCI6IjIzMWQ0YTg2OTA1ZjBmMjYyYzVlMDNmYyIsInNjb3BlIjoicHVibGljIn0.1597dRaJXCVaGBvPKq5hivg1Lb4uT2p7uGDtfpzU7cTRCyiUMyPjVcZ-laKugXbD5pb94J-vmIH1ScEt-mAWstLCXlCk5IJdIUK4od4AQYm92FmiVsXtj2c-K6Jv6Q3aqMGQXBIUVzYgVshHitZ70LsgfUfxDJvWqQbKFcxMru03sGw4KelaTaCEZT7rcCeVoZ4e9Di52TmNsPSbr6zZWQHV0sKGZ67HqDHm9Z9aIug0H9-3cn88jd_vSdw4iDDOSmf8SbSFYGAarOA4N71LaCX5UwgeIVa7Q0iCc2NJtivVfMhvqGgBgoKEr1Sy5_122pPeBKBSsE_8DYTdzgzDHQ'
    }

    r = requests.get(url, params=parameter).json()
    products = r['data']

    for i in products:
        name = i['name']
        harga = i['price']
        stock = i['stock']
        count += 1
        data_list.append([count, name, harga, stock])

# Membuka file CSV untuk menulis
with open('hasil.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['No', 'Nama', 'Harga', 'Stok'])
    writer.writerows(data_list)

print("Data telah berhasil diekspor ke hasil.csv")
