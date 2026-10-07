# class A:
#     a= 10
#     def b(self):
#         print("Python")
# # print(A.a)
# # A.b()

# #=========
# obj = A()
# print(obj.a)
# obj.b()

#=========================== Constractor ================
# class A:
#     a = 50
#     def __init__(self,b,c):
#         print("Value of B is ", b)
#         self.c = c
#     def number(self):
#         print(f"value of c is {self.c}")
# obj = A(100,200)
# obj.number()

#============================= Polymorphism ================
#Example 1:
# class Cat:
#     def speak (self):
#         print("Meow")
# class Dog:
#     def speak(self):
#         print("Woof")
# animals = [Cat(),Dog()]
# for animal in animals:
#     animal.speak()
#========================== Inheritance =============================
# #Example 1:
# class A:
#     a = 20
# class B(A):
#     b = 30
# class C(B):
#     c = 40

# obj = C()
# print(obj.a)
# print(obj.b)
# print(obj.c)
# #===========================Method OverRidding  ================
# class A:


#======================== Abstraction =================

from abc import ABC, abstractmethod
class Animal (ABC):
    @abstractmethod
    def speak(self):
        pass
class Dog(Animal):
    def speak(self):
        print("woof")
dog = Dog()
dog.speak()

    
