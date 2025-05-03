"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
 descrito, exiba a saudação apropriada. Ex. 
 Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
horario_para_input = int(input("digit the hour what you are login:"))

if(horario_para_input <= 11 or horario_para_input == 0 ):
    print("Good Morning:) ")
    
elif(horario_para_input <= 12 or horario_para_input <= 17):
    print("Good afternon")
    
elif(horario_para_input <= 18 or horario_para_input <= 23):
    print("Good Night :)")
    
else:
    print("erro")