# a = 100
# b = 200
# if a>=b:
#     print("A is big ")
# else:
#     print("B is big ")

#======================

# a= 21
# if (a >=18):
#     print("a is eligible for voting ")
#     if (a>=21):
#         print("a also eligibe for participation")

#=====================
#Q3. WAP to check the eligibility criteria for voting & participating in election 
age= int(input("enter the age: "))
# if age>=18:
#     print("This age is eligible for voating")
if age>=18 and age<=21:
    print("This age is not eligible for participation, Only eligible for voating")
elif age>=18 or age>=21:
    print("This age is eligible for voating and participation")
else:
    print("Not eligible for voting or perticipation")