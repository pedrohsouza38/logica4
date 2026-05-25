# logica4
Exercícios de Lógica com Python 4

Exercicios de loops - Fase 2

Exercício 1 - Metas de Vendas:
Dadas as listas abaixo de vendedores e vendas, crie um loop WHILE
que ira imprimir somente os nomes do vendedores que bateram a meta:

venda = [250, 330, 440, 540, 350, 250, 368, 40, 250, 30, 30]
vendedores = ['maria', 'mara', 'joão', 'silva', 'santos', 'mario', 'carlos', 'marly', 'xuxa', 'chica', 'zinha']

meta = 50

#seu código aqui

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

Explicação das Estruturas Utilizadas

1. Estrutura de Repetição (while)

O while é usado quando precisa que um bloco de código seja repetido enquanto uma condição for verdadeira.

Por que foi usado: Como não sabe de antemão qual é o tamanho da lista que vai processar, usa o len(vendedores) para saber quantos itens existem. O while roda repetidamente até que o indice alcance o fim da lista.

Atenção: É obrigatório incrementar a variável (indice += 1 no final do código), pois sem isso o loop rodaria infinitamente travando o editor.

2. Estrutura de Decisão (if)

O if avalia uma condição lógica e executa um bloco de código específico apenas se essa condição for verdadeira (True).

Por que foi usado: O objetivo do programa é filtrar os vendedores. A estrutura if venda[indice] > meta: compara o valor de venda de um funcionário específico com a meta de 50. Se o valor for maior, o programa executa a linha print(). Se for menor ou igual, ele ignora e passa para o próximo.

Exercício 2 - Soma até certo limite
Você está jogando um jogo em que precisa somar os números inteiros sequencialmente até que a soma ultrapasse 20.
Escreva um programa que calcule e exiba a soma desses números.

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

Explicação das Estruturas Utilizadas

Estrutura de Repetição (while): Utiliza o laço while pois não sabe exatamente quantos números precisa somar até atingir a meta. Ele continuará rodando enquanto (while) a condição soma_total <= 20 for verdadeira. Quando a soma finalmente passar de 20, a condição torna-se falsa e o laço é encerrado.

Estrutura de Decisão (if / else): Utiliza o if para verificar se o valor acabou de ultrapassar o número 20. Isso permite executar um bloco de código específico apenas quando a condição de parada do jogo for atingida, exibindo mensagens diferentes para o andamento do jogo e para o resultado final.

Exercício 3: Adivinhe o número
Situação Problema: Você está brincando de adivinhar o número que um computador escolheu entre 1 e 100. Cada vez que você adivinha, o computador lhe dirá se o número é maior ou menor. Escreva um programa que permita que o jogador adivinhe o número e conte quantas tentativas foram necessárias.

import random

def jogo_adivinhacao():
    print("Bem-vindo ao Jogo de Adivinhação!")
    
    #Estrutura de decisão: gera um número aleatório de 1 a 100
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    acertou = False
    
    #Estrutura de repetição: continuará rodando até o jogador acertar
    while not acertou:
        try:
            palpite = int(input("\nDigite o seu palpite (entre 1 e 100): "))
            tentativas += 1
            
            #Estruturas de decisão encadeadas (if, elif, else)
            if palpite == numero_secreto:
                acertou = True
                print(f"Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativas.")
            elif palpite > numero_secreto:
                print("O número que você escolheu é MAIOR que o número secreto.")
            else:
                print("O número que você escolheu é MENOR que o número secreto.")
        except ValueError:
            print("Entrada inválida. Por favor, digite apenas números inteiros.")

#Executa o jogo
jogo_adivinhacao()


Explicação das Estruturas Utilizadas

1. Estruturas de Decisão (if, elif, else)

Uso no código: São usadas para comparar o palpite do usuário com o numero_secreto.

Justificativa: O computador precisa avaliar a resposta do usuário e ramificar o caminho do programa com base na comparação. Se for igual, ele encerra. Se for maior ou menor, ele fornece uma dica.

2. Estrutura de Repetição (while)

Uso no código: Envolve o bloco principal do jogo com while not acertou:.

Justificativa: Como não sabe quantas tentativas o jogador precisará para acertar, precisa de um laço contínuo. O laço while é ideal aqui, pois roda infinitamente até que a condição de parada (acertar o número) seja alcançada.

Exercício 4: Tabuada
Você é um estudante tentando aprender a tabuada. 
Escreva um programa que peça um número ao usuário e, em seguida, exiba a tabuada desse número, de 1 a 10.

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

Justificativa do Uso das Estruturas

Estruturas de Decisão (if e else): Foram utilizadas para tratar casos especiais. O programa verifica se o usuário digitou 0. Se a condição for verdadeira, o bloco if é executado, exibindo uma mensagem direta e evitando cálculos desnecessários. Caso contrário, o fluxo segue para o else, onde o cálculo padrão é realizado.

Estruturas de Repetição (for): A repetição é necessária para evitar a digitação manual da instrução print dez vezes. O comando for contador in range(1, 11) diz ao Python: "Para cada número inteiro chamado contador no intervalo de 1 até 10, execute o bloco de código abaixo". Isso automatiza o processo e torna o código mais limpo e profissional.

Exercício 5: Contagem de vogais
Você está analisando palavras e deseja saber quantas vogais cada palavra contém. Escreva um programa que conte e exiba o número de vogais em uma palavra inserida pelo usuário.

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

Explicação do Código e Estruturas

Manipulação de Strings: O método .lower() é utilizado logo na entrada de dados para converter todas as letras digitadas em minúsculas. Isso facilita a verificação, evitando que o programa precise testar "A" e "a" separadamente.

Estrutura de Repetição (for): O comando for letra in palavra: cria um laço de repetição que percorre a palavra caractere por caractere. Ele garante que nenhuma letra seja ignorada e que o programa execute a verificação para toda a extensão da palavra.

Estrutura de Decisão (if): O comando if letra in vogais: funciona como um filtro. Ele verifica se a letra que está sendo avaliada no momento pertence à lista "aeiou". Se a condição for verdadeira, o código entra no bloco e executa a contagem.

DESAFIOS

1. Criando um Registro de Hóspedes

Digamos que você está criando o sistema para registrar a chegada de hóspedes em um hotel. No hotel, os hóspedes podem ter quartos com 1, 2, 3 e 4 pessoas. Seu sistema deve conseguir:

1. Identificar quantas pessoas o hóspede que acabou de chegar vai ter no quarto (perguntando por meio de input)
2. De acordo com a quantidade de pessoas do hóspede, ele deve fazer um for para perguntar o cpf e o nome de cada pessoa, a fim de registrá-la no quarto (2 inputs para cada pessoa, 1 para o cpf e outro para o nome)
3. O seu programa então deve gerar uma lista com todas as pessoas que ficarão no quarto em que cada item dessa lista é o nome da pessoa e o cpf da pessoa, assim:

EXEMPLO:
quarto = [
    ['João', 'cpf:00000000000'],
    ['Julia', 'cpf:11111111111'],
    ['Marcus', 'cpf:22222222222'],
    ['Maria', 'cpf:33333333333'],
]

- Para simplificar, não vamos nos preocupar com possibilidades de "tentar colocar mais de 1 hóspede, digitar o cpf errado, etc. Nosso objetivo é treinar a criação de uma rotina de cadastro.

#Inicializa a lista vazia que armazenará os hóspedes do quarto
quarto = []

#1. Identificar quantas pessoas ficarão no quarto
qtd_pessoas = int(input("Quantas pessoas ficarão no quarto (1, 2, 3 ou 4)? "))

#2. Estrutura de repetição para cadastrar cada hóspede
for i in range(qtd_pessoas):
    print(f"\n--- Cadastro do {i + 1}º Hóspede ---")
    
    nome = input("Digite o nome do hóspede: ")
    cpf = input("Digite o CPF do hóspede (ex: 00000000000): ")
    
    #Formata o CPF conforme o padrão exigido
    cpf_formatado = f"cpf:{cpf}"
    
    #Cria uma lista temporária apenas para a pessoa atual: [nome, cpf_formatado]
    pessoa = [nome, cpf_formatado]
    
    #Adiciona a lista da pessoa na lista principal do quarto
    quarto.append(pessoa)

#3. Exibir o resultado final gerado
print("\n=== Cadastro Concluído ===")
print("Dados do quarto:")
print(quarto)

Justificativa e Explicação do Código

Estrutura de Repetição (for)

No código, o comando for é utilizado juntamente com a função range(qtd_pessoas). O objetivo é repetir o bloco de código que pede o nome e o CPF exatamente o número de vezes que o usuário definiu.

Exemplo: Se o recebedor digitar que o quarto terá 3 pessoas, a estrutura repetitiva irá rodar 3 vezes, garantindo que o programa não pare de pedir os dados antes da quantidade correta ser informada, e não incomode com perguntas excedentes.

Estruturas de Decisão

Embora o exemplo didático não exija o uso de validações complexas, em um sistema de hotelaria real, o if/elif/else seria fundamental neste exato momento para tomar caminhos diferentes com base em uma condição (por exemplo, garantir que o número digitado no primeiro input seja de 1 a 4.

Aplicação lógica: Usar uma decisão para checar if qtd_pessoas > 4: e barrar a entrada de pessoas excedentes, ou emitir um alerta elif qtd_pessoas < 1: para evitar quartos vazios.

2. Análise de Vendas

Nesse exercício vamos fazer uma "análise simples" de atingimento de Meta.

Temos uma lista com os vendedores e os valores de vendas e queremos identificar (printar) quais os vendedores que bateram a meta e qual foi o valor que eles venderam.
meta = 10000
vendas = [
    ['João', 15000],
    ['Julia', 27000],
    ['Marcus', 9900],
    ['Maria', 3750],
    ['Ana', 10300],
    ['Alon', 7870],
]

#seu código aqui

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

Explicação do Código e das Estruturas Utilizadas:

Estrutura de Repetição (for vendedor in vendas):

Por que usar: Como tem vários vendedores dentro de uma lista, precisa de uma forma automática de "passar" de vendedor em vendedor para analisar os dados um por um.

Como funciona: O laço for percorre a lista vendas. A cada ciclo (loop), ele pega a lista interna de um vendedor específico (ex: ['João', 15000]) e a armazena na variável vendedor. Isso evita que tenha que escrever o mesmo código manualmente para cada pessoa.

Estrutura de Decisão (if valor_vendido >= meta):

Por que usar: Precisa filtrar apenas as pessoas que alcançaram ou superaram o valor estipulado. O computador precisa de uma lógica condicional para tomar essa decisão.

Como funciona: O if avalia a condição: "O valor vendido é maior ou igual a 10000?". Se a resposta for Verdadeira (True), o bloco de código dentro do if é executado. Se for Falsa (False), o programa simplesmente ignora e vai para o próximo vendedor da lista.

3. Comparação com Ano Anterior

Digamos que você está analisando as vendas de produtos de um ecommerce e quer identificar quais produtos tiveram no ano de 2020 mais vendas do que no ano de 2019, para reportar isso para a diretoria.

Sua resposta pode ser um print de cada produto, qual foi a venda de 2019, a venda de 2020 e o % de crescimento de 2020 para 2019.

Lembrando, para calcular o % de crescimento de um produto de um ano para o outro, podemos fazer: (vendas_produto2020/vendas_produto2019 - 1)

Dica: lembre do enumerate, ele pode facilitar seu "for"

produtos = ['iphone', 'galaxy', 'ipad', 'tv', 'máquina de café', 'kindle', 'geladeira', 'adega', 'notebook dell', 'notebook hp', 'notebook asus', 'microsoft surface', 'webcam', 'caixa de som', 'microfone', 'câmera canon']
vendas2019 = [558147,712350,573823,405252,718654,531580,973139,892292,422760,154753,887061,438508,237467,489705,328311,591120]
vendas2020 = [951642,244295,26964,787604,867660,78830,710331,646016,694913,539704,324831,667179,295633,725316,644622,994303]

#seu código aqui



4. DESAFIO: FOR DENTRO DE FOR
Você tem uma lista com várias listas de números:

numeros = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

Faça um programa que:

- Percorra todas as listas usando for
- Mostre cada número na tela
- No final, mostre a soma total de todos os números


