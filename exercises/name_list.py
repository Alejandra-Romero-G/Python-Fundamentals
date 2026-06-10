#I want a progran to asck the user for 5 names.
#Thase names will be displayed at the end, after they have all been entered.
#if the user enters a repeated name, they must be asked to enter another one, meaning I want 5 unique names with no duplicates.

print("***************** Name list *************************")
name_list = []
count = 1
while(len(name_list) != 5):
    print(f"Introduce {6-count} names : ")
    name = input("-> ")
    
    if(len(name_list) == 0):
        name_list.append(name)
        count += 1
    else:
        exist = False
        for names in name_list:
            print("im here")
            if(names.upper() == name.upper()):
                exist = True
                break
        if (exist == False ):
            name_list.append(name)
            count +=1
        print("--------------------------")
    print(" names in list", len(name_list))
for n in name_list:
    print(n)
print("end program")