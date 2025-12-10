#Questão 2 
nome_arquivo= "apresentação.txt" #Definindo nome do arquivo
#Adicionar dados no arquivo
meus_dados= "Meu nome é Rebeca Cruz, tenho 19 anos e sou estudante de Ciências Biológicas:Biofísica na UFRJ.\n"

arq=open (nome_arquivo, "w") #Abrindo modo de escrita
arq.write (meus_dados)  #Escrevendo no arquivo
arq.close() #Fechando o arquivo


arq=open (nome_arquivo, "r") #Ler o arquivo
print (arq.read()) #Mostrando o conteúdo do arquivo
arq.close() #Fechando o arquivo