# Variable :A container for a value (String, Integer, Float, Boolean)
# A Variable behaves as if it was the value it contains.

# String :A sequence of characters enclosed in quotes.
first_name ="Krish"
favourite_game ="Cricket"
email_id ="Chauhnkrish898@gmail.com"
print(f"My name is {first_name}")
print(f"My favourite game is {favourite_game}")
print(f"My email id is {email_id}")


# Integer :A whole number without a decimal point.
age = 20
print(f"My age is {age}")

# Float :A number with a decimal point.
height = 9.4
weight = 67.5
print(f"My height is {height}")
print(f"My weight is {weight}")

# Boolean :A data type that can have one of two values: True or False.s
homework_is_done = True
you_like_pizza = True

if homework_is_done:
    print("Homework is done.")
else:
    print("Homework is not done.")

if you_like_pizza:
    print("You like pizza.")
else:
    print("You dont like pizza.")

    # Type castting :Convertting a value from one data type to another.

    # int() :Converts a value inton an integer.
    # float() :Converts a value into a flot.
    # str() :Converts a value into a string.
    # bool() :Converts a value into a boolean.

# while doing the type casting there are some variables which can be converted but there output seems to be same rather than there data type is changed.
# for example: 
age="20"
age = int(age)
print(age)
print(type(age))
# *Here they are in the out they seem to ba the same numbers but there types are different*
# to check the type of the variable we have to use the type() function.

# Tpyes of explicit type casting in which we convert the variable to another type variable by using ext.

# Integer to Float
age = 82
print(float(age))

# Float to Integer
height = 9.3
height = int(height)
print(height)

# String to Integer
age = "20"
age = int(age)
print(age)

# Integer to String
age = 20
age =(str(age))
print(age)

# Float to String
gpa = 5.6
gpa =(str(gpa))
print(gpa)

# String to Float
my_bdy_count = 4.5
my_bdy_count = (float(my_bdy_count))
print(my_bdy_count)

# String to boolean 
name = "jiya"
name = bool(name)
print(name)

# Integer to boolean
Marks = 90
Marks = bool(Marks)
print(Marks)

# float to boolean 
gpa = 5.7 
gpa = bool(gpa)
print (gpa)

# boolean to string 
homework_is_done = True 
homework_is_done = str(homework_is_done)
print(homework_is_done)

# boolean to integer 
i_love=False
i_love=int(i_love)
print(i_love)

# boolean to float 
you_like_pizza = False
you_like_pizza = float(you_like_pizza)
print(you_like_pizza)

# Implicit type casting in this type we convert avariable into another type variable without using any function or method.
# For example: 
x = 78
y = 9.8
print(x/y)
print(type(x/y))
# In this example if you notice we print x while x is a integer  and y is a float type but in output x/y is a float so, this is the type of implicit type casting.

# User Input: By using the input function we can give the user acsses.

x=int(input ("enter the number:"))
y=int(input("enter the number:"))

print (x/y)

# Mad lib Activity
adjective = input("enter the adjective:")

print(f"Today,when i saw my bus i was {adjective} because the school transport management changed your bus and get a new one for your convience" )
       
# Shopping cart Activity.

Items=input("enter the item:")
quantity=int(input("enter the quantity:"))
price=float(input("enter the price:"))
print(f"You have purchased {quantity} No. of {Items} ")
total= (quantity) * (price)
print(f"Your total is ${total}")

# Arthimetic operator [+(Addition),-(Subtraction),*(mutliplication),/(division),**(Exponent or Power),%(Modules)]

# Addition

pizza = 7
pizza = pizza+4
print(pizza)

pizza = 7
pizza += 5 
print(pizza)
# Subtraction 

friends = 9
friends = friends-8
print(friends)

friends = 9
friends -= 9
print(friends)
# Multiplication 

a = type("enter the number:")
b = type("enter the number:")

a = int(a)
b = int(b)

print(a*b)
# Exponent

a= input("enter the number:")
b = input("enter the number:")

a=int(a)
b=int(b)

print(a**2+b**2)
# Modules

friends = 10
friends = friends % 3
print(friends)

friends = 20
friends %= 3
print(friends)

# Absolute:  This function is used to find the absolute vale of any digit.

a = -9
result = abs(a)
print(result)
# Max: This function is used to find any maximum number between a group of digit.
# Min: This function is used to find any minimum number between a group of digit. 

x =34
y =56
z =74 
result = max(x,y,z)
print(result) 

result = min(x,y,z)
print(result)
# Round: This function is used to round any exponential number.

x = 342.56689876543
result = round(x)

print(result)

# Ceil: This function is used to round a number upward to the nearest integer.
math.ceil (3.4)
# floor: This function is used to round a number downward to the nearest integer.
math.floor (5.6)


# Import: This function is used to import any mathematical or physics unit to the program.
# # Square root: This function is used to square root any given number.
import math
print(math.pi)
print(math.e)

x= 46456
print(math.sqrt(x))

# Simple calculator activity using if and else functions.

operator = input("Select the following operators (+,-,*,/):")
x = float(input("enter the 1st no.:"))
y = float(input("enter the 2nd no.:"))

if operator == "+":
    print(x+y)
elif operator == "-":
    print(x-y)
elif operator == "*":
    print(x*y)
elif operator == "/":
    print(round(x/y ,2))
else:
    print(f"Invalid operator selected: {operator}. Please select a valid operator (+,-,*,/).")

# Usage of dictionary learned in img xp classes .

dict1={"name":"krish","age":18,"city":"sonipat"}
print (dict1)
print (dict1.keys())
print (dict1.values())
print (dict1.items())
print (type(dict1))
print (len(dict1))
print("city:", dict1.pop("city"))
print("age:",dict1.pop("age"))

# Conversion of temperature from Celsius to Fahrenheit and vice versa.

Unit = input("Enter the unit C/F:")
temp = float(input("Enter the temperature:"))
if Unit == "C":
    result = round((temp * 9/5) + 32, 2)  
    print (f"Temperature in Fahrenheit is equal to {result}°F")
elif Unit =="F":
    result = round((temp - 32) * 5/9, 2)
    print (f"Temperature in Celsius is equal to {result}°C")
else :
    print("Invalid unit. Please enter C or F.")

# Various methods of strings.

# len(): This function is used to count the number of characters in a string.

name1 = input("Enter the username: ")
result1 = len(name1)
print(result1)
# Note: len() counts all characters, including spaces.

# find(): This function is used to find the position of the first occurrence of a character, word, or substring.

name2 = input("Enter the username: ")
result2 = name2.find(input("Enter the word to find at first place: "))
print(result2)
# Note: find() returns -1 if the specified character, word, or substring is not found in the string.

# rfind(): This function works like find(), but it returns the position of the last occurrence.

name3 = input("Enter the username: ")
result3 = name3.rfind(input("Enter the word to find at the last place: "))
print(result3)
# Note: rfind() returns -1 if the specified character, word, or substring is not found in the string.

# capitalize(): This function is used to make the first character uppercase.

name4 = input("Enter the username: ")
result4 = name4.capitalize()
print(result4)

# upper(): This function is used to convert the entire string to uppercase.

name5 = input("Enter the username: ")
result5 = name5.upper()
print(result5)

# lower(): This function is used to convert the entire string to lowercase.
name6 = input("Enter the username: ")
result6 = name6.lower()
print(result6)

# isdigit(): This function checks whether the string contains only digits. It returns True or False.

name7 = input("Enter the username: ")
result7 = name7.isdigit()
print(result7)
# Note: It returns True only if the string contains only numbers.

# isalpha(): This function checks whether the string contains only letters. It returns True or False.

name8 = input("Enter the username: ")
result8 = name8.isalpha()
print(result8)

# count(): This function is used to count the number of times a specific character, word, or substring appears in a string.

phone_number = input("Enter your phone number: ")
result9 = phone_number.count(input("Enter the number you want to count: "))
print(result9)

# replace(): This function is used to replace a character, word, or substring with another one.

name0 = input("Enter the username: ")
result0 = name0.replace(input("Enter the word you want to replace: "), input("Enter the word you want to add in place of the replaced one: "))
print(result0)


# A loop is a programming structure that repeats a block of code
# As long as a condition remains true.
# The while loop keeps running until the condition becomes false.

name = input("Enter your name :" )

while  name=="" :
    print ("Invalid name entered")
    name = input("Enter your name :")

else:
    # The else block runs when the while condition is finally false.
    print (f"Your name is {name}")


food = (input("Enter your fav food(Enter Q to exit ) :" ))

while not food=="Q":
    print (f"Your fav food is {food}")
    food = (input("Enter your fav food(Enter Q to exit ) :" ))  

else:
    print ("THANK YOU FOR ORDERING")

age = int(input("Enter your age :" ))

while  age < 0 or age >= 80 :

    print ("Invalid age entered")
    age = int(input("Enter your age :"))

else:
   
    print (f"Your age is {age}")

    
# For loops:
# A for loop is used to iterate over a sequence such as a list, tuple,
# string, or range. It repeats a block of code once for each item.

design = input ("Enter the design you want to print: ")

for i in range (1,10):
    print(design)


# Nested loops: Nested loops are nothing just a loop inside a loop. The inner loop will be executed one time for each iteration of the outer loop.


row = int(input("Enter the number of rows: "))
column = int(input("Enter the number of columns: "))
symbol = input("Enter the symbol to use: ")

for rows in range(row , 0 ,-1):
    for columns in range(1, rows+1):
        print(symbol, end="")
    print()  



    # ============================================================
# PROJECT: Mini ATM / Bank Account Manager
# Uses: variables, type casting, input, f-strings, if/elif/else,
#       while loops, for loops, dictionary, string methods, math
# ============================================================
 
import math
 
print("=" * 32)
print("      WELCOME TO PYBANK ATM")
print("=" * 32)
 
# ---------- 1. Create the account (dictionary) ----------
account = {"name": "", "pin": "", "balance": 0.0, "deposits": 0, "withdrawals": 0}
 
name = input("Enter your name: ")
# isalpha() only works without spaces, so we remove spaces just for the check
while name == "" or not name.replace(" ", "").isalpha():
    print("Invalid name. Please use letters only.")
    name = input("Enter your name: ")
account["name"] = name.title()   # "krish chauhan" -> "Krish Chauhan"
 
pin = input("Create a 4-digit PIN: ")
while not (pin.isdigit() and len(pin) == 4):
    print("PIN must be exactly 4 digits.")
    pin = input("Create a 4-digit PIN: ")
account["pin"] = pin
 
print(f"\nAccount created for {account['name']}!\n")
 
# ---------- 2. Login (3 attempts) ----------
attempts = 3
logged_in = False
 
while attempts > 0 and not logged_in:
    entered_pin = input("Enter your PIN to login: ")
    if entered_pin == account["pin"]:
        logged_in = True
    else:
        attempts -= 1
        print(f"Wrong PIN. {attempts} attempt(s) left.")
 
# ---------- 3. Main menu ----------
if logged_in:
    print(f"\nLogin successful. Hello, {account['name']}!")
    choice = ""
 
    while choice != "6":
        print("\n----------- MENU -----------")
        print("1. Check balance")
        print("2. Deposit money")
        print("3. Withdraw money")
        print("4. Interest projection")
        print("5. Account summary")
        print("6. Exit")
        choice = input("Choose an option (1-6): ")
 
        if choice == "1":
            print(f"Your balance is ${round(account['balance'], 2)}")
 
        elif choice == "2":
            amount = float(input("Enter deposit amount: $"))
            if amount > 0:
                account["balance"] += amount
                account["deposits"] += 1
                print(f"${amount} deposited successfully.")
            else:
                print("Deposit must be greater than 0.")
 
        elif choice == "3":
            amount = float(input("Enter withdrawal amount: $"))
            if amount <= 0:
                print("Withdrawal must be greater than 0.")
            elif amount > account["balance"]:
                print("Insufficient balance!")
            else:
                account["balance"] -= amount
                account["withdrawals"] += 1
                print(f"${amount} withdrawn successfully.")
 
        elif choice == "4":
            rate = float(input("Enter yearly interest rate (%): "))
            years = int(input("Project for how many years? "))
            print(f"\n{'Year':<6}{'Balance'}")
            for year in range(1, years + 1):
                future = account["balance"] * (1 + rate / 100) ** year
                print(f"{year:<6}${round(future, 2)}")
 
        elif choice == "5":
            print("\n====== ACCOUNT SUMMARY ======")
            for key, value in account.items():
                if key != "pin":              # never show the PIN
                    print(f"{key.capitalize():<12}: {value}")
 
            # Nested loop: a triangle showing number of deposits
            print("\nDeposit activity:")
            for rows in range(1, account["deposits"] + 1):
                for columns in range(1, rows + 1):
                    print("$", end="")
                print()
 
        elif choice == "6":
            print(f"\nThank you for banking with us, {account['name']}!")
            print(f"Final balance (rounded up): ${math.ceil(account['balance'])}")
 
        else:
            print(f"Invalid option: {choice}. Please choose 1-6.")
 
else:
    print("\nToo many wrong attempts. Card blocked!")







