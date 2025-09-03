donas = int(input("Ingresa la cantidad de donas: "))

print(f"Con {36} donas puedes hacer {3} docenas!")


num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))
residuo = num1 % num2
print(f"{num1} dividido entre {num2} tiene un residuo de {residuo}!")


segundos = int(input("Ingresa la cantidad de segundos: "))

horas = segundos // 3600
minutos = (segundos % 3600) // 60
segundos_restantes = segundos % 60

print(f"{segundos} segundos son {horas} horas, {minutos} minutos y {segundos_restantes} segundos")
