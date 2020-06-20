'''
list[] - упорядоченнай массив данных, сохраняющийся в этом порядке всегда.

listname.insert() - добавление данных в список. в скобках пишется номер места, на которое нужно поместить данные.
данные в списке считаются с 0, т.е. первая единица данных будет под номером 0

print(listname[0]) - выпишет первую единицу данных в списке

del(listname[0]) - удалит первую единицу данных в списке. вторая займет метсто первой и отчет пойдет с нее.

print(len(listname)) - выпишет длинну списка
'''

ShoesNameList = ['Spizikes', 'Air Force 1', 'Curry 2', 'Melo 5']
print(ShoesNameList)
del(ShoesNameList[1])
print(ShoesNameList)
print(len(ShoesNameList))
ShoesNameList.insert(1, 'Air Forse 1')
print(len(ShoesNameList))
