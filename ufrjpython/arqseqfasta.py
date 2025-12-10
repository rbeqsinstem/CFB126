#Exercício 8: Criando um arquivo de sequência em formato FASTA.
# Sequências fornecidas
seq1_id = "VC1458"
seq1 = "TTTGAAGGCTAATGAAAAAGCAGATTT"

seq2_id = "BK4320"
seq2 = "agcattttggtggtgatttggaaagggtgt".upper()

seq3_id = "SP3450"
seq3 = "GCGC-GGTCATC-ATTATCGG-CTTTGTG---TCGGGC"
seq3 = seq3.replace("-", "").upper()

# Criar arquivo fasta
with open("sequencias.fasta", "w") as f:
    f.write(f">{seq1_id}\n{seq1}\n")
    f.write(f">{seq2_id}\n{seq2}\n")
    f.write(f">{seq3_id}\n{seq3}\n")
    
#Confirmar criação do arquivo
with open("sequencias.fasta", "r") as f:
    conteudo = f.read()
    print(conteudo)