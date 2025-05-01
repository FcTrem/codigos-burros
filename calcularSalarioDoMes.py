# input base
hora_de_trabalho = float(input("quantas horas voce trabalha: "))
ganho_por_hora =  float(input("voce ganha quanto por hora: "))

# calculando nosso ganho e horas de trabalho
calculo_ganho_dia = (hora_de_trabalho * ganho_por_hora)
a = calculo_ganho_dia * 7
b = a * 4

# our print
print(f" nosso salario por dia e {calculo_ganho_dia:.2f} e por semana {a:.2f} e por Mes {b:.2f}")