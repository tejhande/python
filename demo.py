str=input("Enter your name: \n\t")
birthdate=input("Enter your Birth Date: \n\t")
template=''' welcome
to to <name> collage
year is <year>

'''
print(template.replace("<name>",str).replace("<year>",birthdate))