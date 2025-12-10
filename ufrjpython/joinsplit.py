#Exercício 4: Usando o comando split()
arq=open("Documentos/ufrjpython/ids.txt","r+") #Abrindo o arquivo
todas_linhas=arq.read() #Lendo todas as linhas do arquivo
print(todas_linhas) #Imprimindo todas as linhas
linhas_separadas=todas_linhas.split() #Separando as linhas
print(linhas_separadas) #Imprimindo as linhas separadas
arq.close() #Fechando o arquivo
#Exercício 4: Usando o comando join()
arq=open("Documentos/ufrjpython/ids.txt","r+") #Abrindo o arquivo
todas_linhas=arq.read() #Lendo todas as linhas do arquivo
print(todas_linhas) #Imprimindo todas as linhas
linhas_separadas=todas_linhas.split() #Separando as linhas
print(linhas_separadas) #Imprimindo as linhas separadas
linhas_juntas=' '.join(linhas_separadas) #Juntando as linhas
print(linhas_juntas) #Imprimindo as linhas juntas
arq.close() #Fechando o arquivo

