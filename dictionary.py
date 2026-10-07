# # Exercise 1: Basic Dictionary Operations
# mydict = {
#   "brand": "BMW",
#   "model": "Altroz AMT",
#   "year": 2018
# }
# mydict["year"] = 2026
# mydict.update({"brand":"TATA"})
# print(mydict)
# print(mydict.keys())
# print(mydict.values())
# mydict1 = mydict.copy()
# print(mydict.pop("model"))
# print(mydict)
# print(mydict.popitem())
# print(mydict)


# Exercise 2: Dictionary Operations

# Exercise 3: Dictionary from Two Lists
# L1 = ["Name", "Age", "Place","EmpNo"]
# L2 = ["Santanu","30","Kolkata","1234"]
# myDict = dict(zip(L1,L2))
# print(myDict)

# # Exercise 4: Clear Dictionary
# myDict.clear()
# print(myDict)

# Exercise 5: Merge Dictionaries
# dict1 = {"name": "Santanu", "age": 32}
# dict2 = {"age": 35, "city": "Kolkata"}
# dict1.update(dict2)
# print(dict1)

# #Alternet method 
# mar_dict= dict1 | dict2
# print(mar_dict)

# Exercise 6: Access Nested Dictionary
# person = {"name": "Carol", "address": {"city": "Paris", "zip": "75001"}}
# print(person["address"]["zip"])


# Exercise 7: Access ‘history’ Key From a Nested Dictionary
# student = {"name": "Dave", "grades": {"math": 88, "science": 92, "history": 75}}
# print(student["grades"]["history"])

# #Assigning value to the specific key
# student["grades"]["math"] = 99
# print(student)

# Exercise 8: Initialize Dictionary with Default Values
# keys = ["Age1", "Age2","Age3"]
# #default_value = 50
# m_dict = {}
# #m_dict = dict.fromkeys(keys,default_value)  #method returns a dictionary with the specified keys and the specified value.
# print(m_dict)
# m_dict.setdefault("Age2", 25)   # method returns the value of the item with the specified key.If the key does not exist, insert the key, with the specified value.
# print(m_dict)


# Exercise 9: Rename a Key of Dictionary
# dict1 = {"name": "Santanu", "age": 32}
# dict1["Full Name"] = dict1["name"]
# print("Before deleting the Name key : ",dict1)
# del dict1["name"]
# print("After deleting the Name key : ",dict1)

#===============2nd process ===========
# dict2 = {"age": 35, "city": "Kolkata"}
# dict2["Place"] = dict2.pop("city")
# print(dict2)


# Exercise 10: Delete a List of Keys
dict4 = {"Name": "Santanu", "age": 35, "city": "Kolkata","Country" :"India"}
keys_dict4 = ["Name","city"]
for key in keys_dict4:
    del dict4[key]
print(dict4)
