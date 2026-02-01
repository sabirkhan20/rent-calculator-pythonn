# for i in range (10,1,-1):
# for loppp
#     print(i)

#     if i%2==0:
#         print(i,"even")
#     else:
#         print(i,"odd")

# for i in range(3):        # outer loop
#     for j in range(3):    # inner loop
#         print("Hi")

# for i in range(1, 4):
#     for j in range(1, 4):
#         print(i, j)


# colors=["red ",'pink','blue','green']

# for color in colors:
#    print(color)

#    for i in color:
#       print(i,end='')



# for i in range(10):
#     if i == 5:
#         break
#     print(i)




# for i in range(5):
#     if i == 2:
#         continue
#     print(i)

# table logic loop
# for i in range (1,11):
#     print('2 X',i,'=',2*i)

# a = int(input("ENTER THE NUMBER: "))

# for i in range(1, 11):
#     print(a, "X", i, "=", a * i)


# a=int(input("ENTER THE NUMBER:"))
# for i in range(1,11):
#     print(f'2 x',{i},'=',a*i)


# n = 5
# for i in range(1, n+1):
#     for j in range(n - i):   # spaces
#         print(" ", end="")
#     for j in range(i):       # stars
#         print("*", end="")
#     print()

# name = "SABIR"
# for i in name:
#     print(i,end='')


# n = 4
# for i in range(n, 0):
#     for j in range(i):
#         print('*', end=' ')
#     print()

# for i in range(10,2,-1):
#     for j in range(i):
#         print('*',end='')
#     print()



# n = 4
# for i in range(1, n+1):
#     print(' ' * (n - i) + '* ' * i)




# while loop start from here


# a = 1
# while a <= 5:
#     print(a)



# a = 0

# while a <= 5:
#     print(a)
#     a += 1



# function start from here

# def welcome():
#     print("Welcome")

# welcome()

# def welcome(name):
#     print("Welcome", name)

# welcome("Sabir")


# def square(n):
#     print(n*n)

# square(5)


# def minus (a,b):
#     print(a-b)


# minus(10,20)



# def even_odd(n):
#     if n % 2 == 0:
#         print("Even")
#     else:
#         print("Odd")

# even_odd(7)


# def multiple_of_five(n):
#     if n%5==0:
#         print('multiply by 5 ')
#     else:
#         print('not multiply by 5')

# multiple_of_five(100101010)


# def multiple_of_5(n):
#     if n % 5 == 0:
#         return "Yes"
#     else:
#         return "No"

# )




# def modulas(n):
#     if n%2==0:
#         return 'yes its modulas function'
#     else:
#         return 'its not a modulas function'
    
# print(modulas(3))
# print(modulas(4))
# print(modulas(10))
# print(modulas(8))


# calculator using functions

# num1=int(input('ENTER A NUMBER1:'))
# num2=int(input('ENTER A NUMBER2:'))



# def sum(num1,num2):
#     return num1+num2
# def minus(num1,num2):
#     return num1-num2
# def divide(num1,num2):
#     return num1/num2
# def multiply(num1,num2):
#     return num1*num2


# print(sum(num1,num2))
# print(minus(num1,num2))
# print(divide(num1,num2))
# print(multiply(num1,num2))






# ===============================
# 1️⃣ LIST CREATE
# ===============================
# nums = [10, 20, 30, 40]
# print("Initial list:", nums)

# # ===============================
# # 2️⃣ PROPERTIES OF LIST
# # ===============================

# # Ordered (index based)
# print("First element:", nums[0])
# print("Last element:", nums[-1])

# # Mutable (changeable)
# nums[1] = 99
# print("After modification:", nums)

# # Duplicate allowed
# nums_dup = [1, 2, 2, 3]
# print("Duplicates allowed:", nums_dup)

# # Mixed data types
# mixed = [10, "Sabir", 3.14, True]
# print("Mixed data list:", mixed)

# # ===============================
# # 3️⃣ LENGTH
# # ===============================
# print("Length of nums:", len(nums))

# # ===============================
# # 4️⃣ ADD ELEMENTS
# # ===============================

# # append → last
# nums.append(50)
# print("After append:", nums)

# # insert → specific index
# nums.insert(1, 15)
# print("After insert:", nums)

# # extend → multiple values
# nums.extend([60, 70])
# print("After extend:", nums)

# # ===============================
# # 5️⃣ REMOVE ELEMENTS
# # ===============================

# # remove by value
# nums.remove(15)
# print("After remove:", nums)

# # pop by index
# nums.pop(0)
# print("After pop index 0:", nums)

# # pop last
# nums.pop()
# print("After pop last:", nums)

# # ===============================
# # 6️⃣ CHECK VALUE
# # ===============================
# if 30 in nums:
#     print("30 is present")

# # ===============================
# # 7️⃣ LOOP THROUGH LIST
# # ===============================
# print("Looping values:")
# for x in nums:
#     print(x)

# # index + value
# print("Index with values:")
# for i, v in enumerate(nums):
#     print(i, v)

# # ===============================
# # 8️⃣ SORT & REVERSE
# # ===============================
# nums.sort()
# print("Sorted:", nums)

# nums.sort(reverse=True)
# print("Sorted reverse:", nums)

# nums.reverse()
# print("Reversed:", nums)

# # ===============================
# # 9️⃣ SLICING
# # ===============================
# nums2 = [10, 20, 30, 40, 50]
# print("Slice 1:4 ->", nums2[1:4])
# print("Slice start ->", nums2[:3])
# print("Slice step ->", nums2[::2])

# # ===============================
# # 🔟 COPY LIST
# # ===============================
# a = [1, 2, 3]
# b = a.copy()
# b.append(4)
# print("Original list:", a)
# print("Copied list:", b)

# # ===============================
# # 1️⃣1️⃣ CLEAR LIST
# # ===============================
# temp = [5, 6, 7]
# temp.clear()
# print("Cleared list:", temp)

# # ===============================
# # 1️⃣2️⃣ LIST + FUNCTION (REAL USE)
# # ===============================
# def add_task(tasks, task):
#     tasks.append(task)

# tasks = []
# add_task(tasks, "Study Python")
# add_task(tasks, "Practice List")
# print("Tasks:", tasks)









# ================== TUPLE IN PYTHON (ALL IN ONE) ==================

# # 1️⃣ Tuple creation
# t = (10, 20, 30, 40, 50)
# print("Original tuple:", t)

# # 2️⃣ Length of tuple
# print("Length of tuple:", len(t))

# # 3️⃣ Indexing (0 se start hoti hai)
# print("First element:", t[0])
# print("Last element:", t[-1])

# # 4️⃣ Slicing
# print("Elements from index 1 to 3:", t[1:4])
# print("First three elements:", t[:3])
# print("Last two elements:", t[-2:])

# # 5️⃣ Looping through tuple
# print("Looping through tuple:")
# for i in t:
#     print(i)

# # 6️⃣ Tuple is immutable (change nahi hota)
# # t[0] = 100   ❌ ERROR aayega (tuple change nahi hota)

# # 7️⃣ Tuple with different data types
# mixed = (1, "Sabir", 3.14, True)
# print("Mixed tuple:", mixed)

# # 8️⃣ Single element tuple (comma zaroori hai)
# single = (10,)
# print("Single element tuple:", single)
# print("Type:", type(single))

# # 9️⃣ Tuple unpacking
# a, b, c, d, e = t
# print("Unpacked values:", a, b, c, d, e)

# # 🔟 count() method
# print("Count of 20:", t.count(20))

# # 1️⃣1️⃣ index() method
# print("Index of 30:", t.index(30))

# # 1️⃣2️⃣ Tuple inside tuple (nested tuple)
# nested = (1, 2, (3, 4, 5))
# print("Nested tuple:", nested)
# print("Access nested element:", nested[2][1])

# # 1️⃣3️⃣ Convert tuple to list (to modify)
# temp = list(t)
# temp.append(60)
# t_new = tuple(temp)
# print("Tuple after conversion & modification:", t_new)

# # 1️⃣4️⃣ Membership check
# print("Is 40 in tuple?", 40 in t)
# print("Is 100 in tuple?", 100 in t)

# # 1️⃣5️⃣ Tuple with range
# r = tuple(range(1, 6))
# print("Tuple from range:", r)

# # ================== END ==================



# num1=int(input('ENTER THE NUMBER 1:'))
# num2=int(input('ENTER THE NUMBER 2:'))

# def add(num1,num2):
#     return(num1+num2)
# # print(add(num1,num2))

# def sub(num1,num2):
#     return(num1-num2)
# # print(sub(num1,num2))

# def multiply(num1,num2):
#     return(num1*num2)
# # print(multiply(num1,num2))

# def divide(num1,num2):
#     return(num1/num2)
# # print(divide(num1,num2))
# # if num1==0:
# #     print('cant be divided ')
# # else:
# #     print('congratulations:')

# choice = input("Choose + - * / : ")

# if choice == "+":
#     print(add(num1, num2))
# elif choice == "-":
#     print(sub(num1, num2))
# elif choice == "*":
#     print(multiply(num1, num2))
# elif choice == "/":
#     print(divide(num1, num2))
# else:
#     print("Invalid choice")










# num1=int(input('ENTER A NUMBER:'))
# num2=int(input('ENTER A NUMBER 2:'))

# def add(num1,num2):
#     return(num1+num2)
# # print(add(num1,num2))

# def sub(num1,num2):
#     return(num1-num2)
# # print(sub(num2,num2))

# def multiply(num1,num2):
#     return(num1*num2)
# # print(multiply(num1,num2))

# def divide(num1,num2):
#     return(num1%num2)
# # print(divide(num1,num2))

# choices=input('enter the choice:*,%,-,+:')

# if choices=='+':
#     print(add(num1,num2))
# elif choices=='-':
#     print(sub(num1,num2))
# elif choices=='*':
#     print(multiply(num1,num2))
# elif choices=='%':
#     print(divide(num1,num2))
# else:
#     print('invalid choice try again later')







# dictionary start from herE



# my_team = {

#     'RCB': {
#         'NAME': 'ROYAL CHALLENGERS BANGALORE',
#         'FOUNDED IN': 2008,
#         'CAPTAIN':'virat kohli',
#         'OWNER NAME': 'VIJAY MALYA',
#         'BEST BOWLER': 'JOSH HAZELWOOD',
#         'WICKETS': 65,
#         'BEST BATSMAN': 'VIRAT KOHLI',
#         'VIRAT INNINGS': [12, 34, 56, 65, 100]
#     },

#     'MI': {
#         'NAME': 'MUMBAI INDIANS',
#         'CAPTAIN':'rohit sharma',
#         'FOUNDED IN': 2008,
#         'OWNER NAME': 'RELIANCE INDUSTRIES',
#         'BEST BOWLER': 'JASPRIT BUMRAH',
#         'WICKETS': 90,
#         'BEST BATSMAN': 'ROHIT SHARMA',
#         'ROHIT INNINGS': [10, 20, 87, 96, 34]
#     }
# }

# team_name = input("Enter team name (RCB / MI): ")
# team_name=input('enter team name as RCB/MI;')

# # if team_name in my_team:
# #     print("Team Name:", my_team[team_name]['NAME'])
# #     print("Founded In:", my_team[team_name]['FOUNDED IN'])
# #     print("Owner:", my_team[team_name]['OWNER NAME'])
# #     print("Best Batsman:", my_team[team_name]['BEST BATSMAN'])
# #     print("Best Bowler:", my_team[team_name]['BEST BOWLER'])
# #     print("Wickets:", my_team[team_name]['WICKETS'])
# # else:
# #     print("Team not found")


# if team_name in my_team:
#     my_team['CAPTAIN'] = 'YUVRAJ SINGH'
#     print("Captain updated successfully")
# else:
#     print("Team not found")

# if team_name in my_team:
#     my_team['CAPTAIN']='ms dhoni'
#     print('captain updated succesfully')
# print(my_team)



# if team_name in my_team:
#     my_team[team_name]['CAPTAIN'] = 'YUVRAJ SINGH'
#     print("Captain updated successfully")
# else:
#     print("Team not found")

# if team_name in my_team:
#     my_team[team_name]['CAPTAIN'] = 'MS DHONI'
#     print("Captain updated successfully")

# print(my_team)





# menu = {
#     "Espresso": 120,
#     "Cappuccino": 180,
#     "Latte": 200,
#     "Mocha": 220,
#     "Cold Coffee": 250
# }

# print(" Welcome to Starbucks ")
# print("-------- MENU --------")
# print("Espresso : ₹120")
# print("Cappuccino : ₹180")
# print("Latte : ₹200")
# print("Mocha : ₹220")
# print("Cold Coffee : ₹250")
# print("----------------------")

# choice = input("Enter coffee name: ")
# quantity = int(input("Enter quantity: "))

# if choice == "Espresso":
#     total = menu["Espresso"] * quantity
#     print(f"You ordered {quantity} Espresso")
#     print(f"Total Bill: ₹{total}")

# elif choice == "Cappuccino":
#     total = menu["Cappuccino"] * quantity
#     print(f"You ordered {quantity} Cappuccino")
#     print(f"Total Bill: ₹{total}")

# elif choice == "Latte":
#     total = menu["Latte"] * quantity
#     print(f"You ordered {quantity} Latte")
#     print(f"Total Bill: ₹{total}")

# elif choice == "Mocha":
#     total = menu["Mocha"] * quantity
#     print(f"You ordered {quantity} Mocha")
#     print(f"Total Bill: ₹{total}")

# elif choice == "Cold Coffee":
#     total = menu["Cold Coffee"] * quantity
#     print(f"You ordered {quantity} Cold Coffee")
#     print(f"Total Bill: ₹{total}")

# else:
#     print("Sorry, item not available")

# print("Thank you for visiting Starbucks ")


# num1=int(input('enter a number:'))
# num2=int(input('enter a number 2:'))

# choice=input('+,-,/,*:')

# if choice== '+':
#     print(num1+num2)
# elif choice=='-':
#     print(num1-num2)
# elif choice=='*':
#     print(num1*num2)
# elif choice=='/':
#     print(num1/num2)
# else:
#     print('invalid choice try again later:')


# balance=100000
# correct_pin=258099
# account_holder_name='SABIR KHAN'

# pin=int(input('enter your pin:'))

# if account_holder_name=='SABIR KHAN':
#     print('welcome sabir khan please procced next ')

# if pin==correct_pin:
#     print('1.check balance')
#     print('2.withdraw money')
#     print('3.Deposit money')
#     print('4.EXIT')

# choice=int(input('enter your choice from 1 to 4:'))

# if choice==1:
#     print('your current balance is',balance)
# elif choice==2:
#     amount=int(input('Enter amount to withdraw:'))
#     if amount <=balance:
#         balance=balance-amount
#         print('please collec your money thanks have a good day:')
#         print('remaining balance',balance)
#     else:
#         print('insufficient balance')
# elif choice==3:
#     amount=int(input('enter amount to deposit :'))
#     balance=balance+amount
#     print('Amount deposit successfully')
#     print('your current balance is',balance)
# elif choice==4:
#     print('thank you for using ATM')
# else:
#     print('invalid choice')


# balance = 100000
# correct_pin = 258099
# account_holder_name = "SABIR KHAN"

# name = input("Enter account holder name: ")
# pin = int(input("Enter your PIN: "))

# if name == account_holder_name and pin == correct_pin:
#     print("Welcome", account_holder_name)
#     print("1. Check Balance")
#     print("2. Withdraw Money")
#     print("3. Deposit Money")
#     print("4. Exit")

#     choice = int(input("Enter your choice (1–4): "))

#     if choice == 1:
#         print("Your current balance is:", balance)

#     elif choice == 2:
#         amount = int(input("Enter amount to withdraw: "))
#         if amount <= balance:
#             balance -= amount
#             print("Please collect your money")
#             print("Remaining balance:", balance)
#         else:
#             print("Insufficient balance")

#     elif choice == 3:
#         amount = int(input("Enter amount to deposit: "))
#         balance += amount
#         print("Amount deposited successfully")
#         print("Updated balance:", balance)

#     elif choice == 4:
#         print("Thank you for using ATM")

#     else:
#         print("Invalid choice")

# else:
#     print("❌ Invalid name or PIN. Access denied.")



# account_holder_name = 'shiva ji'
# available_balance = 100000

# pin = int(input('Enter your PIN: '))

# if pin == 258099:
#     print(f"\nWelcome {account_holder_name} to Singapore Bank")
#     print('1. Check available balance')
#     print('2. Deposit money')
#     print('3. Withdraw money')
#     print('4. Exit')

#     choice = int(input('Choose from 1,2,3,4: '))

#     if choice == 1:
#         print('Your available balance is:', available_balance)

#     elif choice == 2:
#         deposit_money = int(input('Enter money you want to deposit: '))
#         if deposit_money > 0:
#             available_balance += deposit_money
#             print('Deposit successful')
#             print('Updated balance:', available_balance)
#         else:
#             print('Invalid deposit amount')

#     elif choice == 3:
#         withdraw_money = int(input('Enter amount to withdraw: '))
#         if withdraw_money <= available_balance and withdraw_money > 0:
#             available_balance -= withdraw_money
#             print('Withdrawal successful')
#             print('Remaining balance:', available_balance)
#         else:
#             print('Insufficient balance or invalid amount')

#     elif choice == 4:
#         print('Thanks for visiting the bank. Have a nice day 😊')

#     else:
#         print('Invalid choice')

# else:
#     print('❌ Invalid PIN. Access denied.')






# projects start from here

# rent calculator

# rent=int(input('enter rent for each:'))
# food=int(input('enter the amount of food expenxses'))
# electricity_spend=int(input('enter your electricity bill:'))
# charge_per_unit=int(input('enter the number of elecrtricity bill unit:'))
# person=int(input('enter the amount in each person:'))


# electricity_bill=electricity_spend*charge_per_unit

# output=(rent+food+electricity_bill)/person
# print('amount to pay by one person',output)


# rent calculator

# import random

# choice=['rock','paper','sciessor']

# user_list=str(input('enter your choice:',))

# comp_choice=random.choice(user_list)
# print(comp_choice)




# import random

# choices = ['rock', 'paper', 'scissor']

# user_choice = input('Enter your choice (rock/paper/scissor): ').lower()

# comp_choice = random.choice(choices)

# print("User choice:", user_choice)
# print("Computer choice:", comp_choice)

# if user_choice not in choices:
#     print("Invalid choice")

# if comp_choice==user_choice:
#     print('match tie ')

# elif user_choice=='scissor'and comp_choice=='paper':
#     print('user win')
# elif user_choice=='rock'and comp_choice=='scissor':
#     print('user win')
# elif user_choice=='paper'and comp_choice=='rock':
#     print('user win')

# elif comp_choice=='scissor'and user_choice=='paper':
#     print('comp win')
# elif comp_choice=='rock'and user_choice=='scissor':
#     print('comp win')
# elif comp_choice=='paper'and user_choice=='rock':
#     print('comp win')


# ai_choice=random.choice(user_choice)
# print(ai_choice)

# print('your choice is',user_choice)
# print('ai choice is',ai_choice)


# if user_choice==ai_choice:
#     print('match tie')

# # if user_choice in ai_choice:
# #     print('continue playing')
# # else:
# #     print('invalid choice')

# if user_choice=='paper' and ai_choice=='rock':
#     print('user win')
# elif user_choice=='rock'and ai_choice=='scissor':
#     print('user win')
# elif user_choice=='scissor' and ai_choice=='rock':
#     print('user win')

# elif ai_choice=='rock' and user_choice=='scissor':
#     print('ai win')
# elif ai_choice=='paper'and user_choice=='rock':
#     print('ai win')
# elif ai_choice=='scissor' and user_choice=='paper':
#     print('ai win')

# else:
#     print('exit thanks for playing')


from datetime import date

# Taking input
birth_year = int(input("Enter birth year (YYYY): "))
birth_month = int(input("Enter birth month (MM): "))
birth_day = int(input("Enter birth day (DD): "))

birth_date = date(birth_year, birth_month, birth_day)
today = date.today()

# Calculate difference
years = today.year - birth_date.year
months = today.month - birth_date.month
days = today.day - birth_date.day

# Adjust days
if days < 0:
    months -= 1
    last_month = today.month - 1 or 12
    last_year = today.year if today.month != 1 else today.year - 1
    days += (date(last_year, last_month % 12 + 1, 1) - date(last_year, last_month, 1)).days

# Adjust months
if months < 0:
    years -= 1
    months += 12

print(f"Your age is: {years} years {months} months {days} days")


year=()