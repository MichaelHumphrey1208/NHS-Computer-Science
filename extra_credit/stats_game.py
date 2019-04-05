import random
spiner= random.randint(1,2)
if spiner == 1:
    d4one= random.randint(1,4)
    d4two= random.randint(1,4)
    d4three= random.randint(1,4)
    total = d4one + d4two + d4three
    print(d4one)
    print(d4two)
    print(d4three)
    print(total)

    print(spiner)
else:
    d6one= random.randint(1,6)
    d6two= random.randint(1,6)
    d6three= random.randint(1,6)
    total = d6one + d6two + d6three
    print(d6one)
    print(d6two)
    print(d6three)
    print(total)
    print(spiner)
teir1=0
teir2=0
teir3=0
for d4one in range(1,5):
    for d4two in range(1,5):
        for d4three in range(1,5):
            print(d4one,d4two,d4three)
            total4 = d4one + d4two + d4three
            print(total4)
print("d6 combinations")
for d6one in range(1,7):
    for d6two in range(1,7):
        for d6three in range(1,7):
            print(d6one,d6two,d6three)
            total6 = d6one + d6two + d6three
            if total6 ==10:
                teir1 +=1
                print(teir1)
                print("ten")
            elif total6 ==12:
                teir2 +=1
            elif total6 ==16 or total6 ==17 or total6 ==18:
                teir3 +=1
            print(total6)
print(teir1)
print(teir2)
print(teir3/2)
