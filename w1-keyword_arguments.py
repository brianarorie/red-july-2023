#A keyword argument is a name-value pair that is passed to the function. Here are some of the advantages:

#If the values passed with positional arguments are wrong, you will get an error or unexpected behavior. Keyword arguments can be passed in any order.
#When used with the ** we can pass an arbitrary number of keyword arguments.
#We can reduce the number of lines in our code.

#Ex:

import boto3

def translate_text(**kwargs): 
    client = boto3.client('translate')
    response = client.translate_text(**kwargs)
    print(response) 

def main():
    translate_text(SourceLanguageCode='en',TargetLanguageCode='fr',Text='I am learning to code in AWS')

if __name__=="__main__":
    main()

#To use dictionaries as keyword arguments , you would replace the key=value format with "key":"value" format.
#Example:

import boto3

def translate_text(**kwargs): 
    client = boto3.client('translate')
    response = client.translate_text(**kwargs)
    print(response) 

### Change below this line only ###

kwargs={
    "Text":"I am learning to code in AWS",
    "SourceLanguageCode":"en",
    "TargetLanguageCode":"fr"
    }

def main():
    translate_text(**kwargs)

if __name__=="__main__":
    main()

#We defined a variable called kwargs containing a dictionary of key\:value pairs.
#We replaced the keyword arguments when we called the function with **kwargs. 
#The ** tells python that it is an arbitrary number of arguments, kwargs is the function name we defined.
#We put each key\:value pair on a separate line to make it easy to read.