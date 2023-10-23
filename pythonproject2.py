#Bri Rorie - Python Project
#This Enables Interaction With Files & Directories
import os
#This Will Allow Me Find Files In The Directory With Specific Criteria ("*.py")
import glob
#This Allows Me To Access & Use Time Related Functions
import time
#This Looks For All The Files In My Current Directory That End In ("*.py")
py_files = glob.glob("*.py")
#I'm Creating An Empty List To Store The Dictionaries
file_info = []
#This Will Iterate Through The Files In My Branch Directory
for file in py_files:
#This Creates An Empty Dictionary     
    file_dict = {}
    file_dict['name'] = file
    file_dict['size'] = os.path.getsize(file)
    file_dict['permissions'] = oct(os.stat(file).st_mode)[-3:]
    file_dict['last_modified'] = time.strftime('%I:%M %p',time.localtime(os.path.getmtime(file)))
    file_info.append(file_dict)
    
#This Will Print Out The List Of Files In A Dictionary Format
print(file_info)
