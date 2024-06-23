import requests
import pprint
import json

print('#','-'*10, 'Вывод всех карзин','-'*20)
res = requests.get('https://fakestoreapi.com/carts')
data = res.json()
pprint.pprint(data)
f = open('carts.txt','w+',encoding='utf-8')
for key in data:
     f.writelines(key)
f.close()

#-------Функция определения Username -----------------------
def usernam(b):
    h = str(b)
    t = 'https://fakestoreapi.com/users/' + h
    #print(t)
    reUs= requests.get(t)
    dat = reUs.json()
    #pprint.pprint(dat)
    for key in dat:
        if key == "name":
            usr =dat[key]['firstname'] + " " + dat[key]['lastname']
    return usr
#-------------------------------------------------------------------
#-------Функция определения Товара -----------------------
def productnam(b):
    h = str(b);pro=''
    t = 'https://fakestoreapi.com/products/' + h
    #print(t)
    rePro= requests.get(t)
    dat = rePro.json()
    #pprint.pprint(dat)
    for key in dat:
        if key == 'title':
            pro =dat['title'] 
    return pro
#-------------------------------------------------------------------

print('-'*10,'Вывод первой карзины',end=' ');print('-'*20)
for key in data:
    if key['id'] == 1:
        print(key['products'])
print("-"*50)
print('*'*10,'Вывод карзины по выбору','*'*20)
b = int(input('Введите номер карзины для просмотра '))
k=0
for key in data:
    if key['id'] == b:
        for i in key['products']:
            k=i['productId']
            print('Товар :', productnam(k), 'количество =', i['quantity'])
        print('Покупатель ',usernam(key['userId']))
        print(key['userId'])
print('*'*50)
