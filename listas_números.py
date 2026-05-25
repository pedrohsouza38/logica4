#Lista de listas fornecida
numeros = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

#Variável para acumular a soma de todos os números
soma_total = 0

#Estrutura de repetição externa: percorre cada lista dentro da lista principal
for lista_interna in numeros:
    #Estrutura de repetição interna: percorre cada número dentro da lista atual
    for numero in lista_interna:
        #Mostra o número atual na tela
        print(f"Número encontrado: {numero}")
        
        #Estrutura de decisão: verifica se o número é par apenas como exemplo prático
        if numero % 2 == 0:
            print(f"O número {numero} é par.")
        else:
            print(f"O número {numero} é ímpar.")
            
        #Adiciona o número à nossa soma total
        soma_total += numero

#Exibe o resultado final fora do loop
print("-" * 30)
print(f"A soma total de todos os números é: {soma_total}")