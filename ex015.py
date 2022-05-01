dia = int(input("Quantos dias alugados?"))
km = float(input("Quantos KM rodados?"))
rdia = dia * 60
rkm = km * 0.15
rkmd = rdia + rkm
print("O total a pagar é de R${:.2f}.".format(rkmd))


