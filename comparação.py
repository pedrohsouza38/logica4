#Listas fornecidas contendo os produtos e o volume de vendas em cada ano
produtos = ['iphone', 'galaxy', 'ipad', 'tv', 'máquina de café', 'kindle', 'geladeira', 'adega', 'notebook dell', 'notebook hp', 'notebook asus', 'microsoft surface', 'webcam', 'caixa de som', 'microfone', 'câmera canon']
vendas2019 = [558147, 712350, 573823, 405252, 718654, 531580, 973139, 892292, 422760, 154753, 887061, 438508, 237467, 489705, 328311, 591120]
vendas2020 = [951642, 244295, 26964, 787604, 867660, 78830, 710331, 646016, 694913, 539704, 324831, 667179, 295633, 725316, 644622, 994303]

#Cabeçalho do relatório para a diretoria
print("-" * 65)
print("RELATÓRIO DE CRESCIMENTO DE VENDAS (2020 vs 2019)")
print("-" * 65)

#Estrutura de repetição para percorrer todos os produtos simultaneamente
for i, produto in enumerate(produtos):
    #Armazena as vendas de cada ano usando o índice 'i'
    venda_2019 = vendas2019[i]
    venda_2020 = vendas2020[i]
    
    #Estrutura de decisão: filtra apenas os produtos que venderam mais em 2020 do que em 2019
    if venda_2020 > venda_2019:
        #Cálculo da porcentagem de crescimento: (venda 2020 / venda 2019 - 1)
        #Multiplica por 100 para transformar em porcentagem e usa :.2f para limitar a 2 casas decimais
        crescimento_percentual = (venda_2020 / venda_2019 - 1) * 100
        
        #Exibe os resultados detalhados de cada produto que cumpriu o requisito
        print(f"Produto: {produto.title()}")
        print(f" - Vendas 2019: {venda_2019:,}")
        print(f" - Vendas 2020: {venda_2020:,}")
        print(f" - Crescimento : {crescimento_percentual:.2f}%")
        print("-" * 65)