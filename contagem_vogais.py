#Solicita que o usuário digite uma palavra e converte tudo para minúsculo
palavra = input("Digite uma palavra: ").lower()

#Define a lista de vogais que quer verificar
vogais = "aeiou"

#Inicializa a variável contadora
contador_vogais = 0

#Estrutura de repetição: passa letra por letra dentro da palavra digitada
for letra in palavra:
    
    #Estrutura de decisão: verifica se a letra atual é uma vogal
    if letra in vogais:
        contador_vogais += 1  #Incrementa o contador se for uma vogal

#Exibe o resultado final
print(f"A palavra '{palavra}' contém {contador_vogais} vogais.")