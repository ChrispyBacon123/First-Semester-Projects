# Program that performs Gumatj to Decimal as well as performing basic operations
# Christopher Blignaut 
# BLGCHR003
# 10 April 

# Method that converts a Gumatj number to a Decimal number
def gumatj_to_decimal(gumatj_Num):

    out = gumatj_Num
    
    if gumatj_Num > 10 and gumatj_Num < 15:
        out = gumatj_Num - 5
        
    elif gumatj_Num > 15:
        # Converted into a string to allow slicing
        out = str(out)
        num = int(out[0:1]) * 5                  
        numU= out[1:]
        
        # Checking to see if the number is a multiple of 10 
        if num % 10 != 0:
            out = num + int(numU)
            
        else:
            multi=str(num)
            out = multi[0:1]+numU
            
    return (out)

 
# Method that converts a Decimal number to Gumatj number
def  decimal_to_gumatj(dec_Num):
    
    out = dec_Num
    
    if out > 5 and out < 10:
        out = out + 5
    
    # Checking if the number does not easily fit into a decimal format 
    elif out > 10:
      # Converted into a string to allow slicing
        num = str(dec_Num)
        quot = out//5
        numU = int(num[1:])
        
        if numU > 5:
            out = str(quot) + str(numU - 5)
        else:
            out = str(out) + str(numU)   
            
    return out
  
 
 # Method that outputs the sum of 2 Gumatj numbers
def gumatj_add(num1, num2):

 dec = gumatj_to_decimal(num1) + gumatj_to_decimal(num2)
 convert = decimal_to_gumatj(dec)
 
 return convert
 
  # Method that outputs the product 2 Gumatj numbers
def gumatj_multiply(num1, num2):

 dec = gumatj_to_decimal(num1) * gumatj_to_decimal(num2)
 convert = decimal_to_gumatj(dec)
 
 return convert


#Gum to dec
# out = 0
  
  # # If number has no multiples 
  # if gumatj_Num > 5 and gumatj_Num < 10:
  #   num -= 5
  #   out = "1" + num 
    
  # # If number has multiples 
  # elif gumatj_Num > 10:
  #   num = str(gumatj_Num)
  #   tens = int(num[:1]) * 5
  #   product = str(tens)
  
  # # Splicing string together for output
  #   unit = num[1:]
  #   out = product[:1] + unit
    
  # return out 
  
  
  
  #dec to Gum
  #  # If number is less than 0 
#  if dec_Num <= 0:
   
#   return dec_Num 

# # Generating number 
#  else:
#   num = dec_Num
#   out = ""
#   while num > 0:
#    quot=num // 5
#    remainder = num % 5
#    out = str(remainder) + out
#    number = quot
   
#   return eval(out)