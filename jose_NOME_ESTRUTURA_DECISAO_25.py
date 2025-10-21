#faça um programa para a leitura de duas notas parciais de um aluno.O programa deve calculare a média alcançada por aluno e apresentar:
numero_1 =float(input("escreva numero_1: "))
numero_2 =float(input("escreva numero_2: "))

media = (numero_1 + numero_2) /2
print(f"media{media}")

if numero_1 > 7:
    print(f"aprovado {numero_1} se a media alcançada for maior ou igual a sete")
elif numero_2 < 7:
    print(f"reprovado{numero_2} se a media for menor do que sete")
 
