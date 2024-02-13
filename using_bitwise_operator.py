#Define the recursive function 

def add_recursive(number1,number2):
    
    #create a while loop , repeat until number2 becomes zero

    while (number2!=0):
        
        #calcualte the carry by performing bitwise AND between 'number1' and 'number2'
        carry=number1&number2

        #calculate the sum of 'number1' and 'number2' without considering any carry
        number1=number1^number2

        #shift the carry to the left by one positon
        number2=carry<<1

    #return the final sum
    return number1

#print the result of inputs 'a' and 'b'
num1=int(input("First number :"))
num2=int(input("Second number :"))
print(add_recursive(num1,num2))

