#The main() function sets the entry point for a python program. A python program will run line by line, 
#but it won't execute the defined functions until it comes to a line which calls the function.

#When this code is run, the interpreter will define a special variable called __name__ and assign the value of "__main__" to the code in this python file. 
#So the code in our python file becomes __name__ == "__main__".
#When we use import statements, we can import code from other files into our python program.
#When this happens, the imported code is set a __name__ value of the modules name.

#By setting the __name__=="__main__" we can control the order in which the code in this file is executed,
#telling python to run the code in this file which has the name of __main__ rather than the code imported from another file.
#This avoids situations where your code could run an imported script, resulting in unwanted behavior.

#In simpler terms, it's a way to make sure that certain code only runs when you run this specific Python file directly, and not when you use it as part of another program. 
#It helps keep things organized and prevents code from running when you don't want it to.

import boto3

client = boto3.client('translate')

def translate_text():
    response = client.translate_text(
        Text='I am learning to code in AWS',
        SourceLanguageCode='en',
        TargetLanguageCode='fr'
    )
    print(response) # this code is inside the function and will print the contents of the variable 'response'

def main():
    translate_text()

if __name__=="__main__":
    main()
