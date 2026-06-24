from class_month import Month

month_list = []
for i in range(3):
    month = Month()
    month.name = input(f"Enter the name of the month {i+1}: ")
    month.temp_max = float(input(f"Enter the maximum temperature for {month.name}: "))
    month.temp_min = float(input(f"Enter the minimum temperature for {month.name}: "))
    month_list.append(month)
#Remember the names of the months.
for data in month_list:
     print(f"\n- The maximun temperature in {data.name} is {data.temp_max} degrees Celsius.")
     print(f"- The minimun temperature in {data.name} is {data.temp_min} degrees Celsius.")
     print(f"- The average temperature in {data.name} is {data.get_average()} degrees Celsius.")
     print("\n ***************************************************************** ")