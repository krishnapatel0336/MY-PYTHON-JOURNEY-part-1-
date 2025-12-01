#slicing{part of string}:                         #end index excluded but if lowerremoval is blank then [include} 
#generalcase{[a:b or  :b)}but exeption{[a: ]}     #first blank means it's zero
str="saumyadii"
firsthalf= str[0:6]#saumya
upperremoval= str[ :5]#saumy
lowerremoval= str[2: ]#umyadii
print(firsthalf)
print(upperremoval)
print(lowerremoval)

#CONCEPT OF NEGATIVE INDEXING                       #START WITH (-n,-1]

#que 2:      middle 3 and last 2 characters
#M-1
str1="green"
middle3= str1[1:4]
print(middle3)   
last2= str1[3: ]
print(last2)
#M-2[general]
str2= input("Enter value: ")
mid= len(str2)//2 #'//' is devide with removal of remender
output1= str2[mid-1:mid+2]
print(output1)
output2= str2[-2:]
print(output2)







