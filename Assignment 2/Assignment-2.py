prices = {
    'banana' : 4,
    'apple' : 2,
    'orange' : 1.5,
    'pear' : 3
}

stock = {
    'banana' : 6,
    'apple' : 0,
    'orange' : 32,
    'pear' : 15
}

for i in prices:
    print(i + "\nprice: ", str(prices[i]) + "\nstock: ", str(stock[i]) + "\n")

total = 0
print("Money Earned: ")

for i in prices:
    print(i + ": ",str(prices[i]*stock[i]))
    total = total + (prices[i]*stock[i])
    
print("Total: ",total)


    
