a=1
for a in range (100):
    a+=1
    if a%7==0:
        continue
    elif (a-7)%10==0 or a//10==7:
        continue
    print(a)
