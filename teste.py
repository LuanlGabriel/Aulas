itens = []

while True:
    itens.append(input('>>'))
    if itens == ['fim']:
        break
    else:
        print(f'a lista tem {len(itens)} item')