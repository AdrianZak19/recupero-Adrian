from random import randint
a=randint(1,6)
a1=randint(1,6)
b=randint(1,6)
b1=randint(1,6)
sA=1
sB=1


while a!=a1:
    a=randint(1,6)
    a1=randint(1,6)
    print(str(sA)+'°','A:',a,a1)
    sA=sA+1
print(str(sA)+'°','A:',b,b1)
while b!=b1:
    b=randint(1,6)
    b1=randint(1,6)
    print(str(sB)+'°','B:',a,a1)
    sB=sB+1
print(str(sB)+'°','B:',b,b1)

if sA<sB:
    print('la squadra A ha vinto con ',sA,' tentativi')
else:
    print('la squadra B ha vinto con ',sB,' tentativi')