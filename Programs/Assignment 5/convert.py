# Program to convert a time from a compact form to a long form
# Christopher Blignaut 
# BLGCHR003
# 18 March 

#Getting input from user
uIn = input("Enter the date and time (yyyy-mm-dd hh:mm):\n")

#Extracting values from input
year = uIn[:4]
month = uIn[5:7]
day = uIn[8:10]
hour = uIn[uIn.find(":")-2:uIn.find(":")]
minute = uIn[uIn.find(":")+1:uIn.find(":")+3]

#Determining if it is in the morning or night
hourCheck = int(hour)
if hourCheck<12:
    hour = hour + ":" + minute + " am"
else:
    hour = hour + ":" + minute + " pm"
  
#Converting 24 hour to 12 hour
if hour[0:2] == "00":
    hour = "12" + hour[2:]
elif hour[0:2] == "13":
    hour = "1" + hour[2:]
elif hour[0:2] == "14":
    hour = "2" + hour[2:]
elif hour[0:2] == "15":
    hour = "3" + hour[2:]
elif hour[0:2] == "16":
    hour = "4" + hour[2:]
elif hour[0:2] == "17":
    hour = "5" + hour[2:]
elif hour[0:2] == "18":
    hour = "6" + hour[2:]
elif hour[0:2] == "19":
    hour = "7" + hour[2:]
elif hour[0:2] == "20":
    hour = "8" + hour[2:]
elif hour[0:2] == "21":
    hour = "9" + hour[2:]
elif hour[0:2] == "22":
    hour = "10" + hour[2:]
elif hour[0:2] == "23":
    hour = "11" + hour[2:]
    
    
#Formatting Hour
if hour[0:1] =="0":
    hour = hour[1:]

#Formatting the day of the month
if day [0:1] == "0":
    day = day[1:2]
    singleDay = True
else:
    singleDay = False

if day=="11":
    day = day+"th"
elif day[1:2] == "1" or (day[0:1] =="1" and singleDay):
    day = day+"st"
elif day[1:2] == "2" or (day[0:1] =="2" and singleDay):
    day = day+"nd"
elif day[1:2] == "3" or (day[0:1] =="3" and singleDay):
    day = day+"rd"
elif day[1:2] == "4" or (day[0:1] =="4" and singleDay) or day[1:2] == "5" or (day[0:1] =="5" and singleDay) or day[1:2] == "6" or (day[0:1] =="6" and singleDay) or day[1:2] == "7" or (day[0:1] =="7" and singleDay) or day[1:2] == "8" or (day[0:1] =="8" and singleDay) or day[1:2] == "9" or (day[0:1] =="9" and singleDay) or day[1:2] == "0":
    day = day+"th"

#Formatting month
if month == "01":
    month = "January"
elif month == "02":
    month = "February"
elif month == "03":
    month = "March"
elif month == "04":
    month = "April"
elif month == "05":
    month = "May"
elif month == "06":
    month = "June"
elif month == "07":
    month = "July"
elif month == "08":
    month = "August"
elif month == "09":
    month = "September"
elif month == "10":
    month = "October"
elif month == "11":
    month = "November"
elif month == "12":
    month = "December"

#Formatting year
year = "'"+year[2:4]

#Outputting result
print(hour," on the ",day," of ",month," ",year,sep="")