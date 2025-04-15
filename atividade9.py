import time
lista = ['gui', 'jão', 'xandão']
print(lista)
rem = 'jão'
if rem in lista:
    lista.remove(rem)
time.sleep(1)
print(lista)
time.sleep(1)
removido = lista.pop(1)
print(lista)
time.sleep(1)
print('item removido:',removido,'e',rem)
time.sleep(1)
lista += ['luan', 'kelvão']
for i, item in enumerate(lista):
    print(i, item)
lista.sort(reverse=True)
print(len(f'sua lista tem {lista} elementos'))