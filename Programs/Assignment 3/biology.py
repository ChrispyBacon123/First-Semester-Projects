# Program to determine the type of animal
# Christopher Blignaut 
# BLGCHR003
# 9 March 2022

print("Welcome to the Biology Expert")
print("-----------------------------")
print("Answer the following questions by selecting from among the options.")

birth = ""
fetilization = ""
skin = ""
output = ""
location = ""
skeleton = input("The skeleton is (internal/external)?\n")

if skeleton == "external":
    output = "Arthropod"
    
elif skeleton!= "external":
    fetilization = input("The fertilisation of eggs occurs (within the body/outside the body)?\n")
            
    if fetilization =="outside the body":
        location = input("It lives (in water/near water)?\n")
        
        if location == "in water":
            output = "Fish"
        else:
            output = "Amphibian" 
    
    if fetilization == "within the body":
        
        birth = input("Young are produced by (waterproof eggs/live birth)?\n")
        
        if birth == "live birth":
            output = "Mammal"      
            
        elif birth != "live birth":
            skin = input("The skin is covered by (scales/feathers)?\n")
            
            if skin == "scales":
                output = "Reptile"
            elif skin == "feathers":
                output = "Bird"
print ("Type of animal:",output)