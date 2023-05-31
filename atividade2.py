#Objetivo: Criar um programa que printe os numeros de uma lista e, depois, eles multiplicados por 2
#Bonus: Colocar os numeros multiplicados em uma outra lista e printa-la


lista = [2, 3, 7, 12, 2]
multiplicar = []
for number in lista:
    print(number)
    multiplicar.append(number * 2)
print("number multiplicar por 2:")
for number in multiplicar:
    print(number)