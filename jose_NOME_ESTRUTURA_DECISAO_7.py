#faça um programa que verifique se uma letra digitada é "f" ou "m".conforme a letra a escrever:
entrada_de_genero = input("escreva genero (f)feminino (m)masculino (o)outros")

if entrada_de_genero == "f":
 print(f"seu genero{entrada_de_genero} é feminino")
elif entrada_de_genero =="m":
 print(f"seu genero{entrada_de_genero}é masculino")
elif entrada_de_genero == "o":
 print(f"seu genero{entrada_de_genero}no identificado")
else:
 print("entrada não é valido por favor escreva (f) (m) ou (o)") 