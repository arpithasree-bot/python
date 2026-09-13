#list in python
#list is an ordered and changeable collection that can store
marks = [80, 90, 75, 85]
print(marks)

#accessing elements in a list 
marks = [80, 90, 75, 85]
print(marks[0])
print(marks[1])
print(marks[3])

#change elemens in a list
marks = [80, 90, 75]
marks[1] = 95
print(marks)

marks = [92,86,79,42,69,56]
marks[1]=89
marks[3]=97
marks[5]=67
print(marks)

#add elements to a list
#append is used to add the value at the end of the list
marks = [80,90,75]
marks.append(85)
print(marks)

#remove element from the  list
#remove is used to add the value at the end of the list
marks = [80,90,75]
marks.remove(90)
print(marks)

#adding element to a list 
#to add the element in a particular position we use insert
numbers = [10,20,30]
numbers.insert(1,15)
numbers.insert(3,25)
numbers.insert(6,40)
print(numbers)

#extent method (to combine the elements)
a= [1,2,3]
b= [4,5,6]
a.extend(b)
print(a)

#clear method (to clear the elements)
numbers = [10,20,30]
numbers.clear()
print(numbers)

#index method (to print the index value in the output)
numbers = [10,20,30,40]
print(numbers.index(30))
print(numbers.index(40))

#count method 
#to count the number of time the element is present in the index 
numbers = [10,20,30,20,20]
print(numbers.count(20))

#sort method
#to arrange the nums in order
numbers = [40,20,10,30]
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)

a=[1,2,3]
b=a.copy()
print(b)

#slicing method (start,stop,step)
numbers = [10,20,30,40,50]
print(numbers[1:4])
print(numbers[:3])
print(numbers[2:])
print(numbers[::-1])
print(numbers[::-4])
print(numbers[::-2])
print(numbers[::-3])

numbers = [10,20,30,40,50,60,70,80]
print(numbers[::-3])
print(numbers[::-2])
print(numbers[::-4])

#tuple in python
#tuple is an ordered and unchangeable collection that can store
student = ("John", 20, "Male")
print(student[0])
print(student[2])

#accessing elements in a tuple
student = ("rose", 22, 85.5)

print(student[0])
print(student[1])
print(student[2])

#tuples are immutable, so you cannot change their elements after creation
numbers = (10,20,20,30,20)
print(numbers.count(20))

#index method in tuple
numbers = (10,20,30,40)
print(numbers.index(30))

numbers=(10,20,30,40)
print(len(numbers))
print(max(numbers))
print(min(numbers))
print(sum(numbers))

#sets in python
#set is a collection of unique values that is unordered and mutable
#in sets curly braces is mandatory
numbers = {10,20,30,20,10}
print(numbers)

#why use sets?

#suppose students have selected subjects
subjects = {"python","java","python","SQL","jave"}

print(subjects)

#add values to a set
subjects = {"python","java"}
subjects.add("SQL")
print(subjects)

#remove values from a set
subjects = {"python","java","SQL",}
subjects.remove("java")
print(subjects)

#sets do not allow dupicate values
numbers = {1,2,2,3,3,4}
print(numbers)

#dictionaies in python
#Dictio