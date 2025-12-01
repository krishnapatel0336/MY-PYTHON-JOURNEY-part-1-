#f(x) calling with no argumenets (xyz)
def avg(a,b):
    avg1=(a+b)/2
    print(avg1)
avg(1,2)
avg(2,4) #set defalt value to avoid value when u put no argument
#print age
def display_age(name="divya",age=18):
    print(f"{name} is {age} years old")
display_age("saumyadii",25)
display_age()
#print food
def fav_food(food="gulaabjamun"):
    print(f"saumya loves {food}")
fav_food()
fav_food("rasmalai")
#return statment
def multiply(a=5,b=6):
    return a*b
print(multiply(10,4))
result=multiply(5,5)
print(result)
#prctice1.
#write f(x)=x*2
def square(num=5):
    return num**2 
print(square(4))
#practice2.
# write f(x)that takes string and returncount of vowels and consonents seperately
def f(userinput):
    vowels="aeiouAEIOU"
    countvowel=0
    countconsonent=0
    for eachchar in userinput:
        if(eachchar.isalpha):
            if(eachchar in vowels):
                countvowel+=1
            else:
                countconsonent+=1
    return countvowel, countconsonent
v,c=f("saumyadii")
print(v,c)




    