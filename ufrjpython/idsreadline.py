#Parte um: Usando o comando readline()
arq=open("/home/rebeca-cruz/Documentos/ufrjpython/ids.txt", "r") 
print (arq.read()) #Ler o arquivo
readline=arq.readline() #Ler linha por linha
print (readline)
arq.close() #Fechando o arquivo
#Parte dois: Usando o comando readlines()
arq=open("/home/rebeca-cruz/Documentos/ufrjpython/ids.txt", "r")
print (arq.read()) #Ler o arquivo
readlines=arq.readlines() #Ler todas as linhas
print (readlines)
arq.close() #Fechando o arquivo