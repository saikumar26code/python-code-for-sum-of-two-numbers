# Define a recursive function to add two numbers

def add(number1,number2):
    if number2==0:
        return number1
    else:
        return add(number1+1,number2-1)

#Take input from user

num1=int(input("First number :"))
num2=int(input("Second number :"))

#Call the recursive function

result=add(num1,num2)

#print the result

print(f"the sum of {num1} and {num2} is {result}")