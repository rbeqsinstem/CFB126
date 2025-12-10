#Trabalho de Conclusão de Disciplina -  CFB126
#Dupla: Rebeca O. Cruz e Vitória Catarina
import numpy as np 
import matplotlib.pyplot as plt

aminos = {
'AUG':'M',  'UGG':'W',  'UGC':'C',  'UGU':'C',  'GAC':'D',  'GAU':'D',  'GAA':'E',  'GAG':'E', 
'UUC':'F',  'UUU':'F',  'CAC':'H',  'CAU':'H',  'AAA':'K',  'AAG':'K',  'AAC':'N',  'AAU':'N', 
'CAA':'Q',  'CAG':'Q',  'UAC':'Y',  'UAU':'Y',  'UAA':' ',  'UAG':' ',  'UGA':' ',  'AUA':'I',  
'AUC':'I',  'AUU':'I',  'GCA':'A',  'GCC':'A',  'GCG':'A',  'GCU':'A',  'GGA':'G',  'GGC':'G',  
'GGG':'G',  'GGU':'G',  'CCA':'P',  'CCC':'P',  'CCG':'P',  'CCU':'P',  'ACA':'T',  'ACC':'T',  
'ACG':'T',  'ACU':'T',  'GUA':'V',  'GUC':'V',  'GUG':'V',  'GUU':'V',  'UUA':'L',  'UUG':'L',  
'CUA':'L',  'CUC':'L',  'CUG':'L',  'CUU':'L',  'AGA':'R',  'AGG':'R',  'CGA':'R',  'CGC':'R',  
'CGG':'R',  'CGU':'R',  'AGC':'S',  'AGU':'S',  'UCA':'S',  'UCC':'S',  'UCG':'S',  'UCU':'S', 
}

amino_mw = { 
'A': 89.9  , 'C': 121   , 'D': 133.10, 'E': 147.13, 'F': 165.19, 'G': 75.07 , 'I': 155.16, 
'K': 146.19, 'L': 131.17, 'M': 149.21, 'N': 132.12, 'P': 115.13, 'Q': 146.15, 'R': 174.20, 
'S': 105.09, 'T': 119.12, 'V': 117.15, 'W': 204.23, 'Y': 181.19, 'H': 155.16 }

# Questão 1: Formação da sequência FASTA
def juntar(path):
    with open(path, "r") as f:
        lines = f.readlines()[1:]
    seq = ''.join(lines).replace('\n','')
    return seq

# Questão 2: Gerar fita complementar do genoma.
def complementar(seq):
    bases = {"A":"T", "T": "A", "C":"G", "G":"C"}
    comp = ''.join(bases[s] for s in seq)
    return comp[::-1]


# Questão 3: Porção de CG
def indice (seq):

    cont = 0
    for i in seq:
        if i ==  "C" or i == "G":
            cont= cont + 1
    p = cont/len(seq)
    print (p)

    if p > 0.65:
        print ("Alto Conteúdo")
    elif p > 0.45 and p < 0.65:
        print ("Conteúdo Médio")
    elif p < 0.45:
        print ("Counteúdo Baixo")

indicegc = indice(genoma)

# Questão 4: Ilha Genômica
def grafico(genoma):
    x = [] 
    y = []
    final = len(genoma) - 500000
    for i in range (0, final, 1000):
        trecho = genoma[i: i+500000]
        seq = trecho.replace('A','').replace('T','')
        print('Inicio:',i,' , indice:',len(seq)/500000)
        ind = (seq.count('C') + seq.count('G'))/500000
        x.append(i)
        y.append(ind)
        
    media = np.mean(y)

    figura, grafico = plt.subplots()
    grafico.plot(x, y)              # Faz o plot de linha, grafico com x e y
    grafico.axhline(media)          # Faz o plot constante, o grafico da média
    grafico.set_xlabel("posição")
    grafico.set_ylabel("GC")
    plt.show()

# Questão 5
# A) Janela de Tradução:
def janeladeleitura(genoma):
  listaA=[]
  listaB=[]
  listaC=[]
  final2= len(genoma)
  for y in range(0,final2,3):
      listaA.append( genoma[y:y+3])
    
  for y in range(1,final2,3):
      listaB.append( genoma[y:y+3])
      
  for y in range(2,final2,3):
      listaC.append( genoma[y:y+3])

  return listaA, listaB, listaC

a,b,c = janeladeleitura(genoma)
print(a[:10], b[:10], c[:10])

# B) Contagem de ATG:
def contagemdeatg(a,b,c):
    conta = 0
    for z in a :
        if 'ATG' == z: 
            conta = conta + 1
            
    contb = 0
    for z in b:
        if 'ATG' == z: 
            contb = contb + 1
   
    contc =  0
    for z in c :
        if 'ATG' == z: 
            contc = contc + 1

    if conta> contb and conta>contc:
           return a
    elif contb>contc:
         return b
    else:
         return c  

contagem = contagemdeatg(a,b,c)
print(contagem[:10])

# Questão 6:Transcrição
def transcrição(dna):
    rna = [codon.replace('T','U') for codon in dna ]
    return rna
codons= transcrição(contagem)
print (codons)

#Questão 7:Tradução
def tradução (rna):
      
  amino = [ aminos[r] for r in rna if r in aminos]

  amino = ''.join(amino)
  amino = amino.split(' ')

  amino = [ proteina              for proteina  in amino if 'M' in proteina] # filtrei os que tem M
  amino = [ proteina.split('M',1) for proteina  in amino] # cortei todos no primeiro M
  amino = [ proteina[1]           for proteina  in amino] #
  amino = [ 'M'+proteina          for proteina  in amino] #
  amino = [ proteina              for proteina  in amino if  len(proteina) > 50] # filtrei os que tem M
  return amino

aminoacidos = tradução(codons)
print(aminoacidos[:20])

#B) Maior Proteína 

def maiorproteina(aminoacidos):

    maior = ''
    for proteina in aminoacidos:
        if len(proteina) > len(maior):
            maior = proteina
    return maior
proteina = maiorproteina(aminoacidos)
print(proteina)

#C) Peso mol. Proteína
def pesomol(proteina):
    peso = [amino_mw[l] for l in proteina]
    return sum(peso)

# exemplo
peso_total = pesomol(proteina)
print(f"Peso molecular da proteína: {peso_total:.2f} Da")



# exemplo de uso:
# if proteina:
#     print(pesomol(proteina))


#print(contagem[:6])
#print(codons[:6])
#print(contagem[:6])
#print(codons[:6])
genoma = juntar("/home/rebeca-cruz/Documentos/ufrjpython/genomaE.fasta")
fita_complementar = complementar(genoma)
indicegc  = indice (genoma)
a,b,c = janeladeleitura(genoma)
contagem = contagemdeatg(a,b,c)
codons= transcrição(contagem)
aminoacidos= tradução(codons)
proteina = maiorproteina (aminoacidos)
peso_total = pesomol (proteina)