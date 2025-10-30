#Projeto treinando o .isdigit
#Autor: Matheus Ruivo
#Data: 30/10/25

nome = input("Qual o seu nome?")
num1 = (input("Digite um número:"))
num2 = (input("outro um número:"))

ver = num1.isdigit()
ver1 = num2.isdigit()

soma = int(num1) + int(num2)

print(f'{nome}, a soma é {soma} de {num1} mais: {num2}.')
print(f"Verificando {ver} e {ver1}")