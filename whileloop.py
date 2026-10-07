# Exercise 1: Print first 10 natural numbers using while loop
# i = 1
# while i<=10:
#     print(i,end=" ")
#     i+=1

# Exercise 2: Calculate sum of all numbers from 1 to a given number
# num = int(input("Enter the number: "))
# i= 1
# sum = 0
# while i<=num:
#     sum = sum +i
#     i+=1
# print("Sum is -->",sum)

# Exercise 3: Print multiplication table of a given number
# num = int(input("Enter the number : "))
# i = 1
# j=10
# while i<=j:
#     print(i,"X",num,"=",i*num)
#     i+=1


# Exercise 4: Count the total number of digits in a number
num = int(input("Enter the number: "))
count = 0
while num != 0:
    num = num // 10
    count += 1
print(count)