#january and month2 are instances (objects) of the Month class. 
# Each object has its own values for name, temp_max, and temp_min, 
# but both can use the same get_average() method defined in the class. 
# This demonstrates the principle of code reuse in object-oriented programming.
from class_month import Month
january = Month()
january.name = "January"
january.temp_max = 10
january.temp_min = -2

print(f"The average temperature in {january.name} is {january.get_average()} degrees Celsius.")

month2 = Month()
month2.name = "February"
month2.temp_max = 12
month2.temp_min = 4
print(f"The average temperature in {month2.name} is {month2.get_average()} degrees Celsius.")
print("end program")