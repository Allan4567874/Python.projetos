#print('crie um algaritmo que leia um numero e mostra o seu doblo,tripo e a raiz quadrado')


n = int(input("digite um numero:"))
d = n*2
t = n*3
r = n**(1/2)
print('primero valor: {}\n segundo valor :{}\n'.format(n, d),end='')
print('o tripo vale :{}\n e a raiz quadrada é :{}\n é igual :{:.2f}\n'.format(t, n, r))