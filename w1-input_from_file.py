#The open function is a built-in function. The documentation  shows that there is an optional mode that can be passed in. 
#In the example below we pass in r. 
#This indicates that the file is opened as read-only. To write to the file you need to use w.

with open(filename, 'r' ) as variable_name:
    <Do something with the variable here>


