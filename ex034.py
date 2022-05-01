sal = float(input("Qual é o salario do funcionario? R$"))
aum = sal + (sal * 15 / 100 )
aum2 = sal + (sal * 10 / 100)
if aum <= 1250:
    print("Quem ganhava R${:.2f} passa a ganhar R${:.2f}".format(sal, aum))
if aum2 >= 1250:
    print("Quem ganhava R${:.2f} passa a ganhar R${:.2f}".format(sal, aum2))