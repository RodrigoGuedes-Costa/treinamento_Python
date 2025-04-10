numero = int(input("Informe o número do qual deseja obter o fatorial: "))
fat = numero

for valor in range(1, numero, 1):
 fat = fat * valor
print(f"O fatorial do número informado é: {fat} ")
#exemplo com 4 : fat recebeu do numero o valor digitado 4, no for na primeira volta vai ser 4*1 pq o loop está para
#contar de 1 em 1(fica o fat = 4), na segunda volta  fat = 8 (4*2),na terceira e ultima pq o valor digitado é excludente
#o valor de fat = 24(8*3)