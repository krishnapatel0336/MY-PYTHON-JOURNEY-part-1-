#LIST ==[built in data type which can stoe multiple values]    
food=["pizza", "idlie", "gulabjamun","choco waffle","apple" ]
        #[0]    #[1]----
# (can store diffrent types of data types)
print(food)

#methods in list
print(len(food))
#indexing
print("first value of list:",food[0])#pizza
#list are mutable
food[1]="orange"  #strings are imutable it can't be change
print(food)
print(food[1:3])
num=[3,4,2,1,5,7]
print(num.sort())
num.append(9)
print(num)
num.remove(4)
print(num)
num.pop(3)
print(num)
num.insert(3,10)
print(num)
print(max(num))
print(min(num))

