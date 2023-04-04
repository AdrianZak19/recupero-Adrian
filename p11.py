from random import randint
a=0
b=1
t=0
print('A     B')
print('-------')
while a!=b:
    a=randint(1,6)
    b=randint(1,6)
    t+=1
    
    print(a,' | ',b)
print('ci ha impiegato ',t,' tentativi')