from random import randint

def identica_cruz(matriz):
    vetor_posicao = []
    
    if not matriz or not matriz[0]:
        raise ValueError ('Valores de entrada incompatíveis!')    

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if i > 0 and i < len(matriz) -1 and j > 0 and j < len(matriz[i]) -1:   #Verificação para ver se está nas bordas ou não
                acima = matriz[i -1][j]
                abaixo = matriz[i + 1][j]
                esquerda = matriz[i][j - 1]
                direita = matriz[i][j + 1]
                if matriz[i][j] == 1:
                    if acima == 1 and abaixo == 1 and esquerda == 1 and direita == 1:
                        vetor_posicao.append((i, j))    #Gruda a posição de cada elemento central no vetor
    return vetor_posicao
                    
try:
    l = int(input('Informe o número de linhas da matriz: '))
    c = int(input('Informe o número de colunas da matriz: '))

    matriz_0_1 = []
    for i in range(l):  #Formação da matriz
        linha = []
        for j in range(c):
            valor = randint(0, 1)
            linha.append(valor)
        matriz_0_1.append(linha)

    print()
   
    resultado = identica_cruz(matriz_0_1)
    print('Matriz formada:')
    for i in range(l):
        for j in range(c):
            if (i, j) in resultado:
                print(f'\033[92m{matriz_0_1[i][j]:4}\033[0m', end='')  
            else:
                print(f'{matriz_0_1[i][j]:4}', end='')
        print()
    print(f'As posições dos pontos centrais das cruzes formadas são: {resultado}')
    
except ValueError as e:
    print(f'Erro: {e}')
