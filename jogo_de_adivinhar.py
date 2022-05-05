import random
desafio = int(input("Pensei em um numero de 1 a 5, tente acerta-lo. "))
numero = int(5 * random.random())
n2 = numero * 1
resultado= n2
if desafio == n2:
    print("Parabéns você acertou, o numero que eu pensei foi {:.0f}.".format(n2))
else:
    print("Você errou, o numero que eu pensei foi {:.0f}.".format(n2))

