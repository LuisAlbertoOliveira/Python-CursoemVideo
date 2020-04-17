
print ('\033[35m Bem vindo a calculadora do Luis \n')
n1 = int(input('\033[33m Digite um valor: '))
n2 = int(input('\033[34m Digite outro numero: '))
s = n1 + n2
#print('A soma vale:',s)
#print ('A soma entre ',n1,'e  ',n2,' eh  ',s)
print ('\033[31m A soma entre {} e {} vale {}'.format(n1,n2,s))