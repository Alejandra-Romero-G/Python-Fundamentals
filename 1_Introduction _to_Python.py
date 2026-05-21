print("**************Python*****************")
#variables
name = "Ale"
number = 6
print("Her name is "+ name) # this will print: Her name is Ale
print("Her favorite number is "+ str(number))# Her favorite number is 6

print("*******************************")
#mathemayhical operators:
#sume -> +
#rest -> -
#Division -> /
#multiplication-> *

# We have 3 thypes to Errors in any code
#1) Compilation Errors
#2) Execution Errors
#3) Logic Errors

# Convert between types
# str() - int() - float()

print("My first python")
name = "Paco"
number = 14
number2 = 6
sume = number + number2 #20
rest = number - number2 #8
division = number / number2 #2.333...
multi = number * number2 #84
print(str(sume) +"\n"+ str(rest)+"\n"+ str(division)+"\n"+ str(multi))
print("His name is "+name) #His name is Paco
print("His number is",number) #His number is 14

print("*******************************")
Print("********* SUME *********")
#Ask about information from user
print("Give me a number:  ")
number1=input() #2
print("Give me another number: ")
number2=input() #3
sume = int(number1) + int(number2)
print("The sume is: " + str(sume)) #The sume is: 5

print("*******************************")

#Conditional Operators
# > Greather
# >= Greather or equeal to
# < Less
# <= Less or equeals
# == Equeal
# != Different

#Conditionals (if)-(elif)-(else)
Print("********* LEGAL AGE *********")
print("Example about Conditional")
age=8
if( 18 <= age <= 100 ):
    print("He is legal age")
elif(age <= 18):
    print("He is minor")
else:
    print("He is very old")