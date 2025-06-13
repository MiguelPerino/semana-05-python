def soma(a: int) -> int:
    soma1 = 0
    for i in range(1, a+1):
        soma1 += i
    return soma1
num = int(input('Informe um número inteiro: '))
if num < 0:
    print('Número inválido, informe um número positivo e inteiro!')
else:
    print(soma(num))

input('Pressione Enter para fechar o programa...')
