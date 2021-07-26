#TODO: 
import re, pyperclip
#

phoneRegex = re.compile(r'''
# Types of phone numbers include:
# 123-456-7890, 123-4567, (123) 456-7890, 555-0000, ext 12345, ext. 12345, x12345

((\d\d\d) | (\(\d\d\d)))?   # area code (optional)
(\s|-)                      # separator
\d\d\d                      # first 3 digits
-                           # separator
\d\d\d\d                    # last 4 digits
(ext(\.)?\s|x               # extension (optional)
(\d{2,5}))?                 # extension word part

''', re.VERBOSE)
# create a regex for email addresses

emailRegex = re.compile(r'''
\w{1,21}        # address before extension
\w{1,21}        # email host extension
\w{1,4}         # website extension



''', re.VERBOSE)
# get the text off the clipboard
# extract the email/phone from this text
# copy the extracted email/phone to the clipboard
# 
