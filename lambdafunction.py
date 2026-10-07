# WAP to define a function for sum, difference, multiplication and division

# sum_num = lambda x,y:print(x+y)
# mul_num = lambda a,b:print(a*b)
# div_num = lambda c,d:print(c/d)

# sum_num(10,20)
# mul_num(5,6)
# div_num(200,10)

# ======================
# Write a Python program to sort tuples using Lambda.
#----------------- Without Lambda Function --------------
mytuple = (1,2,3,4,5,6,7,8,9,10)
mylist3 = list(mytuple)
sort_tuple = sorted(mylist3)
print(sort_tuple)

#=============== with Lambda Function ================
my_new_tpl = (1,2,3,4,5,6,7,8,9,10)


# # Write a Python program to square and cube every number in a given list of integers using Lambda
# mylist = [1,2,3,4]
# squar_num = list(map(lambda x: x**2, mylist))
# cube_num =  list(map(lambda x: x**3, mylist))
# print(squar_num)
# print(cube_num)

# # Write a Python program to count the even and odd numbers in a given list of integers using Lambda.
# mylist = [10,11,12,13,14,15,16,17,21,20]
# even_num = list(filter(lambda x: x%2==0, mylist))
# odd_num =  list(filter(lambda x: x%2 !=0, mylist))
# print(even_num)
# print(len(even_num))
# print(odd_num)
# print(len(odd_num))

# # Write a Python program to add two given lists using map and lambda.
# mylist1 = [10,11,12,13,14]
# mylist2 = [15,16,17,21,20]
# added_list = list(map(lambda x,y :x+y,mylist1,mylist2))
# print(added_list)