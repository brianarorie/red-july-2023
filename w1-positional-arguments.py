#When an argument is used to customize a program, it is called a parameter.
#In the previous section SourceLanguageCode is an example of a parameter. 
#Which is something the function needs to perform the action required.

#A parameter in Python is like a space in a recipe that you can fill with different things
#when you use the recipe. It makes your code flexible, so you can do different things with it 
#by changing what you put into those spaces.

#The value we assigned en is an example of an argument,
#which is a piece of information to the function so it can perform the designed action.

#A parameter is like the blank space in a recipe, waiting for something to go in.
#An argument is the real thing you put into that space when you use the recipe.

import boto3

def translate_text(text, source_language_code, target_language_code): # we define the positional arguments in the ()
    client = boto3.client('translate')
    response = client.translate_text(
        Text=text, # we remove the hard coded value
        SourceLanguageCode=source_language_code, # we used the positional argument instead
        TargetLanguageCode=target_language_code
    )
    print(response) 

def main():
    translate_text('I am becoming a cloud engineer','en','es') # we provide the value for the arguments when we call the function in the correct positional order.

if __name__=="__main__":
    main()

#By removing the hard coded values we can now call the function multiple times using different values.
#This makes our code flexible and reusable.
