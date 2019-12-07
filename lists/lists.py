#Ejemplo de una lista

#bicycles = ['Trek', 'cannodale', 'redline']
#print(bicycles[0].upper())

#Removing an item using DEl statement
# motorcycles = ['honda', 'yamaha', 'suzuki']
# del motorcycles[0]
# print(motorcycles)

#Removing an item using the pop() statement
motorcycles = ['honda', 'yamaha', 'suzuki']
# last_owned  = motorcycles.pop()

first_owned = motorcycles.pop(0)

print("The first motorcycle I owned was a " + first_owned.title())
