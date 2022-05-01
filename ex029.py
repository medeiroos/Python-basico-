from time import sleep
velo = int(input("Qual a velocidade atual do carro?"))
print("RADAR!!!")
sleep(2)
if velo <=80:
    print("Tenha um Bom dia, e dirija com segurança")
else:
    multa = (velo-80) * 7
    print("Você,foi multado por não estar no limite da via que é de '60Km/h'.\n Sua multa foi R${:.2f}.".format(multa))