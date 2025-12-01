#implicit 
x=20 #int
y=("type here") #str
z=5.5 #float

#explicit 
#que 1
#take number input convert it into float
#eg1
y=int(x)
z=float(y)
print("coversion:", z)
print(type (z))
#eg2

num=int(input("enter a value:"))
convertedvalue = float(num)
print("original value is", num, "datatype:", type(num))
print ("convertable value is", convertedvalue, "datatype :", type(convertedvalue))
