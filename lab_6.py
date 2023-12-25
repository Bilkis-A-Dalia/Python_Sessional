# integer
# age = 21
age = int(input('Enter your age: '))
print('Age: ',age,type(age))

# float
height = float(input('Enter your height: '))
print('height: ',height,type(height))

# string
name = input('Enter your name: ')
print('Name: ',name,type(name))

# Boolean 
is_student = True
not_student = False
print('i am student -> ',is_student,type(is_student))
print('i am not a student -> ',not_student,type(not_student))

# List:collection which is ordered, changeable and allow duplicate []
fav_colorSet = ['blue','white','merron']
print('Favorite color set: ',fav_colorSet,type(fav_colorSet))

# tuple: collection which is ordered, unchangeable and allow duplicate ()
coordinates = (5,6)
print('Coordinates: ',coordinates,type(coordinates))

# Dictionary: collection which is ordered, changeable and no duplicate {key,value}
person = {'Name:':'Dalia','Age: ':'21','is_student: ':True}
print('My details: ',person,type(person))

# set: collection which is unordered, unchangeable,unindexed and no duplicate {}
unique_numbers = {1,2,3,4,5}
print('Unique numbers are: ',unique_numbers,type(unique_numbers))
