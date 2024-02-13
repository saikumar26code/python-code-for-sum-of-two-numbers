# Defining a lambda function to add two numbers

sum_of_two = lambda number1,number2 : number1+number2

#Take two inputs

num1=int(input("First number :"))
num2=int(input("Second number :"))

#Call the lambda function to add the two numbers

result=sum_of_two(num1,num2)

#print the result

print(f"The sum of two {num1} and {num2} is {result}")