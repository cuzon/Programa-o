a=float(input()) # int() pro computador entender que é um número, float() pro computador entender que é um número com virgula
c=input()
b=float(input())


if c=="*":
    print(a*b) # print() pro computador mandar uma mensagem para mim e resolver a questão

elif c=="/": # else+if=elif. else = caso contrario, if = se (alternativa)
    print(a/b)
elif c=="+":
    print(a+b)
elif c=="-":
    print(a-b)