# Exercício 6: Calculando o tamanho de cada sequência.
arq = open("/home/rebeca-cruz/Documentos/ufrjpython/DNAQ2.txt", "r")
linhas = arq.readlines()  # Lendo todas as linhas do arquivo

for i, linha in enumerate(linhas):
    seq = linha.strip()     # remove \n e espaços
    tamanho = len(seq)      # Calcula o tamanho real
    print(f"Tamanho da sequência {i+1}: {tamanho} bases")

arq.close()  # Fechando o arquivo