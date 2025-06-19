def diagonal_secundaria(matriz):
    tamanho = len(matriz)
    if tamanho == 0:
        raise ValueError ('Valor de entrada incompatível!')
    for j in range(tamanho):
        if len(matriz[j]) != tamanho:
            raise ValueError ('Valor de entrada incompatível!')
    
    else:
        dg_secund = []
        for i in range(tamanho):
            dg_secund.append(matriz[i][(tamanho - 1 - i)])
        return dg_secund
    
try:
    l = int(input('Informe o número de linhas da matriz: '))
    c = int(input('Informe o número de colunas da matriz: '))
    print()
    if l == 0 or c == 0 or l != c:
        raise ValueError ('Valor de entrada incompatível!')
    else: 
        matriz_quadrada = []
        for i in range(l):
            linha = []
            for j in range(c):
                valor = int(input(f'Informe o valor da linha [{i + 1}] e coluna [{j + 1}]: '))
                linha.append(valor)
            matriz_quadrada.append(linha)

        print('Matriz informada: ')
        for i in range(l):
            for j in range(c):
                print(f'{matriz_quadrada[i][j]:7}', end = '')
            print()

    print()
    resultado = diagonal_secundaria(matriz_quadrada) 
    print(f'As diagonais secundarias são: {resultado}')

except ValueError as e:
    print(f'Erro: {e}')

input('\nPressione Enter para fechar o programa...')
