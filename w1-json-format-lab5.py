import json

# This uses a json string as an input 

json_string = """
{
    "Input":[
        {
        "Text":"I am learning to code in AWS",
        "SourceLanguageCode":"en",
        "TargetLanguageCode":"fr",
        "Required": true
        }
    ]
}
"""
# Modify below this line
def main():
    json_input = json.loads(json_string)
    text = json_input['Input'][0]['Text']
    source_language_code = json_input['Input'][0]['SourceLanguageCode']
    target_language_code = json_input['Input'][0]['TargetLanguageCode']
    print(text, source_language_code, target_language_code)

if __name__=="__main__":
    main()

#If you look at the structure above you can see that it comprises a dictionary with a key of "Input" and a value of a list containing another dictionary.
#This is called nesting. It is very common to have dictionaries which contain lists, which contain dictionaries. 