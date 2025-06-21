def matriz_caractere(matriz):
    lista_calculada = []
    letras_encontradas = []
    if not matriz or not matriz[0]:
        raise ValueError ('Valores de entrada incompatível!')
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] not in letras_encontradas:
                letras_encontradas.append(matriz[i][j])

    for letra in range(len(letras_encontradas)):
        cont = 0
        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                if matriz[i][j] == letras_encontradas[letra]:
                    cont += 1
        lista_calculada.append(letras_encontradas[letra])
        lista_calculada.append(cont)

    return lista_calculada

try:
    while True:
        l = int(input('Informe o número de linhas: '))
        c = int(input('Informe o número de colunas: '))
        if l <= 0 or c <= 0:
            print('\nNúmero inválido para linha e coluna!\nTente novamente abaixo: ')
            print()
            continue
        else:
            matriz_global = []
            for i in range(l):
                linha = []
                for j in range(c):
                    linha.append(input(f'Informe o valor da linha [{i}] e da coluna [{j}]: ').lower())
                matriz_global.append(linha)
            break
    
    print('Matriz formada: ')
    for i in range(l):
        for j in range(c):
            print(f'{matriz_global[i][j]:>4}', end = '')
        print()
    

    print(f'\nElemento e quantidade de vezes repetidas na matriz: {matriz_caractere(matriz_global)}')
except ValueError as e:
    print(f'Erro: {e}')

input('\nPressione Enter para fechar o programa...')
