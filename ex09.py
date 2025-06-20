def max_min(matriz):
    tamanho = len(matriz)
    if not matriz or not matriz[0]:
        raise ValueError ('Valor de entrada incompatível!')

    maior = matriz[0][0]
    menor = matriz[0][0]
    for i in range(tamanho):
        for j in range(len(matriz[i])):     #Percorre a todos os elementos de cada linha
            if matriz[i][j] > maior:
                maior = matriz[i][j]
            if matriz[i][j] < menor:
                menor = matriz[i][j]
    return [maior, menor]

try:
    l = int(input('Informe o número de linhas da matriz: '))
    c = int(input('Informe o número de colunas da matriz: '))

    matriz_maior_menor = []
    for i in range(l):
        linha = []
        for j in range(c):
            valor = float(input(f'Informe o valor da linha [{i}] e da coluna [{j}]: '))
            linha.append(valor)
        matriz_maior_menor.append(linha)

    print()
    resultado = max_min(matriz_maior_menor)
    print(f'O maior valor da matriz é: {resultado[0]}')
    print(f'O menor valor da matriz é: {resultado[1]}')

except ValueError as e:
    print(f'Erro: {e}')

input('\nPressione Enter para fechar o programa...')
