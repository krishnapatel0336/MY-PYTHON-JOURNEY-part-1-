#range in fore loop
#range(start(0), stop, jump{step}(1))

for newitem in range(1,20,3):
    print(newitem)

#practice que 8
for i in range(2,21,2):
    print("table of two", i)
   
#break/loop breakdown
for n in range(1,5):
    if n==6:
        break
#continue/bump  that value
    elif n==2:
        continue
    print(n)
#pass/loop can't be blank so do no write code than use pass
for a in range(1,9):
    pass
  