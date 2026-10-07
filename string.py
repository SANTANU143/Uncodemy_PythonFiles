#string method
# text = 'hello world'
# print(text.upper())
# print(text.replace('world','Python'))

#string formatting 
name = 'Santanu'
place = 'Midnapore'
country = 'India'
text1 = f"My Name is {name}"
text2 = f" I am from {place}"
text3 = text1.upper()
text4= text2.replace(text2, f" , I am from {country}")
for i in (text3+text4):
    print(i,end='-')

