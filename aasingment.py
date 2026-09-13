minutes = int(input("enter the minutes:"))
hours = minutes/60
remaining_minutes = minutes%60
seconds = minutes*60
print(hours)
print(remaining_minutes)
print(seconds)

base = int(input("Enter the base:"))
exponent = int(input("Enter the exponent:"))
power = base**exponent
print(power)

n1 = int(input("Enter the first value:"))
n2 =int(input("Enter the second value:"))
n3= int(input("Enter the third value:"))
total = n1+n2+n3
avg = total/3
print(avg)

a= int(input("Enter the first value:"))
b=int(input("Enter the second value:"))
c = a>b
print(c)

a= int(input("Enter the first value:"))
b=int(input("Enter the second value:"))
c = a==b
print(c)

name = input("Enter name:")
age = int(input("Enter age:"))
height = float(input("Enter height:"))
print(name)
print(age)
print(height)

name = input("Enter name:")
print(F"Hello,{name}")

a= int(input("Enter the first value:"))
b=int(input("Enter the second value:"))
total = a+b
print(total)

n = float(input("Enter the value:"))
print(n)
new = int(n)
print(new)

a= int(input("Enter the first value:"))
b=int(input("Enter the second value:"))
print(a+b)

length = float(input("Enter the length of the rectangle:"))
breadth = float(input("Enter the breadth of the rectangle:"))
area = length*breadth
print(area)

a= int(input("Enter the first value:"))
b=int(input("Enter the second value:"))
q = a/b
r = a%b
print(q)
print(r)

a= int(input("Enter the first value:"))
b=int(input("Enter the second value:"))
print(a>0 and b>0)

a= int(input("Enter the first value:"))
b=int(input("Enter the second value:"))
print(a%2==0 or b%2==0)

num = int(input("Enter the value:"))
print(not(num>0))

a = int(input("Enter the value:"))
a = a+5 
a = a*2
a = a-3
print(a)

a= int(input("Enter the first value:"))
b=int(input("Enter the second value:"))
temp = a
a = b
b = temp
print(a)
print(b)

a= int(input("Enter the first value:"))
b=int(input("Enter the second value:"))
a,b = b,a
print(a)
print(b)

principle = float(input("Enter loan amount:"))
rate = float(input("Enter rate of interest:"))
time = float(input("Enter repayment time:"))
si = (principle*rate*time)/100
print(si)

c = float(input("Enter the temperature in celsius:"))
f = (c*9/5)+32
print(f)

n = int(input("Enter the value"))
print(n%3==0 and n%5==0)

num = int(input("Enter the value:"))
tens = num//10
units = num%10
total = tens=units
print(total)