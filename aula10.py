#nome=str(input('Digite um nome: '))
#if nome=='Luis':
#    print('Que nome bonito vc tem!!!')
#print('Bom dia {}, Seja Bem Vindo(a)!!'.format(nome))
n1=float(input('\033[31;40m Digite nota1: '))
n2=float(input('\033[31;44m Informe a nota2: '))
m=(n1+n2)/2
print('\033[32m A media final eh {:.1f}'.format(m))
if m >= 6.0:
    print('Sua nota foi boa! Parabens!!')
else:
    print('Vc precisa estudar mais!')