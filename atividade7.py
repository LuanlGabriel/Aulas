lista = []
while True:
    x = input('>>')
    if x == 'fim':
        break
    lista.append(x)
    print(f'a lista tem {len(lista)} item')