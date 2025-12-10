#Contagem de elementos na Tupla
aminoacidos=("R", "N", "D", "C", "E", "Q", "G", "H", "I", "L", "K", "M", "F", "P", "S", "T", "W", "Y", "V")
w = len (aminoacidos)
print (w)

#Localizar o Ácido Glutâmico
aminoacidos=("R", "N", "D", "C", "E", "Q", "G", "H", "I", "L", "K", "M", "F", "P", "S", "T", "W", "Y", "V")
print (aminoacidos[4])

#Nova Tupla
aminoacidos_2=("Histidina", "Triptofano W", "Tirosina Y" ,  "Prolina P" , "Serina S")
print (aminoacidos_2)

#Soma das Tuplas
sequencia=aminoacidos + aminoacidos_2
print (sequencia)

#Contar elementos
count_w = sequencia.count("Triptofano W")
count_n = sequencia.count("N")     # Asparagina (N)
count_c = sequencia.count("C")     # Cisteína (C)

print("Triptofano (W):", count_w)
print("Asparagina (N):", count_n)
print("Cisteína (C):", count_c)

# Retornar a posição do primeiro elemento Asparagina (N)
posicao_asparagina = aminoacidos.index("N")
print("Posição da Asparagina (N):", posicao_asparagina)

# Retornar os 5 últimos elementos da tupla
ultimos_5 = aminoacidos[-5:]
print("Os 5 últimos elementos:", ultimos_5)