#EXEMPLO 01

lanche = ('Hamburguer','suco','pizza','pudim')
print(lanche)
print(lanche[1])
print(lanche[-2])
print(lanche[1:3])
print(lanche[2:])
print(lanche[:2])
print(lanche[-2:])

#Tuplas são imutaveis
lanche[1] = 'Refrigerante'
print(lanche[1])

for comida in lache:
    print(f'Eu vou comer{comida}')
print('Comi para caramba!')

#EXEMPLO 02

a = (2,5,4)
b = (5,8,1)
print(a)
print(b)
c = a + b
print(c)
print(len(c)) #TAMANHO
print(c.count(5)) #QUANTAS VEZES APARECCE O NUMERO
print(c.index) #QUAL POSIÇÃO TÁ O NÚMERO

#EXEMPLO 03
pessoa('Gustavo',39,'M',99)
del(pessoa) #APAGA/EXCLUI DA MEMORIA
print(pessoa)