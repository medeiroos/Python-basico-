from random import choice
pa = str(input("Primeiro aluno:"))
sa = str(input("Segundo aluno:"))
ta = str(input("Terceiro aluno:"))
qa = str(input("Quarto Aluno:"))
lista = [pa, sa, ta, qa]
escolhido = choice(lista)
print("O aluno escolhido foi o {}".format(escolhido))


