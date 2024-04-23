my_list= [43,44,34,'sara','isabela',]
#print(type(my_list))

print(my_list)
print(my_list[3])

# funciones para la lista

my_list.append('daniela') #agregar objeto
print(my_list)

my_list.insert(0, 'luisa') #agregar objeto donde queramos
print(my_list)

my_list.remove(43) # quita objetos
print(my_list)

my_list.pop(2) # quita objetos en una posicion especifica
print(my_list)

print(my_list.count('sara'))

my_list.reverse() # cambia el orden
print(my_list)