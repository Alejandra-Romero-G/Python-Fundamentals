print("*******************************")
# CREATE METHODS  DEF
def my_first_method():
    print('HII.. I am your first method')
my_first_method() #this only print dosent any return

def greething( paramether_name):
    text= f'Have a good day {paramether_name}'
    return text
x= greething('Ale') # now x is a text 
print(x) # Have a good day Ale

#Example methods return
print("-------------------")

def menu():
    print('Choose an option: ')
    print('1.- Convert to uppercase')
    print('2.- Convert to lowercase')
    print('3.- Concatenate text')
    print(' another number takes end program')
    option = int(input())
    return option

def upper_case(txt):
    return txt.upper()
def lower_case(txt):
    return txt.lower()
def concatenate(txt):
    txt2= input('Introduce another text : ')
    return txt + txt2

print('Introduce a text: ')
txt = input()
option = menu()
if(option == 1):
    print( upper_case(txt) )
elif(option == 2):
    print( lower_case(txt) )
elif(option == 3):
    print( concatenate(txt) )
else:
    print('BYE BYE')
print('end program')

print("-------------------")
#Example methods return

def menu_number():
    print('Choose an option: ')
    print('1.- SUM')
    print('2.- REST')
    print('3.- MULTIPLICATION')
    print('INTRODUCE -1 FOR ENDS PROGRAM')
    option = int(input())
    return option

def op_sume(num1,num2):
    return num1 + num2

def op_rest(num1, num2):
    return num1 - num2

def op_mult(num1, num2):
    return num1 * num2

option=0
while( option!=-1 ):
    option = menu_number()
    if( 1<=option <=3):
        print('Introduce 2 numbers:')
        num1 = int(input('Introduce number 1: '))
        num2 = int(input('introduce a number 2: '))
        if(option == 1):
            print('THE SUM: ', op_sume(num1,num2) )
        elif(option == 2):
            print('THE REST: ', op_rest(num1,num2) )
        elif(option == 3):
            print('THE MULTIPLICATION: ', op_mult(num1,num2) )
        else:
            print('BYE BYE')
        print("-------------------")
print('ENDS PROGRAM')