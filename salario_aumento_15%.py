sal = float(input('qual o salario do funcionario: R$'))
aum = sal + (sal * 15 / 100)
print('um funcionario que ganhava R${:.2f}, com o aumento 15%, passa a receber R${:.2f}'.format(sal, aum))


