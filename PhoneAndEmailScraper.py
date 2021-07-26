#TODO: 
import re, pyperclip
#

phoneRegex = re.compile(r'''
# Types of phone numbers include:
# 123-456-7890, 123-4567, (123) 456-7890, 555-0000, ext 12345, ext. 12345, x12345
(
((\d\d\d) | ((\d\d\d)))?   # area code (optional)
(\s|-)?                     # separator
\d\d\d                      # first 3 digits
-                           # separator
\d\d\d\d                    # last 4 digits
(ext(\.)?\s|x               # extension (optional)
(\d{2,5}))?                 # extension word part
)
''', re.VERBOSE)
# create a regex for email addresses

emailRegex = re.compile(r'''

# Types of email addresses 
# something.+_thing(\d{2,5}))?.com

[a-zA-Z0-9_.+]+       # address name
@                     # the @ symbol
[a-zA-Z0-9_.+]+       # domain host
''', re.VERBOSE)

# get the text off the clipboard
text = pyperclip.paste()   

# extract the email/phone from this text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

print(extractedEmail)
print(extractedPhone)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])

# copy the extracted email/phone to the clipboard
results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)
