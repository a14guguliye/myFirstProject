#!/usr/bin/env python
# coding: utf-8

# In[1]:
# week 08
import json

with open('week07.json','r') as db:
    data=json.load(db)

print(data)

new_book={
    'ad':'deli kur',
    'qiymet':20,
    'sehife':200
}

data["kitablar"].append(new_book)


with open('week07.json','w') as db1:
    json.dump(data,db1)






#week 07 
def mod2function():
    x=int(input("Please enter a number:"))
    if(x%2==0):
        print("even")
    else:
        print("odd")
        


# In[3]:


# In[5]:


def Foo():
    x=7
    
    def Bar():
        x=5
        print(f"Bar function: {x}")
    
    Bar()
    print(f"Foo function: {x}")
Foo()


# In[34]:


books=[]
def melumatlariAl():
    kitabAd=input("Kitab adini daxil edin:")
    kitabSehife=int(input("Kitab sehifesini daxil edin:"))
    kitabQiymet=int(input("Kitab qiymetini daxil edin:"))
    
    return [kitabAd,kitabSehife, kitabQiymet]


# In[35]:


def kitabYarat():
    receivedInfo=melumatlariAl()
    book={
        'Kitabin Adi':receivedInfo[0],
        'Kitabin Sehifesi':receivedInfo[1],
        'Kitabin Qiymeti':receivedInfo[2]}
    return book
    


# In[36]:


def kitabElaveEt():
    new_book=kitabYarat()
    books.append(new_book)
    file=open(r"C:\Users\Hp\OneDrive\Desktop\learning_\week 7\week07.json","a")
    file.write(str(new_book)+"\n")

# In[38]:



# In[39]:



# In[ ]:




