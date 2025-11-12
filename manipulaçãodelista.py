numeros = []
numeros.append(1)
numeros.append(2)
numeros.append(3)
numeros.append(4)
numeros.append(5)
print(numeros)  # [1, 2, 3, 4, 5]
#2
lista = [10, 20, 30]
lista.insert(1, 15)
print(lista)  # [10, 15, 20, 30]
#3
lista = ['a', 'b', 'c']
lista[1] = 'x'
print(lista)
#4
lista = [5, 10, 15, 20]
del lista[2]
print(lista)
#5
lista = ['maçã', 'banana', 'laranja']
lista.remove('banana')
print(lista)
#6
lista = [100, 200, 300, 400]
ultimo = lista.pop()
print(lista)
print("Removido:", ultimo)
#7lista = ['python', 'java', 'c++']
removido = lista.pop(1)
print(lista)
print("Removido:", removido)
#8
lista = [1, 2, 3, 4, 5]
lista.clear()
print(lista)
#9
lista = ['a', 'b', 'd']
lista.insert(2, 'c')
lista.remove('a')
print(lista)
#10
lista = [10, 20, 30, 40, 50]
lista.append(60)
lista.insert(1, 15)
lista.remove(30)
ultimo = lista.pop()
print(lista)
print("Removido:", ultimo)
