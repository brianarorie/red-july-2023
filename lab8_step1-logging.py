#Using logging allows us to return information about how the program is functioning. 
#Using methods like print() allow us to return information to the user.
#Logging allows us to define a number of different levels of logging.
#This helps to differentiate our different log messages when we conduct log file analysis.

# Import logging
import logging
import json

# This uses a json string as an input
json_string = """
{
    "Input":[
        {
        "Text":"I am learning to code in AWS",
        "SourceLanguageCode":"en",
        "TargetLanguageCode":"fr"
        }
    ]
}
"""

json_input = json.loads(json_string)

# Defines two variables to store the language code from the input.
SourceLanguageCode = json_input['Input'][0]['SourceLanguageCode']
TargetLanguageCode = json_input['Input'][0]['TargetLanguageCode']

# The if statement checks to see if the language code is the same as the source code
if SourceLanguageCode == TargetLanguageCode:
    logging.warning("The SourceLanguageCode is the same as the TargetLanguageCode - stopping") # This will print to the console as the default level is warning
else:
    logging.info("The Source Language and Target Language codes are different - proceeding") # This will not print to the console because it is lower than warning

#When python checked the if statement it only printed a message to the console when the if statement returned False. 
#This is because logging.warning() will print to the console, otherwise the logging.info level will not return anything to the console.