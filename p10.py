from random import randint
a=int(0)
tentativi=0
while a!=6:
    a=randint(1,6)
    tentativi=tentativi+1
    print(a)

print("ci ha impieagato ",tentativi,' tentativi')