from time import sleep
print("-=-" * 15)
print("          ANALISADOR DE TRIANGULOS!")
print("-=-" * 15)
ps = float(input("Primeiro segmento:"))
ss = float(input("Segundo segmento:"))
ts = float(input("Terceiro segmento:"))
print("ANALISANDO...")
sleep(2)
if ps < ss + ts and ss < ps + ts and ts < ps + ss:
    print("Os segmentos acima PODEM formar triangulos")
else:
    print("Os segmentos acima NÃO PODEM formar triangulos")

