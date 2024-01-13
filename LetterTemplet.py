from tokenize import Name


letter = '''Dear <|NAME|>,
Greetings from MARSSTRONG INTERNATIONAL. We are happy to let you know about your selection.
You Are Selected!
Have a great day ahead!
Thanks and regards,
Mangesh
Date: <|DATE|>
'''
name = input("Enter Your Name: \n")
date = input("Enter Date: \n" )
# name = (name)
# date = int(date)
letter = letter.replace("<|NAME|>" , name)
letter = letter.replace("<|DATE|>" , date)
print(letter)