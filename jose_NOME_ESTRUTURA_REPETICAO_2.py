#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
nome = input("escreva seu nome:")
senha = input("escreva sua senha:")
while nome == senha:

    print("sua senha não pode ser igual que seu nome")
    print("por favor,escreva novamente sua senha e nome")

    nome = input("escreva seu nome: ")
    senha = input("escreva sua senha: ")
    
    print("""olá como vai.
           sua senha
         ficou em segurança com a gente""")
