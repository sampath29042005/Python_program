"""
DATA TYPES
WHAT ARE DATA TYPES IN PYTHON?
A DATA TYPES DEFINES:
     - WHAT KIND OF VALUE IS STORED
     - HOW THE MEMORY IS ALLOCATED
     - WHETHER THE VALUE CAN BE MODIFIED OR NOT
     - HOW PYTHON INTERNALLY MANAGES THE DATA
PYTHON AUTOMATICALLY IDENTIFIES THE DATATYPES WHEN WE ASSSIGN A VALUE TO A VARIABLE.
EXAMPLE:
x=10
name="John"
price=10.5

TYPES OF DATA TYPES IN PYTHON:
1. NUMERIC DATA TYPES
   - INTEGER [INT] [EXAMPLE: 1, 2, 3]
   - FLOAT [FLOAT] [EXAMPLE: 1.5, 2.7]
   - COMPLEX [COMPLEX] [EXAMPLE: 1+2j]

2. SEQUENCE DATA TYPES
   - STRING [STR] [EXAMPLE: "Hello", 'World']
   - LIST [LIST] [EXAMPLE: [1, 2, 3], ['a', 'b', 'c']]
   - TUPLE [TUPLE] [EXAMPLE: (1, 2, 3), ('x', 'y', 'z')]
   
   
- SET [SET] [EXAMPLE: {1, 2, 3}, {'a', 'b', 'c'}]
- DICTIONARY [DICT] [EXAMPLE: {'key1': 'value1', 'key2': 'value2'}]
- BOOLEAN [BOOL] [EXAMPLE: 0, 1, True, False]
- NONE [NONE] [EXAMPLE: NULL]
    """
'''
a = "Hello"
print(type(a))

# numeric data types
#int
x = 10
print(type(x))

#float
y = 10.5
print(type(y))

#complex
z = 1 + 2j
print(type(z))

# sequence data type
# string
s= "55"
print(type(s))
# list
l= [1,2,3]
print(type(l))

# tuple
t=(1,2,3)
print(type(t))

# set
b = {1,2,3}
print(type(b))

# dict
c= {"age":21}
print(type(c))
'''

# q1
age = int(input())
print(type(age))
print(age)

#q2
height = float(input())
print(type(height))
print(height)

#q3
a = 10
b = 5
print (a+b)
print (a-b)
print (a*b)
print (a/b)
print (a%b)

#q4

monthly_salary = float(input())
annual_salary = monthly_salary*12
print(type(monthly_salary))
print(monthly_salary)
print(annual_salary)


#q5
d=int(input())
e=float(input())
f=complex(input())
print(type(d))
print(type(e))
print(type(f))

#q6
movie_name=input()
print(movie_name)
print(len(movie_name))
print(type(movie_name))

#q7
fruit = list(input())
print(fruit)
print(type(fruit))
print(len(fruit))

#q8
city = tuple(input())
print(city)
print(len(city))
print(type(city))

#q9

name= input()
age = int(input())
city = input()
print(name)
print(age)
print(city)


#q10

list = list(input())
tuple = tuple(input())
print(list)
print(tuple)
