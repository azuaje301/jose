#faça um programa que peça um valor e mostre na tela se o valor é positivo ou negativo
valor_1 =float(input("escreva um numero:"))
print("erro: escreva um numero com valor valido")
if valor_1 > 0:
    print(f"o valor{valor_1}é positivo")
elif valor_1 < 0:
    print(f"o valor{valor_1}é negativo")
else:
    print(f"o valor é igual a 0")