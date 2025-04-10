inimigos = [(10, 15), (30, 30)]

while inimigos!=[]:
    for x, y in inimigos:
        print(f"O inimigo está na posição X={x} e Y={y}")
    x = int(input("Digite a posição X do inimigo que deseja acertar: "))
    y = int(input("Digite a posição Y do inimigo que deseja acertar: "))
    if (x, y) in inimigos:
        print("ACERTOU!!")
        inimigos.remove((x, y))
    else:
        print("Não foi encontrado nenhum inimigo na posição indicada ")
    print(f"Os inimigos ainda existentes são: {inimigos}")
print("Você eliminou todos,não existem mais inimigos!!!")