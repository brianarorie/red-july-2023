#To determine what kind of data types your variable use. Use This Method:

datatype = "string bean"
print(type(datatype))

#This is an example of a datatype error:

my_number = 50
some_string = "The number is "
print(some_string + my_number)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str

#To fix the error type you would turn the data type from an integer into a string. Ex:

print(some_string + str(my_number))
