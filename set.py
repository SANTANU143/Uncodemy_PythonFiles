# Exercise 1: Basic Set Operations
a = {1,11,0.00,"Uncodemy",True,False}
# #By Default True = 1 so if 1 if define separately then True will replace 1 as the default value 
# # Fale = 0
# print(a) 
# a.add(12)
# print(a)
# a.discard("Uncodemy")
# print(a)
# a.remove(False)
# print(a)


# #Exercise 2: Clear All Elements
# a.clear()
# print(a)

# # Exercise 3: Find the Length of a Set
# b= {1,11,0.00,"Uncodemy",True,False}
# print(len(a))
# print(len(b))

# Exercise 4: Check if a Set is Empty
# c = set()
# if len(c) == 0:
#     print("Set is empty")

# Exercise 5: Union of Sets
# d= {1,11,0.00,"Uncodemy",True,False}
# e= {3,12,0.01,"Uncodemy",True,500,700,-1000}
# union_of_set = d|e
# print(union_of_set)
# Exercise 6: Intersection of Sets
# f= {1,11,0.00,"Uncodemy",True,False}
# g= {3,12,0.01,"Uncodemy",True,500,700,-1000}
# intersection_of_set = f&g
# print(intersection_of_set)

# Exercise 7: Difference of Sets
# i= {1,11,0.00,"Uncodemy",True,False,-500,-600,-700}
# j= {3,12,0.01,"Uncodemy",True,500,700,-1000}
# diff_of_set = i-j
# print(diff_of_set)

# Exercise 8: Symmetric Difference
k= {1,11,0.00,500,-600,700}
l= {3,12,0.01,500,700,-1000}
symmetric_diff = k.symmetric_difference(l)
print(symmetric_diff)

# # Exercise 9: Find Max and Min
# i= {1,11,0.00,-500,-600,-700}
# j= {3,12,0.01,500,700,-1000}
# print(max(i))
# print(min(j))


# Exercise 10: Sum of Set Elements
# i= {1,11,0.00,-500,-600,-700}
# j= {3,12,0.01,500,700,-1000}
# print(sum(i))
