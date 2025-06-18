def diagonal_principal (matriz):
    #Começa como sendo verdadeira, ou seja, ela ja é quadratica
    eh_quadrada = True
    #Se for vazia ela vira false, que nao é quadratica
    if len(matriz) == 0:
        #return []
        eh_quadrada = False
    #Verifica se a coluna é diferente de linha entao por exemplo se tiver mais coluna em uma linha do que na outra
    for linha in matriz:
        if len(linha) != len(matriz):
            '''if len(linha) != len(matriz):
            return []'''
            eh_quadrada = False
            break
    #Se nao for quadrada, vai returnar lista vazia
    if not eh_quadrada:
        return []
    else:
        #Aqui returna os elementos da diagonal principal
        dg_princ = []
        for i in range(len(matriz)):
            dg_princ.append(matriz[i][i])
        return dg_princ
        

n = int(input('Informe o tamanho da matriz quadrada (N X N): '))
print()

matriz_quadratica = []
for i in range((n)):
    linha = []
    for j in range((n)):
        linha.append(float(input(f'Informe o valor da linha [{i + 1}] e coluna [{j + 1}]: ')))
    matriz_quadratica.append(linha)

print('\n Matriz informada: ')
for i in range(n):
        for j in range(n):
            print(f'{matriz_quadratica[i][j]:7}', end = '')
        print()

print()
resultado = diagonal_principal(matriz_quadratica)
print('As diagonais principais da sua matriz é:', resultado)

input('\nPressione Enter para fechar o programa...')
