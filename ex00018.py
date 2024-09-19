n1 = int(input('um valor:'))
n2 = int(input('outro valor:'))
s=n1+n2
m=n1*n2
d=n1/n2
di=n1//n2
e=n1**n2
print('a soma é {},\n a multiplicacao e {} \n e  a divisao e {:.3f}\n'.format(s, m, d), end='     ')
print('e a divisao inteira {} \n e a potencia {}\n'.format(di,e))