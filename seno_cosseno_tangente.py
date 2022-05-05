import math
an = float(input("Digite o ângulo que você deseja:"))
se = math.sin(math.radians(an))
co = math.cos(math.radians(an))
ta = math.tan(math.radians(an))
print("O ângulo de {} tem o seno de {:.2f}".format(an, se))
print("O ângulo de {} tem o cosseno de {:.2f}".format(an, co))
print("O ângulo de {} tem a tangente de {:.2f}".format(an, ta))
