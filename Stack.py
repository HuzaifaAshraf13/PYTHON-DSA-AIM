""" DATASTRUCTURE to manage the order like tracing your activity through pages
 Like we see in BROWSER
 TO DIRECTLY POP SPECIFIC ELEMENT WITHOUT iterating throughout list
 PUSH &  POP  OPERATIONS
 STACK IS A DATA STRUCTURE that keeps on pushing element until you pop out last element you pushed """

# POP FUNCTION help removeing the element from the LIST
# s = []
# s.append('http/EDENco.com/ENTER')
# s.append('http/EDENco.com/Home PAGE')
# s.append('http/EDENco.com/ ABOUT US ')
# s.append('http/EDENco.com/ BLOG ')
# # REMOVING LAST ELEMENT  'http/EDENco.com/ BLOG ' from list
# # USING LIST AS A STACK
# s.pop()
# print(s)
# s.pop()
# print(s)
""" USE list for implementing stack nut list is an dynamic array if you have a million element 
    you have to copy them all and puch to another memory (in order to append) location which is expensive
      the deque would allow us to append without copying the previous element  """
# implementation of stack using deques

from collections import deque
stack = deque()
dir(stack)
stack.append('http/EDENco.com/ENTER')
stack.append('http/EDENco.com/LOGIN')
stack.append('http/EDENco.com/HOME')
stack.append('http/EDENco.com/BLOG')
# stack.pop()
# print(stack)
# stack.popleft()
# print(stack)
stack.append('http/EDENco.com/About us')
print(stack)






