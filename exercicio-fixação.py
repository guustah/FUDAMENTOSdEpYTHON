#Solicite a temperatura para o usuario. Se estiver abaixo de 16 graus, informe ao usuario para pegar uma blusa . Ao final escreva "fim do programa".

temperatura = float(input("Digite a temperatura: ")) 

if temperatura <= 16 : #true 
    print("Pegue uma blusa está frio.")
else : #false
    print("Pegue um óculos de sol.")

print()
print("Fim do programa.")