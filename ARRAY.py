
stock_prices =[223,225,330,990]
# Static array
# stock_prices.insert(2,333)

#print(stock_prices[2])
# BIG O ANALYSIS
# AS we are checking it by index the time complexity will be O(1)
# #cause of constant operation perform by program
#  in that case we are searching by value instead of index

# for i in range(len(stock_prices)):
#     if stock_prices[i] == 330:
#         print("Found 330 at index", i)

# time complexity is O(n)
# cause we perform n nyumber of operation

# for prices in stock_prices:
#     print(prices)

# the complexity is O(n)
# we are going through all the element and print them

stock_prices.insert(1,335)
print(stock_prices)
# the time complexity of this program is also O(n) same for deletion

# Dynamic array [That are mutable] i.e List in python
