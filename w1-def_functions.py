#A python package is code comprising of individual components called modules that we can use in our code. 
#Packages save us from having to write every aspect of our program from scratch by allowing us to use other peoples code. 
#By importing packages into our program we can use the features of that package.

#In python we can declare a function using the syntax def function_name():

# A function that prints hello world
def hello_world():
    print('hello world')

# This line calls (runs) the function
hello_world()

#When a function performs some kind of activity, by default the information remains contained within the boundary of the function. 
#To pass the information to other parts of your code, you need to use return.
#The value the function returns is called the return value and it is passed back to the line which called the function.

# A function that returns hello world
def hello_world():
    return 'hello world'

# Assign the hello_world() function to a variable.
greeting = hello_world()
print(greeting)