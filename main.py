"""
Para este desafio, vamos pedir para o usuário informa a idade, o programa irá
verificar a idade e dizer:

- Menor 13 anos "você é uma criança".
- Maior que 13 anos e menor que 19 anos "Você é um adolescente".
- Maior que 20 anos "você é adulto".

"""

#informação passada pelo o usuário.

idade = int(input("Qual a sua idade: "))

#Condição para verificar a idade do usúario.
if idade < 13:
    print("Você é uma criança!")
elif idade in range(13,20):
    print("Você é um adolescente!")
else:
    print("Vocé um adulto!")