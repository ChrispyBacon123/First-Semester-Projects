# Program to format an entered string into a reference
# Christopher Blignaut 
# BLGCHR003
# 18 March 

import string
reference = input("Enter the reference:\n")

#Formatting the authors
authors = reference[0:reference.find("(")]
authors = authors.title()
authors = authors + reference[reference.find("("):reference.find(")")]+")"
reference[reference.find(")")]

#Formatting the title
nameAndOthers= reference[reference.find(") ")+2:]
name = nameAndOthers[:nameAndOthers.find(",")]
name = name.lower()
name = name[0].upper() + name[1:]

#Converting back to one string and outputting result
out = authors+ " " + name + nameAndOthers[nameAndOthers.find(","):]
print("Reformatted reference:")
print(out)