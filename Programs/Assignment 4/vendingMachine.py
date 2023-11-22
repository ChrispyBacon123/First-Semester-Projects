# Program to simulate vending machine and calculate the change
# Christopher Blignaut 
# BLGCHR003
# 11 March 

cost = int(input("Enter the cost (in cents):\n"))
coins = 0

# Entering payment
while coins<cost:
    pay = int(input("Deposit a coin or note (in cents):\n"))
    coins = coins+pay

coins = coins-cost
r5Coin = 0
r2Coin = 0
r1Coin = 0
c50Coin = 0
c20Coin = 0
c10Coin = 0
c5Coin = 0

if coins>0:
    print ("Your change is:")
    if coins>=500:
        r5Coin = (coins-(coins%500))/500
        print(int(r5Coin),"x R5")
    coins = coins-(500*r5Coin)

    if coins>=200:
        r2Coin = (coins-(coins%200))/200
        print(int(r2Coin),"x R2")
    coins = coins-(200*r2Coin)    

    if coins>=100:
        r1Coin = (coins-(coins%100))/100
        print(int(r1Coin),"x R1")
    coins = coins-(100*r1Coin)

    if coins>=50:
        c50Coin = (coins-(coins%50))/50
        print(int(c50Coin),"x 50c")
    coins = coins-(50*c50Coin)

    if coins>=20:
        c20Coin = (coins-(coins%20))/20
        print(int(c20Coin),"x 20c")
    coins = coins-(20*c20Coin)

    if coins>=10:
        c10Coin = (coins-(coins%10))/10
        print(int(c10Coin),"x 10c")
    coins = coins-(10*c10Coin)

    if coins>=5:
        c5Coin = (coins-(coins%5))/5
        print(int(c5Coin),"x 5c")
    coins = coins-(10*c5Coin)

    if coins>=1:
        print(int(coins),"x 1c")