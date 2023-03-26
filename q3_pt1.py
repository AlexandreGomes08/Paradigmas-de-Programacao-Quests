p = input("Digite uma palavra:")
plist = list(p)
a = 1
b = 0
alf = ['a','b'] 

def automato(plist) :
    i = 0
    b = 0
    while(b < len(plist)):
        if plist[b] == "a":
            if i==0:
                i=1
            elif i==1:
                i=3
            elif i==2:
                i=1
            elif i==3:
                i=3
        else:
            if i==0:
                i=2
            elif i==1:
                i=2
            elif i==2:
                i=3
            elif i==3:
                i=3
        b=b+1
    if i == 3:
        print("Palavra reconhecida")
    else:
        print("Palavra não reconhecida")

while b < len(plist):
    if(plist[b] not in alf):
        a = 0
    b=b+1

if a == 1:
    automato(plist)
else:
    print("Valor inválido")



