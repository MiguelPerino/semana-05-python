def soma_divis(a: int) -> int:
    if a < 0:
       raise ValueError ('Número deve ser positivo e inteiro!')
    soma =0 
    for i in range(1, a+1):
       if a % i == 0:
        soma += i
    return soma

try:
    num = int(input('Informe um número inteiro e positivo: '))
    print()
    print(soma_divis(num))
except ValueError as e:
    print()
    print(f'Erro: {e}')


input('\nPressione Enter para fechar o programa...')
