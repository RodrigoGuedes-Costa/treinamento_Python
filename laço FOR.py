#for valor in range(10, 100, 2):#primeiro numero é o qual vai começar, segundo é até onde vai excludente(99) e o ultimo de quanto em quanto.
 #print(f"Nesta volta o conteúdo da variável valor é {valor}")

numero = int(input("digite um numero: "))
meu_numero = numero

for valor in range(10, meu_numero, 2):
 print(f"Nesta volta o conteúdo da variável valor é {valor}")
 if valor == meu_numero:
    break