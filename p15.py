from random import randint
i=0
l=[]
while i<10:
    i=0
    for x in range(1):
        a=randint(1,100)
        if a>50:
            
            l.append(a)
            print(a)
            i=i+1
    
print(l)
print(i,' tentativi')