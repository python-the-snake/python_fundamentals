'''
метод = функция внутри класса

class Dog:
     def bark(self):
         print("BARK")
пример

мы можем приравнять объекты к классу, они будут подчиняться его правилам:
mydog = Dog()
mydog.bark() - здесь ничего не сработает, если мы не напишем в основной функции self в скобках.
мы можем продолжать создавать характеристику элементу класса:
mydog.age  = 10
mydog.name = "Fido"

но выводить все эти данные нужно по отдельности: print(mydog.name)

def __init__(self, name, age)
    self.age = age
    self.name = name

'''


class Car:
    def __init__(self, year, make, model):
        self.year = year
        self.make = make
        self.model = model
    def age(selfelf):
        return 2020 - self.year


