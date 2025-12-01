#commen strings methods  [.upper .lower .title .find(sub) .replace(old,new) .capitalizer]
str="saumya singh"
print(str.upper())
print(str.lower())
print(str.capitalize())
print(str.title())
print(str.find("my"))#to find index number
print(str.replace("singh" , "_1singh"))
print(str.count("s"))#find occurance

#formatted strings use "f" to use variables in "string" with help of {}
name= "saumya singh"
age =21
print(f"my name is {name} and i am {age} years old.")

#ESCAPE SEQUENCES
#\n new line    #\t tab space   #\\backslash    #\' single quote    #\" double quote
print("hello world")
print("hello\nworld")
print("hello\tworld")


