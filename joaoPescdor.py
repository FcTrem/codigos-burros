
"""
João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu 
trabalho.
Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de 
São Paulo (50 quilos) 
deve pagar uma multa de R$ 4,00 por quilo excedente.
João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso.
Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João 
deverá pagar. Imprima os dados do programa com as mensagens adequadas.
"""

kg_fish =float(input("quantos kilos voce pescou:"))

calculo = (kg_fish / kg_fish) + 3
valorMulta = (kg_fish - 50)
valorfinalmulta = (calculo * valorMulta)


if kg_fish <= 50:
    print("Valor dentro das Regras")
      
elif kg_fish > 50:
    print(f" vc deve pagar uma multa de {valorfinalmulta:.2f} reais por quilo excedente")
else:
    print 
    (
        "valor muito alto ou valor invalido"
    )
