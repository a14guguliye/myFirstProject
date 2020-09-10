import json 


def findBookByKeyword(_reqKeyword):
    with open('week07.json','r') as myExistingDb:
        data=json.load(myExistingDb)
    foundBooks=[]
    books=data['kitablar']

    for book in books:
        bookName=book['ad']
        if _reqKeyword in bookName:
            foundBooks.append(book)
    
    return foundBooks

searchedKeyword=input("Please enter a keyword to look for:")
print(findBookByKeyword(searchedKeyword))
