def segundos(h:int, m: int, s: int) -> int:
    if h < 0 or m < 0 or s < 0:
        raise ValueError ('Erro! Apenas números inteiros e positivos!')
    if h >= 0:
        horas = h * 60 *60
    if m >= 0:
        minutos = m * 60
    soma = horas + minutos + s
    print(f'O tempo total em segundos é igual a: {soma}')

try:
    hour = int(input('Informe a hora: '))
    minute = int(input('Informe os minutos: '))
    seconds = int(input('Informe os segundos: '))
    segundos(hour, minute, seconds)
except ValueError as e:
    print(f'Erro: {e}')


input('\nPressione Enter para fechar o programa...')
