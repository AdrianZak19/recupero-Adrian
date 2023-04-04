from random import randint
i=0
for x in range(10):
    a=randint(1,100)

    if a>50:
        print(a)
        i=i+1
print(i,' numeri sono piu grandi di 50')