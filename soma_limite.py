#Inicialização das variáveis
soma_total = 0  #Variável que acumula o resultado das somas
contador = 1    #Variável que representa o número inteiro a ser somado

#Estrutura de repetição: Executa o bloco continuamente até que a condição seja falsa
while soma_total <= 20:
    soma_total += contador #Soma o valor atual do contador à variável 'soma_total'
    
    #Estrutura de decisão: Avalia se a soma já ultrapassou 20 para definir a ação
    if soma_total > 20:
        print(f"O último número somado foi {contador}.")
        print(f"A soma ultrapassou 20! O total acumulado é {soma_total}.")
    else:
        print(f"Somando {contador}, o total atual é {soma_total}.")
    
    contador += 1 #Incrementa o contador em 1 para a próxima sequência (1, 2, 3, etc.)

print("Fim do jogo!")