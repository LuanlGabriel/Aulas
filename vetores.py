lista = ['banana', 'maça', 'kiwi']

print('essa é tua lista atual')
for i in lista:
    print(i)

print('\nagora adicione mais alguma coisa na lista')
lista.append(input('>>'))
print('agora essa é a sua lista atual\n')
for i in lista:
    print(i)