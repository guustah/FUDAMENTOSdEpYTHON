nome = input("Seu nome: ")
cargo = input("Seu cargo: ")
salario = float(input("Seu salário: "))
salario_ac = salario * 1.10

if salario <= 1000 : #true 
    print(f"Seu salário acreciscido a 10% seria {salario_ac}")

print()
print(f"Prazer {nome}, você é {cargo} e recebe {salario}")