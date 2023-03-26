def func1():
    def foo():
        L = []
        def bar():
            L.append(5)
        bar()
        return L
    foo()

def func2():
    def foo():
        def bar():
            L.append(5)
        L = []
        bar()
        return L
    foo()

def func3():
    def foo():
        L = []
        bar()
        return L
    def bar():
        L.append(5)
    foo()

def tent():
    try:
        print("Executando...")
        func1()
        print("Sucesso da função 1")
    except Exception as erro:
        print("Falha da função 1 ",erro,sep="")
    try:
        print("\nExecutando próxima função...")
        func2()
        print("Sucesso da função 2")
    except Exception as erro:
        print("Falha da função 2 ",erro,sep="")
    try:
        print("\nExecutando próxima função...")
        func3()
        print("Sucesso da função 3")
    except Exception as erro:
        print("Falha da função 3 ",erro,sep="")    
tent()
