#A dictionary is a way of storing related information in key-value pairs.
#It uses a key as an identifier and a value to store the information.
#The key could be first_name and the value could be Ada.
#Example {"first_name": "Ada"}
#They are used to exchange information between different services and functions
#They are returned by Application Programming Interfaces (API)
#They are used as Tag values
#The Code Below Creates A Value In a Dictionary :

user = {"first_name":"Ada"}
print(user)

#You Can Add The Contents To the Dictionary Later Using Either Of The Following Methods:
# dictionary_example1 = {}
# OR dictionary_example2 = dict()
#To read the value associated with a key, you need to provide the name of the dictionary,
#and the the value of the key inside square brackets.

#Example :
# This Code Is Used To Read A Value :
user = {"first_name":"Ada"}
print(user["first_name"])

#To Add A New Key & Value To A Dictionary :
#To add an additional key-value to a dictionary, provide the dictionary name 
#,the new key in [] and a value after an = sign.

#Example :

user["last_name"] = "waters"
print(user)

#The Same Process Is Used For Modifying A Dictionary, Just Insert New Value
#To remove a key-value pair you use the del statement 
#with the name of the dictionary and the key you want to delete.

#del user["last_name"]
#print(user)