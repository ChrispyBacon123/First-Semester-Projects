# Program to extract wheather data from a string 
# Christopher Blignaut 
# BLGCHR003
# 31 March 

import string

# Extracts the loaction from the block
def location(block):
    city = block[1+block.find('S'):block.find("END")-1] # The values added at the beginning of the slicing are to ensure that the S in begining is not selected
    reverse = ""
    
    if '_' in city:                      
        city = block[24+block.find('N'):block.find("END")-1] # Used to account if the co-ordinates are in the northern hemisphere
    
    for i in city:              #Converting name of location to a readable format
        reverse = i+reverse
    
    reverse = reverse.title()
    return reverse

# Extracts the temprature from the block
def temperature(block):
    temp = block[6:block.find("_")]
    temp = float(temp)
    return temp

# Extracts the x co-ordinate from the block
def x_coordinate(block):
    coord = block[block.find(":")+1:block.find(",")]
    return coord

# Extracts the y co-ordinate from the block
def y_coordinate(block):
    coord = block[block.find(",")+1:block.find(",")+6]
    return coord

# Extracts the pressure from the block
def pressure(block):
    pressure = block[block.find("_")+1:block.find(":")]
    pressure = float(pressure)
    return pressure


# Extracts the relevent block of data from the string
def get_block(data):
    block = data[data.find("BEGIN"):data.find("END")+3]
    return block

def main():
    data = input('Enter the raw data:\n')
    block = get_block(data)
    print('Site information:')
    print('Location:', location(block))
    print('Coordinates:', y_coordinate(block), x_coordinate(block))
    print('Temperature: {:.2f} C'.format(temperature(block)))
    print('Pressure: {:.2f} hPa'.format(pressure(block)))

if __name__=='__main__':
    main()

#fds BEGIN 12.2_1014:18.6E,34.0N NWOT EPAC END fdf fds 
#fds BEGIN 12.2_1014:18.6E,34.0S NWOT EPAC END fdf fds 