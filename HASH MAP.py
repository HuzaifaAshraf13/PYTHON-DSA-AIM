# HASH TABLE are DATA STRUCTURE while dict is Python SPECIFIC implementation of HASH TABLE
stock_prices = {
    'April 6':310,
    'May 6':431,
    'june 6':330,
    'Jully 6':334,
}
# stock_prices['April 6'] = 130 # INSERTION O(1)

# print(stock_prices['April 6']) # LOOK AT ITEMS ALSO O(1)
del stock_prices['April 6'] # DELETION O(1)
print(stock_prices)
