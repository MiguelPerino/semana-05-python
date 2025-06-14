def positivo_negativo(a: int) -> int:
    if a < 0: 
        return 'Número negativo.'
    else:
        return 'Número positivo.'
     

num = int(input('Informe um número para saber se é positivo ou negativo: '))
print()

print(positivo_negativo(num))


input('\nPressione Enter para fechar o programa...')
