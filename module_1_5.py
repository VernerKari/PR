immutabel_var=(1,2,3,'appel','sun',0.25,5.47)
print(immutabel_var)
#immutabel_var[4]='pen'
#Я не могу изменить элемент кортежа, так как он содержит в себе ссылку на список, а не элементы списка.

mutabel_list=[1,10,100,'сова','лампа','лапша']
mutabel_list[3]='лебедь'
print(mutabel_list)