from random import randint
from time import sleep
computador = randint(0, 5) #FAZ O COMPUTADOR SORTEAR UM NUMERO
print("-=-" * 20)
print("       Pensei em um numero de 0 a 5, tente adivinhar")
print("-=-" * 20)
jogador = int(input("Em que numero pensei?")) #JOGADOR TENTA ADIVINHAR
print("PROCESSANDO...")
sleep(2)
if jogador == computador:
    print("Parabéns você acertou eu pensei no numero {}, e me venceu!!!.".format(computador))
else:
    print("Você perdeu, eu pensei no numero {} e não no {}.".format(computador, jogador))
