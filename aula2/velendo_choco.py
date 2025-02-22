print("Digite uma palavra:")
palavra = str(input()).lower().strip().replace('','')
if palavra == palavra[::-1]:
    print('É palíndromo')
else:
    print('Não é palíndromo')


