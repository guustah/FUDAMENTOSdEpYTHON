#Exercio 21 
ValorSegundos = int(input("Digite um valor em sgundos:"))
Minutos = ValorSegundos / 60
Horas = Minutos / 60
segundos = Minutos * 60
print(f"Seu valor equivale a {Horas} {Minutos} {segundos}")