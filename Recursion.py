'''x=input
print(factorial of x)
create a function called factorial that returns the factorial of x'''
#x = input('Enter Number:\n')
def factorial(x):
    num = 1
    if(x>0):
        for y in range(2, x+1):
            num *= y
        return num
    elif(x==0):
        return "1"
    else:
        return "Impossible"

number = factorial(3)
print(number,end='!\n')
print(factorial(number))
