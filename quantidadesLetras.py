"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
 menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
 "Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
# variable and input
name = input("enter your name:")
checar_quantas_Letras_tem = len(name)

# verification the condition
if checar_quantas_Letras_tem == 2  or checar_quantas_Letras_tem <= 4:
    print(f"seu nome e curto ")
elif checar_quantas_Letras_tem == 5 or checar_quantas_Letras_tem <= 6:
    print("Seu nome e normal")
elif checar_quantas_Letras_tem > 6:
    print("seu nome e muito grande")
else:
    print("nome curto demais pra ser valido")
    


