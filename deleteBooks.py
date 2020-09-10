import json
with open('week07.json','r') as myExistingDb:
    data=json.load(myExistingDb)


books = data["kitablar"]

i=0
for book in books:
    if(book['qiymet']=='20'):
        del data['kitablar'][i]
    
    i+=1


with open('week07.json','w') as existingDb:
    json.dump(data,existingDb)
