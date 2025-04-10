calorias = []
resposta = ""
while resposta.upper() != "NÃO":
    caloria = int(input("Por favor, informe a quantidade de calorias consumida nesta refeição: "))
    calorias.append(caloria)
    resposta = input("Digite SIM para informar mais uma caloria ou NÃO para encerrar a digitação")
total = 0
print("As calorias informadas para este dia foram: ")
for caloria in calorias:
    total = total + caloria
    print(caloria)
media = total / len(calorias)
print(f"Ao longo do dia foram consumidas {total} calorias, com uma média de {media:.2f} calorias por refeição")