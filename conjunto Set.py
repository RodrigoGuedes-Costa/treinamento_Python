#A principal diferença do set para a lista é que o set não mostra elementos repetidos
conjunto = set() #cria um set vazio
conjunto.add("Cebolinha")
conjunto.add("Cascão")
conjunto.add("Mônica")
conjunto.add("Cebolinha")
print(f"O conteúdo do set que foi recebendo elementos com o método add() é \n{conjunto}") #Note que não existe repetição de elementos
lista = ["Cebolinha", "Cascão", "Mônica", "Magali", "Cebolinha"]
novo_conjunto = set(lista)
print(f"\nPodemos criar um set a partir de uma lista de um outro set ou de qualquer estrutura iterável. A lista é \n{lista}")
print(f"O conteúdo do set construído a partir da lista é \n{novo_conjunto}") #Note que não existe repetição de elementos
print("\n")
#Existem  ainda  métodos  que podem  atualizar  os  elementos  de  um  set  com base  nos  elementos  presentes  em  um  segundo  set,  como:.difference_update(), .intersection_update() e .symmetric_difference_update():
conjunto1 = {"Mega Drive", "Super Nintendo", "Playstation"}
conjunto2 = {"Playstation", "Nintendo 64", "Sega Saturn", "Dreamcast"}
print(f"O primeiro set contém {conjunto1}")
print(f"O segundo set contém {conjunto2}")
conjunto1.difference_update(conjunto2)
print(f"O primeiro set foi atualizado com o método .difference_update() e agora contém: \n{conjunto1}")
print("\nRECONSTRUINDO OS SETS")
conjunto1 = {"Mega Drive", "Super Nintendo", "Playstation"}
conjunto2 = {"Playstation", "Nintendo 64", "Sega Saturn", "Dreamcast"}
print(f"O primeiro set contém {conjunto1}")
print(f"O segundo set contém {conjunto2}")
conjunto1.intersection_update(conjunto2)
print(f"O primeiro set foi atualizado com o método .intersection_update() e agora contém: \n{conjunto1}")
print("\nRECONSTRUINDO OS SETS")
conjunto1 = {"Mega Drive", "Super Nintendo", "Playstation"}
conjunto2 = {"Playstation", "Nintendo 64", "Sega Saturn", "Dreamcast"}
print(f"O primeiro set contém {conjunto1}")
print(f"O segundo set contém {conjunto2}")
conjunto1.symmetric_difference_update(conjunto2)
print(f"O primeiro set foi atualizado com o método .symmetric_difference_update() e agora contém: \n{conjunto1}")
print("\n")
#É possível que,ao invés de alterar um dos sets,você queira apenas retornarum  novo  set  contendo  os  elementos  que  resultaram  das  comparações.  Para  isso, podemos    utilizar    os    métodos .difference(),    .symmetric_difference(),    .union(), .intersection():
conjunto1 = {"Mega Drive", "Super Nintendo", "Playstation"}
conjunto2 = {"Playstation", "Nintendo 64", "Sega Saturn", "Dreamcast"}
print(f"\nO primeiro set contém {conjunto1}")
print(f"O segundo set contém {conjunto2}")
novo_conjunto = set.difference(conjunto1, conjunto2)
print(f"O novo set foi gerado a partir do método .difference() usando os sets 1 e 2 e contém: \n{novo_conjunto}")
print(f"\nO primeiro set contém {conjunto1}")
print(f"O segundo set contém {conjunto2}")
novo_conjunto = set.symmetric_difference(conjunto1, conjunto2)
print(f"O novo set foi gerado a partir do método .symmetric_difference() usando os sets 1 e 2 e contém: \n{novo_conjunto}")
print(f"\nO primeiro set contém {conjunto1}")
print(f"O segundo set contém {conjunto2}")
novo_conjunto = set.union(conjunto1, conjunto2)
print(f"O novo set foi gerado a partir do método .union() usando os sets 1 e 2 e contém: \n{novo_conjunto}")
print(f"\nO primeiro set contém {conjunto1}")
print(f"O segundo set contém {conjunto2}")
novo_conjunto = set.intersection(conjunto1, conjunto2)
print(f"O novo set foi gerado a partir do método .intersection() usando os sets 1 e 2 e contém: \n{novo_conjunto}")
print("\n")
#Ainda  podemos  utilizar  métodos  que  retornam  valores  booleanos,  como .isdisjoint(), issubset(), issuperset():
conjunto1 = {"Mega Drive", "Super Nintendo", "Playstation"}
conjunto2 = {"Mega Drive", "Super Nintendo","Playstation", "Nintendo 64", "Sega Saturn", "Dreamcast"}
print(f"\nO primeiro set contém {conjunto1}")
print(f"O segundo set contém {conjunto2}")
print(f"Ao comparar o set 1 com o set 2 utilizando o método isdisjoint() obtivemos \n{conjunto1.isdisjoint(conjunto2)}, pois existem elementos do set 1 que se repetem no set 2")
print(f"\nO primeiro set contém {conjunto1}")
print(f"O segundo set contém {conjunto2}")
print(f"Ao comparar o set 1 com o set 2 utilizando o método issubset() obtivemos \n{conjunto1.issubset(conjunto2)}, pois o conjunto de elementos do set 1 está contido no set 2")
print(f"\nO primeiro set contém {conjunto1}")
print(f"O segundo set contém {conjunto2}")
print(f"Ao comparar o set 1 com o set 2 utilizando o método issuperset(), obtivemos \n{conjunto1.issuperset(conjunto2)}, pois o conjunto de elementos do set 2 não está contido no set 1")
print("\n")
#Por fim, vamos testar os últimos métodos disponíveis para o tipo set: .clear(), .copy(), .pop(), .remove()e.discard().
conjunto = {"Mega Drive", "Super Nintendo","Playstation", "Nintendo 64", "Sega Saturn", "Dreamcast"}
copia = conjunto.copy()
print(f"O conjunto original contém {conjunto}")
print(f"Ao gerar uma cópia utilizando o copy(), obtivemos {copia}")
copia.clear()
print(f"\nAo utilizar o método clear na cópia, ela ficou assim: \n{copia}")
print(f"Mas o conjunto original permanece inalterado: \n{conjunto}")
conjunto.pop()
print(f"\nAo utilizar o método pop() no conjunto, ele ficou assim: \n{conjunto}")
conjunto = {"Mega Drive", "Super Nintendo","Playstation", "Nintendo 64", "Sega Saturn", "Dreamcast"}
print(f"\nO conjunto foi recriado e agora contém \n{conjunto}")
conjunto.remove("Mega Drive")
print(f"Ao utilizar o método remove() com o item Mega Drive, o conjunto ficou assim \n{conjunto}, mas retornaria um erro caso o item não estivesse no conjunto")
conjunto = {"Mega Drive", "Super Nintendo","Playstation", "Nintendo 64", "Sega Saturn", "Dreamcast"}
print(f"\nO conjunto foi recriado e agora contém \n{conjunto}")
conjunto.discard("Mega Drive")
print(f"Ao utilizar o método discard() com o item Mega Drive o conjunto ficou assim \n{conjunto}, e não retornaria um erro caso o item não estivesse no conjunto")
print("\n")
#já sabe: quando precisar de uma estrutura dinâmica que suporte repetições,deve  usar  a  list;quando  precisar  que  ela  não  suporte  repetições  de elementos,é  melhor  usar  o  set;e,  por  fim,  quando  precisar  de  uma  estrutura imutável,a  tuple  será  a  solução.  Mas  e  quando  precisarmos  associar  os  nossos dados a determinados valores? É aí que entra o dicionário!