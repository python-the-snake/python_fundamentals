'''
dictionaryname = {} - словарь. нумеровка элементов словаря идет с 1 и тд

словарь позволяет создавать элементы с качествами:
DictionaryName = {'Element1':1, 'Element2':2, 'Element3':3}

важным отличием от списков у словаря помимо начала отсчета является его неупорядоченность. при выдаче элементы будут
обязательно стоять сосвоими характеристиками, но не обязательно в изначальном порядке.

словари позволяют запрашивать элемент, сопряженный с основным, вводом первого:
print(dictionaryname['element1']) - выводом будет 1 (см. строку 4)

удаление элементов из словаря работает по тому же принципу, что и из списка:
del(dictionaryname['element1'])

в словари необязательно вставлять элементы посредством команды .insert можно так же написать dictionaryname['element1'] = 1
после основного куска словаря и он добавит его значение в общий массив данных

'''

words = ["PoGo","Spange","Lie-Fi"]
definitions = ["Slang for Pokemon Go","To collect spare change, either from couches, passerbys on the street or any numerous other ways and means","When your phone or tablet indicates that you are connected to a wireless network, however you are still unable to load webpages or use any internet services with your device"]

cooldictionary = {}
for i in range (0,3):
    cooldictionary[words[i]] = definitions[i]

print(cooldictionary)



