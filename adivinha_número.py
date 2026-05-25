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