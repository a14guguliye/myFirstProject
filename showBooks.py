import json 

with open('week07.json','r') as myMainDb:
    data=json.load(myMainDb)

name="ad"
price="qiymet"
pageCount="sehifeSayi"
for book in data['kitablar']:
    print(f"\nKitab adi: {book[name]}, Kitabin qiymeti: {book[price]}, Kitabin sehife sayi: {book[pageCount]}\n")
