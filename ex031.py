viagem = int(input("Qual é a distância da sua viagem(KM)?"))
viagemc = viagem * 0.50
viageml = viagem * 0.45
if viagem <= 200:
    print("Você esta prestes a começar uma viagem de {}.".format(viagem))
    print("E o preço da sua passagem será de R${:.2f}.".format(viagemc))
else:
    print("Você esta prestes a começar uma viagem de {}.".format(viagem))
    print("E o preço da sua passagem será de R${:.2f}.".format(viageml))
