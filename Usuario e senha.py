usuario = input("Informe o usuário que deseja acessar o sistema: ")
senha = input("Informe a senha do usuário que deseja acessar o sistema: ")
tentativa = 0
acertou = False

while usuario.upper() != "ADMIN" or senha != "123":
    if tentativa == 1:
        print("ultima chance")
        
    elif tentativa == 2:
        print("conta bloqueada")
        break
    print("tente novamente! ")
    usuario = input("Informe o usuário que deseja acessar o sistema: ")
    senha = input("Informe a senha do usuário que deseja acessar o sistema: ")
    tentativa = tentativa +1
    
else:
    acertou = True

if acertou:
   print ("Certoooo")