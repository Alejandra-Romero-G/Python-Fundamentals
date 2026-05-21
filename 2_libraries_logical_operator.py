print("*******************************")
#Libraries in Python
# Two types of Python libraries
# 1) Built-in Python libraries
# 2) External Python libraries
import math
result = 7 / 3
print("Floor:", math.floor(result))
print("Ceil:", math.ceil(result))
print("---------------------------------")
from math import floor, ceil
print("Floor:", floor(result))
print("Ceil:", ceil(result))

print("*******************************")
# Logical Operators (and,or)
print("Greather / Lesser / middle \n")
print("Enter first number: ")
number1 = int(input())
print("Enter second number: ")
number2 = int(input())
print("Enter third number: ")
number3 = int(input())
greather = 0
lesser = 0
middle = 0
if(number1 > number2 and number1 > number3):
    greather = number1
elif(number2 > number1 and number2 > number3):
    greather = number2
else:
    greather = number3
if(number1 < number2 and number1 < number3):
    lesser = number1
elif(number2 < number1 and number2 < number3):
    lesser = number2
else:
    lesser = number3
middle = ()(greather - lesser)

print("Lesser:",lesser," Middle:",middle," Greather:",greather)
print("*******************************")