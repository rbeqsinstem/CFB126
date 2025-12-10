#Prática8-Questão3
fatorial=1
fatorial_desejado = 9
for stop in range(1,fatorial_desejado + 1):
 fatorial = fatorial * stop
 print('Fatorial de ',stop , " : ", fatorial)
print( 'Final :' ,fatorial)