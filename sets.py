# no hay orden en los set

set= {}


set= {'sara', 'isabela', 'daniela', 'luisa', 'maria'}
print(type(set))

#print(set[0])  TypeError: 'set' object is not subscriptable

#no aceptan repetidos
set.add('sara')
print(set)

set.add('wilson')
print(set)

set1= {'sara', 'isabela', 'daniela', 'luisa', 'maria'}

set.difference_update(set1)
print(set)
