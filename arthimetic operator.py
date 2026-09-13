#comparison operators
a=10
b=20
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a<=b)
print(a>=b)

#age eligibility check
age=int(input("Enter your age:"))
print("Eligible :",age>=18)

#pass  or fail checker
marks=int(input("Enter your marks:"))
print("Passed :",marks>=40)

#login validation
correct_username="admin"
correct_password="admin123"
username=input("Enter your username:")
password=input("Enter your password:")
print(username==correct_username)
print(password==correct_password)

#logical operator
age=25
citizen=True
print(age >= 18 and citizen == True)

has_card=False
has_cash=True
print(has_card or has_cash)

is_logged_in=True
print(not is_logged_in)

#atm eligibility check
balance=10000
withdraw=5000
print(withdraw > 0 and withdraw <= balance)

#studdent scholarship eligibility check
marks=float(input("Enter your marks:"))
attendance=float(input("Enter your attendance:"))
eligible=marks>=85 and attendance>=75
print("Scholarship Eligible:",eligible)

#identity operator
a = None
print(a is None)
print(a is not None)

#Bitwise operator
a=5
b=3
print(a & b)
print(a | b)
print(a ^ b)
print(a << b)
print(a >> b)
print(~a)

#electric city bill calculation
units = int(input("Enter electricity units:"))
rate = 6
bill = units * rate 
print("Electricity bill:", bill)

#travel expense calculator
travel = float(input("travel expense:"))
food = float(input("food expense:"))
hotel = float(input("hotel expense:"))
total = travel + food + hotel
print("total expense;",total)
