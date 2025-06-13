def eh_primo(a: int) -> int:
    cont = 0
    for i in range(1, a+1):
        if a % i == 0:
            cont += 1
    if cont == 2:
       return True
    else:
        return False

num = int(input('Informe um número para verificar se é primo ou não: '))
print('True = Primo\nFalse = Não é primo')
print()
print(eh_primo(num))

input('\nPressione Enter para fehcar o programa...')    
