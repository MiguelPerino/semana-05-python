def soma_divis(a: int) -> int:
    soma =0 
    for i in range(1, a+1):
       if a % i == 0:
        soma += i
    return soma

num = int(input('Informe um número inteiro e positivo: '))

print()

print(soma_divis(num))

print()

input('Pressione Enter para fechar o programa...')
