AnoDeNascimento = int(input("Digite o ano de seu nascimento:"))
AnoAtual = int(input("Digite o ano atual:"))
idade = AnoAtual - AnoDeNascimento
idadeSemanas = 4 * 12 * idade 
print(f"A sua idade é: {idade} ")
print(f"A sua idade em semanas é {idadeSemanas}")