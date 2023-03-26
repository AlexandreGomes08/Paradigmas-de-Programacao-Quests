n = input("Digite um número: ")
nlist = list(n)
nval = ['1','2','3','4','5','6','7','8','9','0',',']
verif = 1

c = 0
while(c < len(nlist)):
    if(nlist[c] not in nval):
        verif = 0
    c=c+1

if(verif == 0):
    print("Valor inválido")
else:
    if("," in nlist):
        print("número informado é tipo flutuante")
    else:
        print("número informado é tipo inteiro") 
    
