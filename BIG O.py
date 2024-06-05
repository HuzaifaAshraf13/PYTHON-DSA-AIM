# def get_squared_numbers(numbers):
#     squared_numbers = []
#     for n in numbers:
#         squared_numbers.append(n * n)
#     return squared_numbers
#
# numbers = [2, 3, 5, 6, 7]
# print(get_squared_numbers(numbers))  # This will print the squared numbers
# # cause the time increases to execute a program as a size increases so  time complexity is o(n)

def find_first_pe(prices,eps,index):
    pe = prices[index]/ eps[index]
    return pe
# the index provided execute a constant operation so
# time execution is going to be constant so   o(1)
