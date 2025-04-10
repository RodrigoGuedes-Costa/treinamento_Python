print("Quilão do Andrezão")
preco_quilo = float(input("Informe o valor cobrado por quilo! "))
peso_prato = float(input("Informe o peso do prato do cliente (em kg) "))
preco_prato = preco_quilo * peso_prato
print(f"O valor do prato é R${preco_prato:.2f}")
#O desvio abaixo testa se o peso do prato ultrapassa 1kg e exibe a mensagem apenas
#caso o resultado do teste seja verdadeiro
if peso_prato >= 1:
    print("O prato excedeu 1kg. O cliente pode pagar R$80,00 e consumir à vontade")