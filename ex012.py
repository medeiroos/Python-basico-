prod = float(input('Valor do produto? R$'))
desc = (prod * 5 / 100 )
valor = prod-desc
print('O produto custa R${:.2f} e com o desconto de 5% aplicado, saiara por R${:.2f}.'.format(prod, valor))
