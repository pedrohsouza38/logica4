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