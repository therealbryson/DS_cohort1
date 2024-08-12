# def my_function():   # No parameter function 
#     print('Hello Welcome to Function, This is my first function')
# my_function() # calling the function

# def function_param(location):
#         print('GoMyCode Hackerspace '+location)
# function_param('Ikeja')
# function_param('Yabba')

# def function_param1(name, location, destination):
#     print('Welcome'+name)
#     print('You are from'+location)
#     print('You are now in'+destination)

# function_param1('Enoch','Lagos','Qatar')


def caculate_math(x,y,z):
    print((x+y)*z)

caculate_math(2,6,3)

# Default argument or parameter 

def default_param(name,location,destination='Germany'):
    print('Welcome'+name)
    print('You are from'+location)
    print('You are now in'+destination)

default_param('Enoch', 'Lagos','Dubai')

