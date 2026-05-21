#List and tuples
my_list=[3,5,7,11,2,9,88]
# We can print or order the list directly
print(my_list)#[3, 5, 7, 11, 2, 9, 88]
my_list.sort()
print(my_list)#[2, 3, 5, 7, 9, 11, 88]
#reverse order
my_list.sort(reverse=True)
print(my_list)#[88, 11, 9, 7, 5, 3, 2]

#iterate over a list
number_list = [1,6,99,0]
for i in range(len(number_list)):
    print (number_list[i])


name_list = ["Ale", "Sebastian","King","Ale"]#index 0,1,2,3
# We can search for the name by its index
print("Name 3 :", name_list[2])
print("Name 1:", name_list[0])
# We can add a new element to the end of the list
name_list.append("Casie")##['Ale', 'Sebastian', 'King', 'Ale', 'Casie']
# We can insert a new element at a specific position
name_list.insert(1,"amoung")#['Ale','amoung', 'Sebastian', 'King', 'Ale', 'Casie']
# This method removes the first element it finds
name_list.remove("Ale")
print(name_list)#['amoung', 'Sebastian', 'King', 'Ale', 'Casie']
# We can remove an element by its index too range
name_list.pop(0)#['Sebastian', 'King', 'Ale', 'Casie']
del name_list[0:2]
print(name_list)#['Ale', 'Casie']
# We can search elemen in the list
asnwer='No'
result= 'King' in name_list #False 
if (result):
    asnwer='in your dreams'
print('Is King real? ',asnwer)
# We can drop the list
name_list.clear()
print(name_list) #[]

print("*****************************************")
#TUPLES
my_tuple=("milk", "Cacao","Hazelnut","Sugar")
print("tuple 1:", my_tuple[0])
# We cannot modify a tuple
#my_tuple[1] = "Coconut" #-->Error
print(my_tuple)