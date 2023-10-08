#The default logging level is set at warning. 
#This can be changed so that we capture more or less information in the log files. 
#In the last example, only the warning returned a result to the console meaning we didn't see any other log data.

# Import logging
import logging
import json

# Set the log level in the basic configuration.  This means we will capture all our log entries and not just those at Warning or above.
logging.basicConfig(filename='example.log',level=logging.DEBUG)

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

#We set the logging level in logging.basicConfig(filename='example.log,level=logging.DEBUG) to DEBUG. 
#This ensures that any errors which are DEBUG and above will be logged. 
#In effect, this ensures that everything is logged.
#We told python to create a log file called example.log in Cloud9

#This should return nothing to the console. This is because by default the logging level is set to logging.warning.
#Because the code is correct, it does not generate a warning.