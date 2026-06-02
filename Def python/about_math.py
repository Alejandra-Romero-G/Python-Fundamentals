
def positive_negative_zero(number):
    if (number >0):
        return "Positive"
    elif(number < 0):
        return "negative"
    else:
        return "Zero"
    
def grether_number(number1, number2):
    if (number1 > number2):
        return str(number1)
    elif(number1==number2):
        return "equeals"
    else:
        return str(number2)
    
def dni_letter(dni_num):
    letter = "TRWAGMYFPDXBNJZSQVHLCKET"
    return letter[dni_num % 23]

def day_of_birth(d,m,y):
    day = ["Saturday", "Sunday","Monday","Tuesday","Wednesday","Thursday","Friday"]
    if ( 1 == m == 2):
        m = 12 + m
        y -= 1
    o1 = (( 6 + 1 ) * 3) // 5
    o2 = (y // 4 )
    o3 = (y // 100 )
    o4 = (y // 400 )
    o5 = (d + (m * 2) + y + o1 + o2 - o3  + o4 + 2)
    o6 = (o5 // 7)
    o7 = (o5 -(o6 * 7))
    return  day [o7]

def greather_lesser_middle(number1,number2,number3):
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
    middle = (number1 + number2 + number3)-(greather + lesser)

    return f'"Lesser: "{lesser}" Middle:" {middle}" Greather:" {greather}'

def Collatz(number):
    while(number != 1):
        print(number)
        if(number % 2 == 0):
            number= number // 2
        else:
            number= (number * 3 ) + 1
    print(number)

def multiplication_table( num ):
    for i in range (1, 10+1):
        print(f" {num} * {i} = { num * i }")


def mail_validation(mail):
    if ( mail.find('@') == -1 or mail.find('@') != mail.rfind('@') ):
        validation=False
    elif ( mail.find('.') == -1 or mail.find('.') != mail.rfind('.')):
        validation=False
    elif ( mail.startswith("@") or mail.endswith("@") ):
        validation=False
    elif ( mail.endswith('.com') == False and mail.endswith('.es') ==False and mail.endswith('.org') ==False ):
        validation=False
    else:
        validation = True
    return validation

def isbn_validation(isbn):
    isbn = str(isbn)
    if (len(isbn) != 10 or not isbn.isdigit() ):
        return False
    num = 0
    for i in range(10):
        num += (i+1) * int(isbn[i])
    return (num % 11 == 0)

def validate_dni_number(dni):
    validation = False
    remainder = dni % 23

    if (remainder == 0):
        validation = True

    return validation

def counter_number():
    number = 0
    total_sum = 0
    even_sum = 0
    odd_sum = 0

    num_list = []
    even_list = []
    odd_list = []

    while(number != -1):
        number = int(input("Introduce a number: "))

        total_sum += number
        num_list.append(number)

        if number % 2 == 0:
            even_list.append(number)
            even_sum += number
        else:
            odd_list.append(number)
            odd_sum += number

    print(f"""
    Numbers: {num_list}
    Sum: {total_sum}

    Even numbers: {even_list}
    Even sum: {even_sum}

    Odd numbers: {odd_list}
    Odd sum: {odd_sum}
    """)

def counter_number():
    numbers = [int(input("Enter a number: ")) for _ in range(5)]

    even_numbers = [n for n in numbers if n % 2 == 0]
    odd_numbers = [n for n in numbers if n % 2 != 0]

    print(f"""
Numbers: {numbers}
Total sum: {sum(numbers)}

Even numbers: {even_numbers}
Even sum: {sum(even_numbers)}

Odd numbers: {odd_numbers}
Odd sum: {sum(odd_numbers)}
""")

