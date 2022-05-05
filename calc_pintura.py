larg = float(input('Qual a largura da sua parede:'))
alt = float(input('Qual a altura:'))
area= larg * alt
tinta = area / 2
print('Sua parede tem a dimensão de {}x{} e sua área é de {:.3}m².\nEntão você precisara de {:.3}L, para poder pintar a parede.'.format(larg, alt, area, tinta))



