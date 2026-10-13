print("Hello,Welcome to Python Programming from scratch")
'''#variables
name="Vedanti"
age=19
print(name,age)
a=7
b=2
print(a+b,a-b,a*b)
# Input from an user 
name=input("Enter your name:")
age=input("enter your age:")
# input calculation 
a=int(input("Enter the value of a:"))
b=int(input("enter the value of b:"))
print(a+b,a-b,a*b)
#input message
z=int(input("message:"))
print(z)'''
#
#  Arithmetic Operators
#| Operator 
# `+` | Addition 
# `-` | Subtraction 
# `*` | Multiplication 
# `/` | Division 
# `//` | Floor division 
# `%` | Modulus/remainder 
# `**` | Power 
'''c=2
d=2
e=(c+d,c-d,c*d,c/d,c//d,c%d,c**d)
print(e)
#Comparison/relation operations
#| Operator | Meaning 
#`>` | Greater than |
# `<` | Less than |
# `==` | Equal to |
# `!=` | Not equal to |
# `>=` | Greater than or equal to |
# `<=` | Less than or equal to |
age=int(input("Enter your age:"))
print(age>=18)
#eg.2 marks
marks=int(input("Enter you Python Internal+External marks-"))
print(marks>=20)
#eg.3
a = 15
b = 10
print(a > b)
print(a < b)
print(a == b)
print(a != b)
print(a >= b)
print(a <= b)'''

#Statement Pass or fail, Eligible or not eligible, True or False,Positive or Negative
'''a=int(input("Enter your marks:"))
if a>=20:
  print("Pass")
else:
  print("Fail")

#if → first condition
#elif → another condition
#else → everything remaining

a=int(input("Enter your marks:"))
if a>20:
 print("Pass")
elif a==20:
 print("Katavar pass")
else:
  print("Fail")'''

#Logical operators
#`and` | Both conditions must be true | BOTH |
# `or` | At least one must be true | ANY ONE |
# `not` | Reverses True/False | REVERSE |
# and
'''marks=25
attendance=80
if marks>20 and attendance>75:
 print("Pass and Eligible")
elif marks==20 and attendance==75:
 print("Katyvar aaish")
else:
 print("Fail and Not Eligible")
#or 
choice = input("Do you want coffee or tea? ")
if choice == "coffee" or choice == "tea":
 print("Your order is accepted")
else:
 print("Please choose coffee or tea")
#Positive, Negative oe Zero
number = int(input("Enter a number: "))
if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")'''
# Assignment operators
# `=` | assignment |
#`+=` | `x = x + value` |
# `-=` | `x = x - value` |
# `*=` | `x = x * value` |
# `/=` | `x = x / value` |
# `%=` | `x = x % value` |
# `//=` | `x = x // value` |
# `**=` | `x = x ** value` |
'''number=2
number=21
print(number)
number+=22
print(number)
number-=23
print(number)
number*=24
print(number)
number/=25
print(number)
number//=48
print(number)
number%=50
print(number)
number**=60
print(number)'''
#Loops
#for loop
'''for i in range(5):
    print(i)
#Range with a step
for i in range(2, 11, 2):
    print(i)
#Range with a starting no.
for i in range(1, 6):
    print(i)
#Counting Backward
for i in range(5, 0, -1):
    print(i)
#Repeat smtg on loop
for i in range(5):
    print("Hello")
#eg
dna = "ATGCGT"
for base in dna:
    print(base)
#while loop
number = int(input("Enter a number: "))
i = 1
while i <= 10:
    print(number * i)
    i = i + 1
dna = "ATGCGTAC"
for base in dna:
    print(base)
# 1. FOR LOOP
for i in range(1, 6):
    print(i)


# 2. FOR LOOP WITH STEP
for i in range(2, 11, 2):
    print(i)


# 3. FOR LOOP BACKWARDS
for i in range(5, 0, -1):
    print(i)


# 4. FOR LOOP THROUGH A STRING
dna = "ATGCGT"

for base in dna:
    print(base)


# 5. FOR LOOP THROUGH A LIST
fruits = ["Apple", "Banana", "Mango"]

for fruit in fruits:
    print(fruit)


# 6. IF INSIDE FOR LOOP
for i in range(1, 11):

    if i % 2 == 0:
        print(i, "is Even")
    else:
        print(i, "is Odd")


# 7. FOR LOOP WITH BREAK
for i in range(1, 11):

    if i == 6:
        break

    print(i)


# 8. FOR LOOP WITH CONTINUE
for i in range(1, 11):

    if i == 5:
        continue

    print(i)


# 9. WHILE LOOP
i = 1

while i <= 5:
    print(i)
    i = i + 1


# 10. WHILE LOOP BACKWARDS
i = 5

while i >= 1:
    print(i)
    i = i - 1


# 11. WHILE LOOP WITH IF
i = 1

while i <= 10:

    if i % 2 == 0:
        print(i, "is Even")

    i = i + 1


# 12. WHILE LOOP WITH BREAK
i = 1

while i <= 10:

    print(i)

    if i == 5:
        break

    i = i + 1


# 13. WHILE LOOP WITH CONTINUE
i = 1

while i <= 10:

    if i == 5:
        i = i + 1
        continue

    print(i)
    i = i + 1


# 14. NESTED FOR LOOP
for i in range(1, 4):

    for j in range(1, 4):
        print(i, j)


# 15. MULTIPLICATION TABLE USING FOR LOOP
number = int(input("Enter a number: "))

for i in range(1, 11):
    print(number, "x", i, "=", number * i)


# 16. MULTIPLICATION TABLE USING WHILE LOOP
number = int(input("Enter another number: "))

i = 1

while i <= 10:
    print(number, "x", i, "=", number * i)
    i = i + 1


# 17. COUNT A IN DNA USING FOR LOOP
dna = "ATGCAAA"

count = 0

for base in dna:

    if base == "A":
        count = count + 1

print("Number of A =", count)


# 18. COUNT A IN DNA USING WHILE LOOP
dna = "ATGCAAA"

i = 0
count = 0

while i < len(dna):

    if dna[i] == "A":
        count = count + 1

    i = i + 1

print("Number of A =", count)



#List
#indexing
#append()
#insert()
#remove()
#len()
fruits = ["Apple", "Banana", "Mango"]

# 1. Print the list
print(fruits)

# 2. Access using index
print(fruits[0])

# 3. Access using negative index
print(fruits[-1])

# 4. Change an element
fruits[1] = "Orange"
print(fruits)

# 5. Find length
print(len(fruits))

# 6. Add at the end
fruits.append("Grapes")
print(fruits)

# 7. Add at a specific position
fruits.insert(1, "Pineapple")
print(fruits)

# 8. Remove by value
fruits.remove("Orange")
print(fruits)

# 9. Remove by index
fruits.pop(1)
print(fruits)

# 10. Sort
fruits.sort()
print(fruits)

# 11. Reverse
fruits.reverse()
print(fruits)

# 12. Extend with another list
more_fruits = ["Kiwi", "Papaya"]
fruits.extend(more_fruits)
print(fruits)

# 13. Print final length
print(len(fruits))

# 14. Print final list
print(fruits)

#Tuple
numbers = (10, 20, 30, 20, 40)

# Print tuple
print(numbers)

# Indexing
print(numbers[0])
print(numbers[-1])

# Slicing
print(numbers[1:4])

# Length
print(len(numbers))

# Count
print(numbers.count(20))

# Index
print(numbers.index(30))

# Loop
for number in numbers:
    print(number)

# Single element tuple
x = (5,)

print(x)
print(type(x))

#sets
numbers = {10, 20, 30, 20, 40, 10}

# Print set
print(numbers)

# Add
numbers.add(50)
print(numbers)

# Remove
numbers.remove(20)
print(numbers)

# Loop
for number in numbers:
    print(number)

# Two sets
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Union
print(A | B)

# Intersection
print(A & B)

# Difference
print(A - B)

# Reverse difference
print(B - A)

# Empty set
empty_set = set()
print(empty_set)
print(type(empty_set))

#DICTIONARIES
student = {
    "name": "Vedanti",
    "age": 19,
    "marks": 85
}

# Print dictionary
print(student)

# Access values
print(student["name"])
print(student["marks"])

# Add new value
student["city"] = "Pune"
print(student)

# Change value
student["marks"] = 90
print(student)

# Keys
print(student.keys())

# Values
print(student.values())

# Items
print(student.items())

# Get
print(student.get("name"))

# Update
student.update({"course": "Biotechnology"})
print(student)

# Remove
student.pop("age")
print(student)

# Loop through keys
for key in student:
    print(key)

# Loop through key-value pairs
for key, value in student.items():
    print(key, ":", value)'''

#Practice set

'''name=input("Enter your Name:")
age=int(input("Enter your Age:"))
marks=float(input("Enter your Marks:"))
print(name,age,marks)

#2
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
total = num1 + num2
print("Sum",total)
print("Data type:",type(total))'''

#3
'''a=10
b=3
c=(a+b,a-b,a*b,a/b,a//b,a**b,a%b,)
print(c)

#4
age=int(input("Enter your age:"))
marks=int(input("Enter your marks:"))
if age>=18 and marks>=40:
    print("Eligible")
else:
    print("Not Eligible")'''

#5
'''number=int(input("Enter the number you want:"))
if number>0:
   print("Positive")
elif number<0:
   print("Negative")
else:
   print("Zero")

#6 even odd
number=int(input("Enter the number you want:"))
if number%2==0:
   print("Even")
else:
   print("Odd")
#7
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if num1 > num2:
    print("Greater number:", num1)
elif num2 > num1:
    print("Greater number:", num2)
else:
    print("Both are equal")'''

#8Take input from the user and convert it to a float
marks = float(input("Enter the student's marks: "))
# Determine the grade using if-elif-else
if marks >= 75 and marks <= 100:
    grade = "A"
elif marks >= 60 and marks < 75:
    grade = "B"
elif marks >= 40 and marks < 60:
    grade = "C"
elif marks >= 0 and marks < 40:
    grade = "F"
else:
    grade = None

# Display the result
if grade is not None:
    print(f"Grade: {grade}")
else:
    print("Invalid marks entered. Please enter a score between 0 and 100.")