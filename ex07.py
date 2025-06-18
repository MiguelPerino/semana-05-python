def diagonal_principal (matriz):

    if len(matriz) == 0:
        raise ValueError ('Valores de entrada inválidos!')

    for linha in matriz:
        if len(linha) != len(matriz):
            raise ValueError ('A matriz não é quadrada!')
    else:
        #Aqui returna os elementos da diagonal principal
        dg_princ = []
        for i in range(len(matriz)):
            dg_princ.append(matriz[i][i])
        return dg_princ
        
try:
    l = int(input('Informe o tamanho da linha da matriz: '))
    c = int(input('Informe o tamanho da coluna da matriz: '))
    print()

    matriz_quadratica = []
    if l != c or l == 0 or c == 0:
        print('Matriz não quadrada!')
    else:
        for i in range((l)):
            linha = []
            for j in range((c)):
                linha.append(float(input(f'Informe o valor da linha [{i + 1}] e coluna [{j + 1}]: ')))
            matriz_quadratica.append(linha)

        print('\n Matriz informada: ')
        for i in range(l):
                for j in range(c):
                    print(f'{matriz_quadratica[i][j]:7}', end = '')
                print()

        print()
        resultado = diagonal_principal(matriz_quadratica)
        print('As diagonais principais da sua matriz é:', resultado)

except ValueError as e:
    print(f'Erro: {e}')
