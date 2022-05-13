
# + = Adição
# - = Subtração
# * = Multiplicação
# / = Divisão
# ** ou pow(0,0) = Potência
# // = Divisão Inteira
# % = Resto da Divisão

# Ordem de Procedência

# ()
# **
# *, /, //, %
# +, -

####################################################

# print('='*20)

####################################################
# nome=input('Qual o seu nome? ')
# print('Prazer em te conhecer {}!'.format(nome))

# nome=input('qual o seu nome? ')
# print('Prazer em te conhecer {:20}!'.format(nome))

# nome=input('qual o seu nome? ')
# print('Prazer em te conhecer {:<20}!'.format(nome))

# nome=input('Qual o seu nome?')
# print('Prazer em te conhecer {:^20}'.format(nome))

# nome=input('Qual o seu nome?')
# print('Prazer em te conhecer {:>20}'.format(nome))

####

# nome=input('Qual o seu nome? ')
# print('Prazer em te conhecer {:=<20}!'.format(nome))

# nome=input('Qual o seu nome?')
# print('Prazer em te conhecer {:=^20}'.format(nome))

# nome=input('Qual o seu nome?')
# print('Prazer em te conhecer {:=>20}'.format(nome))

########################################################################################################################

n1=int(input('Um valor: '))
n2=int(input('Outro numero: '))
a=n1-n2
s=n1+n2
m=n1*n2
d=n1/n2
di=n1//n2
p=n1**n2
print('Os rezultados são: {}, {}, {}, {}, {} e {}'.format(a, s, m, d, di, p))



################################ DESAFIOS #####################################

###################### 01
print(' '*1)

n1=int(input('Desafio 1: '))
r1=n1-1
r2=n1+1
print('{}'.format(r1))
print('{}'.format(r2))

####

x=int(input('Digite um valor que vc queira saber o seu antecessor e seu sucessero'))
print('Antecessor: {}, sucessor: {}'.format(x-1, x+1))

##################### 02
print(' '*1)

print('exencício 06')

v=int(input('Desafio 2: '))
d=n1*2
t=n1*3
r=n1** (1/2)
print('{}, {}, {}'.format(d, t, r))

####

x=int(input('Digite um valor: '))
print('O dobro:{}, o triplo:{},  e a  raiz:{}.'.format((x*2), (x*3), x** (1/2)))

##################### 03
print(' '*1)

m=float(input('Digite um valor em metro(os) que vc queira converte em centimetra e milimetros: '))
cm=m*100
mm=m*1000
print('O valor: {}m, convertido em centimetros é :{:.0f}cm e milimetros :{:.0f}mm.'.format(m, cm, mm))

##################### 04
print(' '*1)

x=int(input('Digite um mumero que vc queira ver a tabuada : '))
r1=x*1
r2=x*2
r3=x*3
r4=x*4
r5=x*5
r6=x*6
r7=x*7
r8=x*8
r9=x*9
r10=x*10
print( '1 x',x,'=',r1,'\n' '2 x',x,'=',r2,'\n' '3 x',x,'=',r3,'\n' '4 x',x,'=',r4,'\n' '5 x',x,'=',r5,'\n' '6 x',x,'=',r6,'\n' '7 x',x,'=',r7,'\n' '8 x',x,'=',r8,'\n' '9 x',x,'=',r9,'\n' '10 x',x,'=',r10,)

#############################################################################
print(' '*1)

y=int(input('Digite um munero que vc queira obter a tabuada: '))
print('1 x {} = {}'.format(y, y*1))
print('2 x {} = {}'.format(y, y*2))
print('3 x {} = {}'.format(y, y*3))
print('4 x {} = {}'.format(y, y*4))
print('5 x {} = {}'.format(y, y*5))
print('6 x {} = {}'.format(y, y*6))
print('7 x {} = {}'.format(y, y*7))
print('8 x {} = {}'.format(y, y*8))
print('9 x {} = {}'.format(y, y*9))
print('10 x {} = {}'.format(y, y*10))

###################### 05
print(' '*1)

r=float(input('Digite o valor que vc que converte em Dola: '))
print('R$:{} convertido em Dola é :{}'.format(r, r*5.13))

###################### 06
print(' '*1)

a=float(input('Digite a altura da parede: '))
l=float(input('Digite a largura da parede: '))
print('A aria dessa parede é de: {}m² (metros-quadrados), e serão utilisados {} Litros de tinta para pintala'.format(a*l, a*l/2))

##################### 07
print(' '*1)

v=float(input('Digite o preço do produto: '))
print('O produto custa R$:{}, com desconto ficara R$:{}'.format(v, v-(v*5)/100))

##################### 08
print(' '*1)

s=float(input('Digite o valor do salario: '))
print('O salario R$:{} com 15% de almento sera de R$:{}.'.format(s, s+(s*15)/100))

##################### 09
print(' '*1)

r1=float(input('Digite uma note de um aluno que vc queira saber a sua média: '))
r2=float(input('Digite outra nota: '))
print('A média entre {} e {} é igual a {:.2f}'.format(r1, r2, (r1+r2)/2))

##################### 10
print(' '*1)

c=float(input('Informe a temperatura em °C: '))
print('A temperatura de {}°C correstonde a {:.2f}°F!'.format(c, (9*c)/5+32))

#################### 11
print(' '*1)

km=float(input('Digite a quantidade de kilometros precorridos pelo veiculo: '))
dias=int(input('Digite quantos dias o carro foi ultilizado: '))
print('O carro precorreu {}KM = R$:{},(valor por KM R$:0,15). Foi ultilizado por {} Dia(as) = R$:{:.2f}, (valor por Dia R$:60,00). Total:R$:{}.'.format(km, km*0.15, dias, dias*60, (km*0.15)+(dias*60)))























