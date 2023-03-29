global nome
nome:str='a'
cognome:str='a'
o=int(input('inserire numero persone '))

def Lista():
    i=0
    l=[]
    for x in range(o):
        a=str(input('nome: '))
        b=str(input('cognome: '))
        l.append(a+ " " +b)
        if nome==a and cognome==b:
            i+=1

    return l, i

def main():
    lista=Lista()
    print(lista)
main()