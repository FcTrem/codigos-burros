#Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Farenheit.
Celsius = 0
Celsius = float(input("digite quanto graus celsius esta agora:"))
conver = (Celsius * 1.8)
conver2 = (conver + 32)

print(f"{Celsius}°C para Farenheit e  {conver2:.1f}")
