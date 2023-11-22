# Program to workout the BMI of a person 
# Christopher `Blignaut
# BLGCHR003
# 5 April 2022


# Weight^2/height`
def calculateBMI(weight, height):
    bmi = (weight)/height**2
    return "Your BMI is: "+ str(bmi)

def main():
    inp = input("Do you want to calculate (Y/N)?")
    while inp != "N":
        height = eval(input("What is your heigh (in metres, e.g. 1.65)?"))
        weight = eval(input("What is your weight (in kg, e.g. 72.5)?"))
        print(calculateBMI(weight, height))
        inp = input("Do you want to calculate again (Y/N)?")
        
    print("\nHave a nice day :)")
    
main()