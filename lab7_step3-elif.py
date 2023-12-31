#The and statement is a logical operator that combines the check for both source language and target language. 
#The elif statement allows us to introduce multiple different logical checks.

import json

# A defined list of languages supported by Amazon Translate
languages = ["af","sq","am","ar","az","bn","bs","bg","zh","zh-TW","hr","cs","da","fa-AF","nl","en","et","fi","fr","fr-CA","ka","de","el","ha","he","hi","hu","id","it","ja","ko","lv","ms","no","fa","ps","pl","pt","ro","ru","sr","sk","sl","so","es","sw","sv","tl","ta","th","tr","uk","ur","vi"]

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

SourceLanguageCode = json_input['Input'][0]['SourceLanguageCode']
TargetLanguageCode = json_input['Input'][0]['TargetLanguageCode']

# Uses an if-elif-else statements to check that the SourceLanguageCode is in the languages list.
if SourceLanguageCode == TargetLanguageCode:
    print("The SourceLanguageCode is the same as the TargetLanguageCode - nothing to do")
elif SourceLanguageCode not in languages and TargetLanguageCode not in languages:
    print("Neither the SourceLanguageCode and TargetLanguageCode are valid - stopping")
elif SourceLanguageCode not in languages:
    print("The SourceLanguageCode is not valid - stopping")
elif TargetLanguageCode not in languages:
    print("The TargetLanguageCode is not valid - stopping")
elif SourceLanguageCode in languages and TargetLanguageCode in languages:
    print("The SourceLanguageCode and TargetLanguageCode are valid - proceeding")
else:
    print("There is an issue")

#"Input" is a list that contains one item, and that item is enclosed in curly braces {}.
#The item inside the "Input" list is at index 0 because lists in Python are zero-indexed. 
#This item is represented by the following part: