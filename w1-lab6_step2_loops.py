# Standard Imports
import argparse
import json

# 3rd Party Imports
import boto3 

# Arguments
parser = argparse.ArgumentParser(description="Provides translation  between one source language and another of the same set of languages.")
parser.add_argument(
    '--file',
    dest='filename',
    help="The path to the input file. The file should be valid json",
    required=True)

args = parser.parse_args()

# Functions
def open_input():
    """This function returns a dictionary containing the contents of the Input section in the input file""" 
    with open(args.filename) as file_object:
        contents = json.load(file_object)
    return contents['Input']

# Boto3 function to use Amazon Translate to translate the text and only return the Translated Text
def translate_text(**kwargs): 
    client = boto3.client('translate')
    response = client.translate_text(**kwargs)
    print(response['TranslatedText']) 

# Add a Loop to iterate over the json file.
def translate_loop():
    input_text = open_input()
    for item in input_text: # Here we iterate over all dictionaries in the Input list
        translate_text(**item)

# Create a list of the input text
def new_input_text_list():
    input_text = open_input()
    new_list = []
    for item in input_text:
        text = item['Text']
        new_list.append(text)
    print(new_list)

# Main Function - use to call other functions
#Remember to call the function from your main() otherwise it won't run.
#Using a for loop to generate new lists using .append() is a perfectly valid way of generating new lists.
#However, we can use a list comprehension to reduce this to a single line. 
#It combines the for loop and the creation of the list into a single line.

def new_list_comprehension():
    input_text = open_input()
    list_comprehension = [item['Text'] for item in input_text]
    print(list_comprehension)

def main():
    translate_loop()
    new_input_text_list()
    new_list_comprehension()

if __name__ == "__main__":
    main()
    
#Using a for loop to generate new lists using .append() is a perfectly valid way of generating new lists.
#However, we can use a list comprehension to reduce this to a single line. 
#It combines the for loop and the creation of the list into a single line.
#argparse is a built in python argument parser that allows you to write user friendly command line
#interfaces
    

