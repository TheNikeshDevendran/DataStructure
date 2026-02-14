'''
Function is nothing but a reusable block of code
It follow DRY principal
In function write once and use it multiple times

*There are 2 types of function*
1.userdefined
2.predefined (input,print,lower,upper etc...)
Manditory part of function is 
1.Declaration a function
2.calling a function

optional part is 
3.return 
4.Argumants/parameters
'''

def Dosomething():
    """
    This function prints a greeting message
    and asks the user to define what they want the function to do.
    """
    print('Hi i am a function')
    print('Please defined what u want me to do.')

print(Dosomething.__doc__)
help(Dosomething)

# Recursion
'''
A function which call itself is known as recursive function and the process
is known as recursion
It follow divide and conqure rule
It is used for its problem solving ability
It take more time and space
A we know that it executes in stack mememory if that has less space then it cause error
'''
