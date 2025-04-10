#Na programação,esse mecanismo é chamado de chave-valor, onde a chave é um identificador único e o valor é o dado que estamos associando a essa chave
#Uma  das  grandes  vantagens dessa estrutura  é  que  podemos  recuperar  um determinado  valor  sem  ter  que  percorrer  o  dicionário  inteiro,  bastando  saber  a  sua chave.  Para  compreendermos  melhor,  vamos  criar  um  dicionário  com   alguns elementos e exibi-lo:
dicionario = {
    "nome": "Star Wars - Episódio IV - Uma nova esperança",
    "diretor": "George Lucas",
    "lançamento": 1977,
    "bilheteria": 775000000.00
}
print(dicionario)
print(f"O valor da chave nome é {dicionario['nome']}")

#vamos   criar   exemplos   separados   para compreendê-los  por  grupos,  sendo  os  primeiros:.values(),  .keys()e.items() os métodos que retornam estruturas iteráveis
dicionario = {
    "nome": "Star Wars - Episódio IV - Uma nova esperança",
    "diretor": "George Lucas",
    "lançamento": 1977,
    "bilheteria": 775000000.00
}
print(f"O método .keys() retorna \n{dicionario.keys()}")
print("Se percorrermos a lista retornada com um loop for teremos: ")
for chave in dicionario.keys():
    print(chave)
print(f"\nO método .values() retorna \n{dicionario.values()}")
print("Se percorrermos a lista retornada com um loop for teremos: ")
for valor in dicionario.values():
    print(valor)
print(f"\nO método .items() retorna \n{dicionario.items()}")
print("Como foi retornada uma lista de tuplas e as tuplas podem ser desempacotadas, teremos: ")
for chave, valor in dicionario.items():
    print(f"{chave} -- {valor}")
#Viu  como  foi  bom  ter  estudado  as  tuplas  e  as  listas  antes?  O  dicionário  nos retorna  alguns  dados  no  formato  dessas  estruturase  podemos  aplicar  as  mesmas técnicas de iteração que utilizávamos com elas

#Agora  é  hora  de  testarmos  os  métodos  que  retornam  valores,  como  .get()  e .setdefault(), e que retornam um dicionário inteiro, como o .copy():
#É possível perceber que o método .setdefault() é muito útil para as situações em que precisamos verificar o valor de uma chave e criá-la caso não exista.
dicionario = {
    "nome": "Star Wars - Episódio IV - Uma nova esperança",
    "diretor": "George Lucas",
    "lançamento": 1977,
    "bilheteria": 775000000.00
}
print(f"O método .get() para a chave diretor retorna \n{dicionario.get('diretor')}")
print(f"O método .get() para a chave publico (que não existe) retorna \n{dicionario.get('publico')}")
print(f"\nO método .setdefault() para a chave diretor retorna \n{dicionario.setdefault('diretor')}")
dicionario.setdefault("publico")
print(f"O método .setdefault() para a chave publico (que não existe) cria a chave e coloca o valor None. Veja como ficou nosso dicionário depois de utilizar este método: \n{dicionario}")
dicionario.setdefault("custo", 11000000.0)
print(f"Caso utilizemos o método .setdefault() para a chave custo (que não existe) e também passarmos um valor como argumento, a chave será criada com este valor. Veja como ficou nosso dicionário depois de utilizar este método: \n{dicionario}")
print(f"\nO método .copy() retorna a seguinte cópia do dicionário que, se for alterada, não impacta no dicionário original: {dicionario.copy()}")

#Quando  a  nossa  intenção,  porém,  é  apenas a de  modificar  o  dicionário, podemos utilizar os métodos .update(), .pop(), .popitem() e .clear():
dicionario = {
    "nome": "Star Wars - Episódio IV - Uma nova esperança",
    "diretor": "George Lucas",
    "lançamento": 1977,
    "bilheteria": 775000000.00
}
dicionario.update({"custo": 50.0})
print(f"O método .update() com a chave custo (que não existia) e o valor 50.0 nos deixa com o seguinte dicionário \n{dicionario}")
dicionario.update({"custo": 11000000.0})
print(f"O método .update() com a chave custo (que já existe após a mudança anterior) e o valor 11000000.0 nos deixa com o seguinte dicionário \n{dicionario}")
dicionario.pop("diretor")
print(f"\nO método .pop() para a chave diretor nos deixa com o seguinte dicionário \n{dicionario}")
dicionario.popitem()
print(f"\nO método .popitem() nos deixa com o seguinte dicionário \n{dicionario}")
dicionario.clear()
print(f"\nO método .clear() nos deixa com o seguinte dicionário \n{dicionario}")

#o  método  .fromkeys(),que  é usado para gerar um dicionário com um conjunto de chaves e o mesmo valor para todas. Esse método não é usado para extrair dados de um dicionário existente, mas,sim,para gerar um novo.
notas = dict.fromkeys(("Matemática", "Física", "Química"))
print(f"O dicionário gerado com o método fromkeys para a tupla de chaves (Matemática, Física, Química) e sem valor foi: \n{notas}")
notas = dict.fromkeys(("Matemática", "Física", "Química"), [])
print(f"\nO dicionário gerado com o método fromkeys para a tupla de chaves (Matemática, Física, Química) e valor zero foi: \n{notas}")