# # Exercise 1: Basic Tuple Operations
# tpl = (1,2,3,4.5,"Python",True,"PYTHON")
# #      0 1 2  3    4       5     6
# print(len(tpl))
# print(tpl.count("Python"))
# print(tpl[1])
# print(tpl[:6:2])

# # Exercise 2: The Trailing Comma
# tpl1 = (10,)   
# print(type(tpl1))
# tpl2 = (20)
# print(type(tpl2))

# # Exercise 3: Tuple Repetition
# tpl1 = (10,)
# print(tpl1*4)

# # Exercise 4: Tuple Concatenation
# tpl3 = (10,20,30,"Test",True)
# tpl4 = (40,50,60,"Tuple",False)
# print(tpl3+tpl4)

# Exercise 5: Tuple Slicing
# tpl5 = (40,50,60,"Tuple",False,2,1,0)
# print(tpl5[:8:2])

# Exercise 6: Tuple Reversal
# tpl6 = (40,50,60,"Tuple",False,2,1,0)
# print(tpl6[::-1])

# Exercise 7: Counting
# tpl7 = (40,50,60,"Tuple",False,2,1,0)
# print(len(tpl7))

# Exercise 8: Tuple Unpacking
tpl7 = (40,50,60,"Tuple",False,2,1,0)
tpl8 = (1,2,"Santanu")
tpl9 = (40,50,60,tpl8,"Tuple",False,2,1,0)
print(tpl9)
tpl10 = (40,50,60,*tpl8,"Tuple",False,2,1,0)
print(tpl10)
print(type(tpl10))

#2nd Method 
tpl8 = (40,50,60,"Tuple")
a,b,c,d = tpl8
print(a)
print(b)
print(c)
print(d)

# Exercise 9: The Swap Trick
# tpl9 = (40,50,60,"Tuple")
# tpl10 = (False,2,1,0)
# tpl9,tpl10=tpl10,tpl9
# print(tpl9)
# print(tpl10)

# Exercise 10: Nested Tuple Access
tpl11=((1, 2, 3), (4, 5, 6), (7, 8, 9))
tpl12= tpl11[1][1]
print(tpl12)

# Purpose: This exercise introduces you to the fundamental building blocks of working with tuples: creating them, retrieving individual elements using index positions, and measuring their size using len(). These are the first skills you need before working with any tuple-based data.