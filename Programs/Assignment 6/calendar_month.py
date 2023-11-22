from calendar import isleap
import math
import printmonth
import string  

# Returns the day on which the specific date requested by the user falls 
def day_of_week(day, month, year):
    
    yearStr = str(year) + " "
    # Determining the century code 
    if yearStr[0:2] == "17":
        cen_Code = 4
    elif yearStr[0:2] == "18":
        cen_Code = 2
    elif yearStr[0:2] == "19":
        cen_Code = 0
    elif yearStr[0:2] == "20":
        cen_Code = 6
    elif yearStr[0:2] == "21":
        cen_Code = 4
    elif yearStr[0:2] == "22":
        cen_Code = 2
    elif yearStr[0:2] == "23":
        cen_Code = 0
    
    # Determining the year code
    yearNum = int(yearStr[2:4])
    year_Code = (yearNum +(yearNum//4))%7

    # Determining the month code
    if month == 1:
        mon_Code = 0
    elif month == 2:
        mon_Code = 3
    elif month == 3:
        mon_Code = 3
    elif month == 4:
        mon_Code = 6
    elif month == 5:
        mon_Code = 1
    elif month == 6:
        mon_Code = 4
    elif month == 7:
        mon_Code = 6
    elif month == 8:
        mon_Code = 2
    elif month == 9:
        mon_Code = 5
    elif month == 10:
        mon_Code = 0
    elif month == 11:
        mon_Code = 3
    elif month == 12:
        mon_Code = 5
    
    # Calculation to determine the day that the month starts on
    if is_leap(year):
      dayNum = (year_Code + mon_Code + cen_Code + day -1 ) %7
    else:
      dayNum = (year_Code + mon_Code + cen_Code + day)%7
    
    return dayNum

# Method to deterime if a year is a leap year
def is_leap(year):
    leap = False
    cen_Check = str(year) #Used to check century years (2000;1900)
    
    if year%4 ==0:
        leap = True
    if cen_Check[2:4]=="00":
        if year % 400 == 0:
           leap = True
        else:
            leap = False
    return leap

# Method to return an integer that corresponds to the number month that a user enters 
def month_num(month_name):
    month_name= month_name.upper()
    
    if month_name == "JANUARY":
        return 1
    elif month_name == "FEBRUARY":
        return 2
    elif month_name == "MARCH":
        return 3
    elif month_name == "APRIL":
        return 4
    elif month_name == "MAY":
        return 5
    elif month_name == "JUNE":
        return 6
    elif month_name == "JULY":
        return 7
    elif month_name == "AUGUST":
        return 8
    elif month_name == "SEPTEMBER":
        return 9
    elif month_name == "OCTOBER":
        return 10
    elif month_name == "NOVEMBER":
        return 11
    elif month_name == "DECEMBER":
        return 12
    
# Method to return the number of days in a given month given the year
def num_days_in(month_num, year):
    if month_num == 1 or month_num == 3 or month_num == 5 or month_num == 7 or month_num == 8 or month_num == 10 or month_num == 12: #31 days
        return 31
    elif month_num == 4 or month_num == 6 or month_num == 9 or month_num == 11: #30 days
        return 30
    elif month_num == 2:
        if is_leap(year):
            return 29
        else:
            return 28

# Method to convert day numbers into their days
def num_to_days(dayNum):
  
 # Converting number values into their respective days
    if dayNum == 0:
        return "Sunday"
    elif dayNum == 1:
        return "Monday"
    elif dayNum == 2:
        return "Tuesday"
    elif dayNum == 3:
        return "Wednesday"
    elif dayNum == 4:
        return "Thursday"
    elif dayNum == 5:
        return "Friday"
    elif dayNum == 6:
        return "Saturday"

# Method to determine the number of weeks that a particular month spans
def num_weeks(month_num, year):
    month = str(printmonth.printMonth(month_name(month_num),day_of_week(1,month_num,year),is_leap(year)))
    weeks = month.count("\n") - 3 
   
    return weeks

# Method to generate a week of a month
def week(week_num, start_day, days_in_month):
    
    # Converting start_day into words
    if start_day == 1:
        day = "Monday"
    elif start_day == 2:
        day = "Tuesday"
    elif start_day == 3:
        day = "Wednesday"
    elif start_day == 4:
        day = "Thursday"
    elif start_day == 5:
        day = "Friday"
    elif start_day == 6:
        day = "Saturday"
    elif start_day == 7:
        day = "Sunday"
    
    # Generating month into a string
    if days_in_month == 28:
        month = str(printmonth.printMonth("February",day,False))
    elif days_in_month == 29:
        month = str(printmonth.printMonth("February",day,True))
    elif days_in_month == 30:
        month = str(printmonth.printMonth("April",day,False))
    elif days_in_month == 31:
        month = str(printmonth.printMonth("May",day,False))

    # Splitting the entire month into weeks

    weeks = month.split("\n")

    return weeks[week_num+1]

# Method to convert the month number into it's name
def month_name(month_num):
    if month_num == 1:
        return "January"
    elif month_num == 2:
        return "February"
    elif month_num == 3:
        return "March"
    elif month_num == 4 :
        return "April"
    elif month_num == 5 :
        return "May"
    elif month_num == 6 :
        return "June"
    elif month_num == 7 :
        return "July"
    elif month_num == 8 :
        return "August"
    elif month_num == 9 :
        return "September"
    elif month_num == 10 :
        return "October"
    elif month_num == 11 :
        return "November"
    elif month_num == 12 :
        return "December"
    
def main():
    month = input("Enter month:\n")
    year = eval(input("Enter year:\n"))
    leap = is_leap(year)
    month = month_num(month)
    day = num_to_days(day_of_week(1,month,year))
    month = month_name(month)
    out = printmonth.printMonth(month,day,leap)
    print(out)
    
if __name__=='__main__':
    main()