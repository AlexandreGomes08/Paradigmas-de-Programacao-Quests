msg = open("mensagem.txt","r")
arq = list(msg.read())
comentario = []

b = 0
a = 2
while(a <= len(arq)):
    if arq[a-1] == "*" and arq[a-2]=="/":
        cont = 0

        while(arq[a+1]!="/" and arq[a]!="*"):
            cont = cont+1
            comentario.append(arq[a])
            a=a+1

            if((a+1) == len(arq)):
                j = a-cont
                while(a != j):
                    item = comentario.pop(-1)
                    a=a-1
                break
        comentario.append("\n")
    a=a+1

while(b < len(comentario)):
    print(comentario[b],sep="",end="")
    b=b+1