#Exercício 5: Contagem de bases nitrogenadas em uma sequência de DNA
arq=open("/home/rebeca-cruz/Documentos/ufrjpython/DNAQ2.txt", "r")
linha1=arq.readline() #Lendo a primeira linha da sequência de DNA
print(linha1) #Imprimindo primeira sequência
a_count=linha1.count("A") #Contando Adenina
t_count=linha1.count("T") #Contando Timina
c_count=linha1.count("C") #Contando Citosina
g_count=linha1.count("G") #Contando Guanina
print("Número de Adenina (A):", a_count) #Imprimindo contagem de Adenina
print("Número de Timina (T):", t_count) #Imprimindo contagem de Timina
print("Número de Citosina (C):", c_count) #Imprimindo contagem de Citosina
print("Número de Guanina (G):", g_count) #Imprimindo contagem de Guanina
arq.close() #Fechando o arquivo