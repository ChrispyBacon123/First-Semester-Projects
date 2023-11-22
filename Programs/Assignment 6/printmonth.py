# Program to output a calendar month based on an input from a user
# Christopher Blignaut 
# BLGCHR003
# 13 March 


def printMonth(month, day,leap):
    out = "" 
    
    # If month has 28 days
    if month == "February": 
        if leap:
            dayNum = 30
        else:
            dayNum = 29

        out = str(month)+"\n"
        out = out +"Mo Tu We Th Fr Sa Su\n"
        if day == "Monday":
            out = out + " 1  2  3  4  5  6  7\n"
            numOfDays = 8
            for i in range (5):
                for j in range (7):
                    a = format(numOfDays, "2")
                    if numOfDays < dayNum:
                      out = out +str(a)+" "  
                    numOfDays += 1
                out = out +"\n"   
            return (out)      
                
        elif day == "Tuesday":
            out = out +"    1  2  3  4  5  6\n"
            numOfDays = 7
            for i in range (5):
                for j in range (7):
                    a = format(numOfDays, "2")
                    if numOfDays < dayNum:
                      out = out +str(a)+" "  
                    numOfDays += 1
                out = out +"\n"   
            return (out)      
                 
        elif day == "Wednesday":
            out = out +"       1  2  3  4  5\n"
            numOfDays = 6
            for i in range (5):
                for j in range (7):
                    a = format(numOfDays, "2")
                    if numOfDays < dayNum:
                      out = out +str(a)+" "  
                    numOfDays += 1
                out = out +"\n"   
            return (out)      
            
        elif day == "Thursday":
            out = out +"          1  2  3  4\n"
            numOfDays = 5
            for i in range (5):
                for j in range (7):
                    a = format(numOfDays, "2")
                    if numOfDays < dayNum:
                      out = out +str(a)+" "  
                    numOfDays += 1
                out = out +"\n"   
            return (out)    
          
        elif day == "Friday":
            out = out +"             1  2  3\n"
            numOfDays = 4
            for i in range (5):
                for j in range (7):
                    a = format(numOfDays, "2")
                    if numOfDays < dayNum:
                      out = out +str(a)+" "  
                    numOfDays += 1
                out = out +"\n"   
            return (out)
         
        elif day == "Saturday":
            out = out + "                1  2\n" 
            numOfDays = 3
            for i in range (5):
                for j in range (7):
                    a = format(numOfDays, "2")
                    if numOfDays < dayNum:
                      out = out +str(a)+" "  
                    numOfDays += 1
                out = out +"\n"   
            return (out)
        
        elif day == "Sunday":
            out = out + "                   1\n"
            numOfDays = 2
            for i in range (5):
                for j in range (7):
                    a = format(numOfDays, "2")
                    if numOfDays < dayNum:
                      out = out +str(a)+" "  
                    numOfDays += 1
                out = out +"\n"   
            return (out)
    
          
    # If month has 31 days
    elif month == "January" or month == "March" or month == "May" or month == "July" or month == "August" or month == "October" or month == "December": #31 days
        
        dayNum = 32 
        
        out = str(month)+"\n"
        out = out +"Mo Tu We Th Fr Sa Su\n"
        
        if day == 'Monday':
            out = out + " 1  2  3  4  5  6  7\n"
            numOfDays = 8
            for i in range (5):
                for j in range (7):
                    a = format(numOfDays, "2")
                    if numOfDays < dayNum:
                      out = out +str(a)+" "  
                    numOfDays += 1
                out = out +"\n"   
            return (out)      
                
        elif day == "Tuesday":
            out = out +"    1  2  3  4  5  6\n"
            numOfDays = 7
            for i in range (5):
                for j in range (7):
                    a = format(numOfDays, "2")
                    if numOfDays < dayNum:
                      out = out +str(a)+" "  
                    numOfDays += 1
                out = out +"\n"   
            return (out)      
                 
        elif day == "Wednesday":
            out = out +"       1  2  3  4  5\n"
            numOfDays = 6
            for i in range (5):
                for j in range (7):
                    a = format(numOfDays, "2")
                    if numOfDays < dayNum:
                      out = out +str(a)+" "  
                    numOfDays += 1
                out = out +"\n"   
            return (out)      
            
        elif day == "Thursday":
            out = out +"          1  2  3  4\n"
            numOfDays = 5
            for i in range (5):
                for j in range (7):
                    a = format(numOfDays, "2")
                    if numOfDays < dayNum:
                      out = out +str(a)+" "  
                    numOfDays += 1
                out = out +"\n"   
            return (out)    
          
        elif day == "Friday":
            out = out +"             1  2  3\n"
            numOfDays = 4
            for i in range (5):
                for j in range (7):
                    a = format(numOfDays, "2")
                    if numOfDays < dayNum:
                      out = out +str(a)+" "  
                    numOfDays += 1
                out = out +"\n"   
            return (out)
         
        elif day == "Saturday":
            out = out + "                1  2\n" 
            numOfDays = 3
            for i in range (5):
                for j in range (7):
                    a = format(numOfDays, "2")
                    if numOfDays < dayNum:
                      out = out +str(a)+" "  
                    numOfDays += 1
                out = out +"\n"   
            return (out)
        
        elif day == "Sunday":
            out = out + "                   1\n"
            numOfDays = 2
            for i in range (5):
                for j in range (7):
                    a = format(numOfDays, "2")
                    if numOfDays < dayNum:
                      out = out +str(a)+" "  
                    numOfDays += 1
                out = out +"\n"   
            return (out)
                
    # If month has 30 days
    elif month == "April" or month == "June" or month == "September" or month == "November": #30 days
        
        dayNum = 31 
        
        out = str(month)+"\n"
        out = out +"Mo Tu We Th Fr Sa Su\n"
        
        if day == 'Monday':
            out = out + " 1  2  3  4  5  6  7\n"
            numOfDays = 8
            for i in range (5):
                for j in range (7):
                    a = format(numOfDays, "2")
                    if numOfDays < dayNum:
                      out = out +str(a)+" "  
                    numOfDays += 1
                out = out +"\n"   
            return (out)      
                
        elif day == "Tuesday":
            out = out +"    1  2  3  4  5  6\n"
            numOfDays = 7
            for i in range (5):
                for j in range (7):
                    a = format(numOfDays, "2")
                    if numOfDays < dayNum:
                      out = out +str(a)+" "  
                    numOfDays += 1
                out = out +"\n"   
            return (out)      
                 
        elif day == "Wednesday":
            out = out +"       1  2  3  4  5\n"
            numOfDays = 6
            for i in range (5):
                for j in range (7):
                    a = format(numOfDays, "2")
                    if numOfDays < dayNum:
                      out = out +str(a)+" "  
                    numOfDays += 1
                out = out +"\n"   
            return (out)      
            
        elif day == "Thursday":
            out = out +"          1  2  3  4\n"
            numOfDays = 5
            for i in range (5):
                for j in range (7):
                    a = format(numOfDays, "2")
                    if numOfDays < dayNum:
                      out = out +str(a)+" "  
                    numOfDays += 1
                out = out +"\n"   
            return (out)    
          
        elif day == "Friday":
            out = out +"             1  2  3\n"
            numOfDays = 4
            for i in range (5):
                for j in range (7):
                    a = format(numOfDays, "2")
                    if numOfDays < dayNum:
                      out = out +str(a)+" "  
                    numOfDays += 1
                out = out +"\n"   
            return (out)
         
        elif day == "Saturday":
            out = out + "                1  2\n" 
            numOfDays = 3
            for i in range (5):
                for j in range (7):
                    a = format(numOfDays, "2")
                    if numOfDays < dayNum:
                      out = out +str(a)+" "  
                    numOfDays += 1
                out = out +"\n"   
            return (out)
        
        elif day == "Sunday":
            out = out + "                   1\n"
            numOfDays = 2
            for i in range (5):
                for j in range (7):
                    a = format(numOfDays, "2")
                    if numOfDays < dayNum:
                      out = out +str(a)+" "  
                    numOfDays += 1
                out = out +"\n"   
            return (out)
     
# def main():    
#     month = input("month") 
#     day = input("day")      
#     print(printMonth(month,day,True))
    
# main()




"""    # if month == "February": 
    #     print(month)
    #     print("Mo", "Tu", "We", "Th", "Fr", "Sa", "Su")

    #     if day == "Monday":
    #         print(" 1", " 2", " 3", " 4", " 5", " 6", " 7", sep = " ")
    #         numOfDays = 8
    #         for i in range (5):
    #             for j in range (7):
    #                 a = format(numOfDays, "2")
    #                 if numOfDays < 29:
    #                     print(a, end = " ")
    #                 numOfDays += 1
    #             print("")         
                
    #     elif day == "Tuesday":
    #         print("  ", " 1", " 2", " 3", " 4", " 5", " 6", sep = " ")
    #         numOfDays = 7
    #         for i in range (5):
    #             for j in range (7):
    #                 a = format(numOfDays, "2")
    #                 if numOfDays < 29:
    #                     print(a, end = " ")
    #                 numOfDays += 1
    #             print("")
                 
    #     elif day == "Wednesday":
    #         print("  ", "  ", " 1", " 2", " 3", " 4", " 5", sep = " ")
    #         numOfDays = 6
    #         for i in range (5):
    #             for j in range (7):
    #                 a = format(numOfDays, "2")
    #                 if numOfDays < 29:
    #                     print(a, end = " ")
    #                 numOfDays += 1
    #             print("")
    #     elif day == "Thursday":
    #         print("  ", "  ", "  ", " 1", " 2", " 3", " 4", sep = " ")
    #         numOfDays = 5
    #         for i in range (5):
    #             for j in range (7):
    #                 a = format(numOfDays, "2")
    #                 if numOfDays < 29:
    #                     print(a, end = " ")
    #                 numOfDays += 1
    #             print("")
    #     elif day == "Friday":
    #         print("  ", "  ", "  ", "  ", " 1", " 2", " 3", sep = " ")
    #         numOfDays = 4
    #         for i in range (5):
    #             for j in range (7):
    #                 a = format(numOfDays, "2")
    #                 if numOfDays < 29:
    #                     print(a, end = " ")
    #                 numOfDays += 1
    #             print("")
    #     elif day == "Saturday":
    #         print("  ", "  ", "  ", "  ", "  ", " 1", " 2", sep = " ")
    #         numOfDays = 3
    #         for i in range (5):
    #             for j in range (7):
    #                 a = format(numOfDays, "2")
    #                 if numOfDays < 29:
    #                     print(a, end = " ")
    #                 numOfDays += 1
    #             print("")
    #     elif day == "Sunday":
    #         print("  ", "  ", "  ", "  ", "  ", "  ", " 1", sep = " ")
    #         numOfDays = 2
    #         for i in range (5):
    #             for j in range (7):
    #                 a = format(numOfDays, "2")
    #                 if numOfDays < 29:
    #                     print(a, end = " ")
    #                 numOfDays += 1
    #             print("")
    # 
    # 
    # elif month == "January" or month == "March" or month == "May" or month == "July" or month == "August" or month == "October" or month == "December": #31 days
        
        print(month)
        print("Mo", "Tu", "We", "Th", "Fr", "Sa", "Su")
        if day == "Monday":
            print(" 1", " 2", " 3", " 4", " 5", " 6", " 7", sep = " ")
            numOfDays = 8
            for i in range (5):
                for j in range (7):
                    a = format(numOfDays, "2")
                    if numOfDays < 32:
                        print(a, end = " ")
                    numOfDays += 1
                print("")
        elif day == "Tuesday":
            print("  ", " 1", " 2", " 3", " 4", " 5", " 6", sep = " ")
            numOfDays = 7
            for i in range (5):
                for j in range (7):
                    a = format(numOfDays, "2")
                    if numOfDays < 32:
                        print(a, end = " ")
                    numOfDays += 1
                print("")
        elif day == "Wednesday":
            print("  ", "  ", " 1", " 2", " 3", " 4", " 5", sep = " ")
            numOfDays = 6
            for i in range (5):
                for j in range (7):
                    a = format(numOfDays, "2")
                    if numOfDays < 32:
                        print(a, end = " ")
                    numOfDays += 1
                print("")
        elif day == "Thursday":
            print("  ", "  ", "  ", " 1", " 2", " 3", " 4", sep = " ")
            numOfDays = 5
            for i in range (5):
                for j in range (7):
                    a = format(numOfDays, "2")
                    if numOfDays < 32:
                        print(a, end = " ")
                    numOfDays += 1
                print("")
        elif day == "Friday":
            print("  ", "  ", "  ", "  ", " 1", " 2", " 3", sep = " ")
            numOfDays = 4
            for i in range (5):
                for j in range (7):
                    a = format(numOfDays, "2")
                    if numOfDays < 32:
                        print(a, end = " ")
                    numOfDays += 1
                print("")
        elif day == "Saturday":
            print("  ", "  ", "  ", "  ", "  ", " 1", " 2", sep = " ")
            numOfDays = 3
            for i in range (5):
                for j in range (7):
                    a = format(numOfDays, "2")
                    if numOfDays < 32:
                        print(a, end = " ")
                    numOfDays += 1
                print("")
        elif day == "Sunday":
            print("  ", "  ", "  ", "  ", "  ", "  ", " 1", sep = " ")
            numOfDays = 2
            for i in range (5):
                for j in range (7):
                    a = format(numOfDays, "2")
                    if numOfDays < 32:
                        print(a, end = " ")
                    numOfDays += 1
                print("") 
                
    # If month has 30 days
    elif month == "April" or month == "June" or month == "September" or month == "November": #30 days
        
        print(month)
        print("Mo", "Tu", "We", "Th", "Fr", "Sa", "Su")
        if day == "Monday":
            print(" 1", " 2", " 3", " 4", " 5", " 6", " 7", sep = " ")
            numOfDays = 8
            for i in range (5):
                for j in range (7):
                    a = format(numOfDays, "2")
                    if numOfDays < 31:
                        print(a, end = " ")
                    numOfDays += 1
                print("")
        elif day == "Tuesday":
            print("  ", " 1", " 2", " 3", " 4", " 5", " 6", sep = " ")
            numOfDays = 7
            for i in range (5):
                for j in range (7):
                    a = format(numOfDays, "2")
                    if numOfDays < 31:
                        print(a, end = " ")
                    numOfDays += 1
                print("")
        elif day == "Wednesday":
            print("  ", "  ", " 1", " 2", " 3", " 4", " 5", sep = " ")
            numOfDays = 6
            for i in range (5):
                for j in range (7):
                    a = format(numOfDays, "2")
                    if numOfDays < 31:
                        print(a, end = " ")
                    numOfDays += 1
                print("")
        elif day == "Thursday":
            print("  ", "  ", "  ", " 1", " 2", " 3", " 4", sep = " ")
            numOfDays = 5
            for i in range (5):
                for j in range (7):
                    a = format(numOfDays, "2")
                    if numOfDays < 31:
                        print(a, end = " ")
                    numOfDays += 1
                print("")
        elif day == "Friday":
            print("  ", "  ", "  ", "  ", " 1", " 2", " 3", sep = " ")
            numOfDays = 4
            for i in range (5):
                for j in range (7):
                    a = format(numOfDays, "2")
                    if numOfDays < 31:
                        print(a, end = " ")
                    numOfDays += 1
                print("")
        elif day == "Saturday":
            print("  ", "  ", "  ", "  ", "  ", " 1", " 2", sep = " ")
            numOfDays = 3
            for i in range (5):
                for j in range (7):
                    a = format(numOfDays, "2")
                    if numOfDays < 31:
                        print(a, end = " ")
                    numOfDays += 1
                print("")
        elif day == "Sunday":
            print("  ", "  ", "  ", "  ", "  ", "  ", " 1", sep = " ")
            numOfDays = 2
            for i in range (5):
                for j in range (7):
                    a = format(numOfDays, "2")
                    if numOfDays < 31:
                        print(a, end = " ")
                    numOfDays += 1
                print("")"""
    