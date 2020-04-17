a=int(input('Digite um numero: '))
b=int(input('Digite outro numero:'))
s=a+b
m=a*b
d=a/b
di=a//b
p=a**b
print('A soma entre {} e {} é {}'.format(a,b,s), end=' ')
print('A multiplicação é {}, a divisão é {:.2f}, a divInteira é {}, a potencia é {}'.format(m, d, di, p))

