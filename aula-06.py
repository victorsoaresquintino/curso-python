

# n1=int(input('Digite um valor: '))
# n2=int(input('Digite outro numero: '))
# r=n1+n2
# print('o resultado de {} mais {} é {}'.format(n1,n2,r))

# x=input('Digite: ')
# print(x.isascii())

################## EXERCÍCIO-03 #####################

#n1=int(input('Digite um numero: '))
#n2=int(input('Digite outro numero'))

#r=n1+n2

#print('O rezaultado de' ,r, '+' ,n1, 'é' ,n2,)


n1=int(input('Digite um numero: '))
n2=int(input('Digite outro numero'))

r=n1+n2

print('O rezaultado de {} + {} é {}'.format(n1,n2,r))

########## EXERCÍCIO-04 ###########

x=input('Digite algo : ')
print('O tipo primitivo desse valor é ',type(x))
print('Só tem espacos? ', x.isspace())
print('É um numero? ', x.isnumeric())
print('É alfabético? ', x.isalpha())
print('É alfanumérico? ', x.isalnum())
print('Está em maiúsculas? ', x.isupper())
print('Está em minúsculas? ', x.islower())
print('Está capitalizado? ', x.istitle())
