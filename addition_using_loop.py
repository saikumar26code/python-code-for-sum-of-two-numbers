#define the addition function

def add_with_loop(x,y):
    result=[]
    carry=0

    while x>0 or y>0 or carry>0:
        digit_sum= (x%10) + (y%10) + carry
        carry=digit_sum//10
        result.append(digit_sum%10)
        x=x//10
        y=y//10
    final_sum=int("".join(map(str,reversed(result))))
    return final_sum

num1=int(input("first number :"))
num2=int(input("second number :"))
print("sum :",add_with_loop(num1,num2))