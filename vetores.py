#semelhante a uma fila de espera, os elemntos em uma lista python tem uma ordem especifica e podem ser acessados por sua posição
lista = ['banana', 'maça', 'kiwi']

for i in lista:
    print(i)
print('essa é tua lista atual logo a cima')

lista.append(input('\n>>'))
for i in lista:
    print(i)
print('agora essa é a sua lista atual')