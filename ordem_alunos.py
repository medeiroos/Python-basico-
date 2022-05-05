import random
pa = (input("Primeiro aluno:"))
sa = (input("Segundo aluno:"))
ta = (input("Terceiro aluno:"))
qa = (input("Quarto aluno:"))
lista = [pa, sa, ta, qa]
random.shuffle(lista)
print("A ordem de apresentação ficou assim")
print(lista)


