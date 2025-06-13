def segundos(h:int, m: int, s: int) -> int:
    if h < 0:
        print('Apenas números inteiros e positivos.')
    if h >= 0:
        horas = h * 60 *60
    if m >= 0:
        minutos = m * 60
    soma = horas + minutos + s
    print(soma)
print(segundos(2, 40, 10))  
