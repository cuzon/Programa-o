print("Digite um número pica: ")

a=float(input()) # int() pro computador entender que é um número, float() pro computador entender que é um número com virgula
print("Qual operação fodona que você quer?")
c=input()
print("Digite um número pica: ")
b=float(input())

c=c.lower()

if c=="ao quadrado":
    print(a**2)
    quit()
if c=="*":
    print(a*b) # print() pro computador mandar uma mensagem para mim e resolver a questão

elif c=="/": # else+if=elif. else = caso contrario, if = se (alternativa)
    print(a/b)
elif c=="+":
    print(a+b)
elif c=="-":
    print(a-b)
elif c=="elevado":
    print(a**b)