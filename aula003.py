"""
exercício
 Peça ao usuário para digitar seu nome
 Peça ao usuário para digitar sua idade
 Se nome e idade forem digitados:
     Exiba:
         Seu nome é {nome}
         Seu nome invertido é {nome invertido}
         Seu nome contém (ou não) espaços
         Seu nome tem {n} letras
         A primeira letra do seu nome é {letra}
         A última letra do seu nome é {letra}
 Se nada for digitado em nome ou idade: 
     exiba "Desculpe, você deixou campos vazios.
"""

nome = input("digite seu nome: ")
if(nome != ""):
    print(f"seu nome e {nome}")
    print(f"primeira letra do seu nome e {nome[-0]}")
    print(f"a utilma letra do seu nome e {nome[-1]} ")
    
    if ' ' in nome:
        print("nome contem espaco")
    else:
        print("nao contem espaco")
    
    print(f"seu nome invertido e {nome[::-1]}")
    print(f"seu nome contem {len(nome)} letras")
else:
    print("voce deixou o campo vazio")


    
    