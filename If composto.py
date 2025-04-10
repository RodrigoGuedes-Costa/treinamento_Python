print("Saldão da alegria!")
total_compra = float(input("Por favor, informe o valor total da compra do cliente "))
forma_pagamento = int(input("Selecione a forma de pagamento: 1 - Boleto ou 2 - Cartão "))
if forma_pagamento == 1:
    total_compra_desconto = total_compra * 0.95
    print(f"O total da compra de R${total_compra:.2f} sofreu um desconto pelo pagamento em boleto. O cliente deverá pagar R${total_compra_desconto:.2f}.")
else:
    parcelas = int(input("Informe a quantidade de parcelas desejadas (entre 1 e 12)"))
    valor_parcela = total_compra / parcelas
    print(f"O total da compra de R${total_compra:.2f} será pago em {parcelas} parcelas de R${valor_parcela:.2f}.")