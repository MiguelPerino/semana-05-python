def potencia(a:int, b:int) -> int:
    if a < 0 or b < 0:
        raise ValueError ('Número inválido, tem que ser inteiro e positivo!')
    else:
        elevado = a ** b
        print(f'X elevado a Y é: {elevado}')

try:
    x = int(input('Informe o valor de X: '))
    y = int(input('Informe o valor de Y: '))
    potencia(x, y)
except ValueError as e:
    print(f'Erro: {e}')


input('\nPressione Enter para fechar o programa...')
