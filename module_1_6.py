my_dict={'Maria':2000,'Paulo':1978,'Lena':1758,'Pepa':2015}
print(my_dict)
print(my_dict['Lena'])
print(my_dict.get('Nikita'))
my_dict.update({'Lola':1899,'Misha':1887})
a=my_dict.pop('Maria')
print(a)
print(my_dict )


my_set={1,2,'Молоко',1,2,2,127,0,7,77,127,1,1,77,7}
print(my_set)
my_set.add(777)
my_set.add('Хлеб')
my_set.discard(0)
print(my_set)