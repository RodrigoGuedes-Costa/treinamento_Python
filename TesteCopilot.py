class Cliente:
    def __init__(self, nome, tipo):
        self.nome = nome
        self.tipo = tipo

class Bagagem:
    def __init__(self, peso):
        self.peso = peso

class CompanhiaAerea:
    def __init__(self):
        self.clientes = []

    def adicionar_cliente(self, cliente):
        self.clientes.append(cliente)

    def verificar_bagagem(self, cliente, bagagem):
        if cliente.tipo == "premium" and bagagem.peso <= 32:
            return "Bagagem despachada sem custo adicional."
        elif cliente.tipo == "gold" and bagagem.peso <= 28:
            return "Bagagem despachada sem custo adicional."
        else:
            return "Bagagem sujeita a cobrança."

# Exemplo de uso
companhia = CompanhiaAerea()

cliente1 = Cliente("Alice", "premium")
cliente2 = Cliente("Bob", "gold")
cliente3 = Cliente("Charlie", "comum")

companhia.adicionar_cliente(cliente1)
companhia.adicionar_cliente(cliente2)
companhia.adicionar_cliente(cliente3)

# Solicitar o peso da bagagem ao usuário
peso_bagagem1 = float(input("Digite o peso da bagagem do cliente Alice: "))
peso_bagagem2 = float(input("Digite o peso da bagagem do cliente Bob: "))
peso_bagagem3 = float(input("Digite o peso da bagagem do cliente Charlie: "))

bagagem1 = Bagagem(peso_bagagem1)
bagagem2 = Bagagem(peso_bagagem2)
bagagem3 = Bagagem(peso_bagagem3)

print(companhia.verificar_bagagem(cliente1, bagagem1))  # Bagagem despachada sem custo adicional.
print(companhia.verificar_bagagem(cliente2, bagagem2))  # Bagagem despachada sem custo adicional.
print(companhia.verificar_bagagem(cliente3, bagagem3))  # Bagagem sujeita a cobrança.
