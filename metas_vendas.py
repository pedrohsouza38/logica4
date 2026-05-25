#Listas fornecidas
venda = [250, 330, 440, 540, 350, 250, 368, 40, 250, 30, 30]
vendedores = ['maria', 'mara', 'joão', 'silva', 'santos', 'mario', 'carlos', 'marly', 'xuxa', 'chica', 'zinha']
meta = 50 

#Inicializa a variável de controle (índice) do loop com zero
#O 'while' exige um contador manual para percorrer as listas
indice = 0

#Estrutura de repetição: O loop while continuará rodando enquanto o 'indice' for menor que o tamanho total da lista 'vendedores'
while indice < len(vendedores):
    
    #Estrutura de decisão: Verifica se a venda atual (acessada pelo indice) é estritamente maior do que a meta (50)
    if venda[indice] > meta:
        #Imprime o nome do vendedor caso a condição acima seja verdadeira
        print(f"Vendedor(a) que bateu a meta: {vendedores[indice]}")
        
    #Incrementa o índice para garantir que o loop avance para a próxima pessoa evitando assim um loop infinito
    indice += 1