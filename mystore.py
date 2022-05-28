#!/usr/bin/env python
# coding: utf-8

# In[3]:


#from pyfiglet import Figlet
#import qrcode

def loadd():
   print('loading...')
   myfile=open('store.txt','r+')
   data=myfile.read()
   productList=data.split('\n')
   for i in range(len(productList)):
       if productList[i]=='':
           break
       productInfo=productList[i].split(',')
       dict={}
       dict['id']=productInfo[0]
       dict['name']=productInfo[1]
       dict['price']=productInfo[2]
       dict['number']=productInfo[3]
       PRODUCT.append(dict)
   print('welcome')
def showMenu():
   print('1-add product')
   print('2-edit product')
   print('3-search product with name')
   print('4-delete product')
   print('5-show product')
   print('6-buy product')
   print('7-Exit')
   print('8-qrcode')
   
def showProduct():
   for i in range(len(PRODUCT)):
       print(PRODUCT[i])
def addProduct():
   dict={}
   dict['id']=int(input('enter id'))
   dict['name']=input('enter name')
   dict['price']=int(input('enter price'))
   dict['number']=int(input('enter number of product'))   
   PRODUCT.append(dict) 
   print('prodact added')
   
def editProduct():
   productdict=searchName()
   if productdict!='product not found':
       print('1-edit id')
       print('2-edit name')
       print('3-edit price')
       print('4-edit number of product')
       num=int(input('enter number'))
       if num==1:
           productdict['id']=int(input('enter new id'))
           print('id updated')   
       elif num==2:
           productdict['name']=input('enter new name')
           print('name updated') 
       elif num==3:
           productdict['price']=int(input('enter new price'))
           print('price updated')
       elif num==4:
           productdict['number']=int(input('enter new number of product'))
           print('number of product updated')
   else:
       print('product not found')
def deleteProduct():
   txt=input('enter name of product')
   for product in PRODUCT:
       if txt==product['name']:
           PRODUCT.remove(product)
           print('product deleted')
           break
   else:
           print('product not found')
def searchName():
   txt=input('enter name of product')
   for product in PRODUCT:
       if txt==product['name']:
           return product
   else:
           return 'product not found'
def searchid():
   txt=input('enter id of product or enter * for exit')
   if txt=='*':
       return '*'
   for product in PRODUCT:
       if txt==product['id']:
           return product
   else:
           return 'product not found'
def buy():
   sabadKharid=[]
   dic={}
   while True:
       productdict=searchid()
       if productdict=='*':
           print(sabadKharid)
           break
       
       elif productdict!='product not found':
           num=int(input('enter number of product you want to buy'))
           productNumber=int(productdict['number'])
           if num<=productNumber:
               productNumber-=num
               dic['number']=num
               dic['name']=productdict['name']
               dic['price']=int(productdict['price'])
               dic['sumprice']=int(productdict['price'])*num
               sabadKharid.append(dic)
               productdict['number']=productNumber
               print('mahsool be sabade kharid ezafe shod')
           else:
               print('mojoodi nakafi')
       elif productdict=='product not found':
           print('product not found')
           
#def qcode():
   #id= searchid()
   #img=qrcode.make(id)
   #img.save('qrcode.png')
PRODUCT=[]
loadd()
while True:
   showMenu()
   #f=Figlet(font='standard')
   #print(f.renderText('store'))
   num=int(input('enter a number:'))
   if num==1:
       addProduct()
   elif num==2:
       editProduct()
   elif num==3:
       print(searchName())
   elif num==4:
       deleteProduct()
   elif num==5:
       showProduct()
   elif num==6:
       buy()
   elif num==7:
       myfile=open('store.txt','w')

       for i in range(len(PRODUCT)):
           if i<len(PRODUCT):
               myfile.write(str(PRODUCT[i]['id'])+','+PRODUCT[i]['name']+','+str(PRODUCT[i]['price'])+','+str(PRODUCT[i]['number'])+'\n')
           else:
               myfile.write(str(PRODUCT[i]['id'])+','+PRODUCT[i]['name']+','+str(PRODUCT[i]['price'])+','+str(PRODUCT[i]['number']))

       myfile.close()
       break
       exit()
   elif num == 8:
       #qcode()
       pass


# In[ ]:


pip install pyfiglet


# In[ ]:




