def soma(a: int) -> int:
    soma1 = 0
    if a < 0:
        raise ValueError ('Apenas números inteiros e positivos!')
    else:
        for i in range(1, a+1):
            soma1 += i
        return soma1

try:    
    num = int(input('Informe um número inteiro: '))
    print()
    print(soma(num))
except ValueError as e:
    print(f'Erro: {e}')


input('\nPressione Enter para fechar o programa...')
