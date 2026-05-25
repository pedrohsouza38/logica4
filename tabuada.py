#Solicita um número ao usuário e o converte para inteiro
numero = int(input("Digite um número para ver a tabuada: "))

#Estrutura de Decisão: verifica se o número digitado é igual a 0
if numero == 0:
    print("A tabuada do 0 é sempre 0!")
else:
    #Estrutura de Repetição: cria um laço que vai de 1 a 10
    #O range(1, 11) gera números de 1 até 10 (o 11 é o limite, mas não é incluído)
    for contador in range(1, 11):
        #Calcula o resultado da multiplicação
        resultado = numero * contador
        
        #Exibe a tabuada de forma formatada
        print(f"{numero} x {contador} = {resultado}")