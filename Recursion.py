'''x=input
print(factorial of x)
create a function called factorial that returns the factorial of x'''
'''x = input('Enter Number:\n')
def factorial(x):
    for y in range(x,1,-1):
        print(y)
    return'''
def solver (heads,legs):
    for roadrunner in range(heads+1):
        coyote = heads - roadrunner
        if(coyote*4 + roadrunner*2 == legs):
            return roadrunner, coyote
    return "No Solutions"
solutions = solver(input('Enter Heads: '), input('Enter Legs: '))
#solutions = solver(35,94)
print(solutions)