#Definindo a meta que os vendedores precisam atingir
meta = 10000

#Lista contendo os vendedores e seus respectivos valores de vendas
vendas = [
    ['João', 15000],
    ['Julia', 27000],
    ['Marcus', 9900],
    ['Maria', 3750],
    ['Ana', 10300],
    ['Alon', 7870],
]

#Exibindo um cabeçalho para melhor visualização no terminal
print("--- Vendedores que bateram a meta ---")

#Estrutura de repetição: Percorre cada item (vendedor) dentro da lista principal
for vendedor in vendas:
    nome = vendedor[0]  #Pega o nome do vendedor (posição 0)
    valor_vendido = vendedor[1]  #Pega o valor da venda (posição 1)
    
    #Estrutura de decisão: Verifica se o valor vendido é maior ou igual à meta
    if valor_vendido >= meta:
        #Exibe o resultado caso a condição seja verdadeira
        print(f"Vendedor: {nome} | Valor Vendido: R$ {valor_vendido}")