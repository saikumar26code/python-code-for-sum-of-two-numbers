#READ ALL THE COMMENTS IF YOU ARE BEGGINER FOR CODING

#program to add two numbers in python by importing the operator module

import operator

#Taking inputs as integers 
#You can also use other datatypes like float

number1=int(input("First number :"))
number2=int(input("Second number:"))

#operator.add is a inbuilt function in operator module

sum=operator.add(number1,number2)
print(sum)