import json


def addBook():
    _name=input("Please enter book name:")
    _price1=input("Please enter book cost:")
    _pageCount=input("Please enter page count:")


    new_book={
        'ad':_name,
        'qiymet':_price1,
        'sehifeSayi':_pageCount
    }

    with open('week07.json','r') as existingDb:
        data=json.load(existingDb)

    
    data['kitablar'].append(new_book)
    with open('week07.json','w') as existingDb:
        json.dump(data,existingDb)



addBook()