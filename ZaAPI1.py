import requests
import pprint
import json
print('#','-'*10, 'Вывод всех категорий ','-'*20)
res = requests.get('https://fakestoreapi.com/products/categories')
data = res.json()
pprint.pprint(data)
print('#','-'*10, 'Вывод выбранной категорий ','-'*20)
z= [i for i in range(len(data))]
t = "Для просмотра категории товара введите нужную цифру"
print(t, end=" ")
sl = {i:j for (i,j) in zip(z, data) }
print(sl)
v = int(input('Введите цифру'))
f = sl.get(v)
print(f)
t = 'https://fakestoreapi.com/products/category/' + f
print('#','-'*10, 'URL выбранной категории ','-'*20)
print(t)
rett= requests.get(t).json()
#pprint.pprint(rett)
#--------------подготовка к отображению-----------------------------------------
m=['Id:','Название:','Цена:','Описание:','Категория:','Рисунок:','Рейтинг:']
for i in rett:
    n=0
    for j in i:
        if j == "rating":
            print("Рейтинг:",end=' ')
            h = dict(i[j])
            print('ставка:',h['rate'],end='')
            print(" считать", h['count'])
        else:
            print(m[n],i[j])
            n +=1 
    print('-'*55)
       
