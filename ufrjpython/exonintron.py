#Exercício 7: Extraindo éxons e íntrons de uma sequência genômica.
with open("Documentos/ufrjpython/genomic_DNA.txt", "r") as f: #Abrindo o arquivo
    seq = f.read().strip() #Lendo o arquivo e removendo espaços em branco
    exon1 = seq[0:63]     # pega do início até 63 (exclui o 63)
    intron = seq[63:90]   # pega da posição 63 até 89
    exon2 = seq[90:]      # do 90 até o fim
#A) Imprimindo as sequências
print("Exon 1:\n", exon1)
print("Intron:\n", intron)
print("Exon 2:\n", exon2)
#B) Tamanho total codificante
tamanho_total = len(seq)
print("Tamanho total da sequência:\n", tamanho_total)
#C) Seq. total com o intron lowercase
seq_com_intron_lower = exon1 + intron.lower() + exon2
print("Sequência com intron em lowercase:\n", seq_com_intron_lower)
#D) Proporção codificante (%)
tamanho_codificante = len(exon1) + len(exon2)
proporcao_codificante = (tamanho_codificante / tamanho_total) * 100
print("Proporção codificante (%):\n", proporcao_codificante)  
