nome = str(input("Digite um nome:")).strip()
print("Seu nome em letras maiúsculas é {}".format(nome.upper()))
print("Seu nome em letras minúsculas é {}".format(nome.lower()))
print("Seu nome tem {} letras".format(len(nome)-nome.count(" ")))
print("Seu primeiro nome tem {} letras".format(nome.find(" ")))
