#Tamanho da lista
ncbi = ["AAY66821.1", "AAY66759.1", "AAY66711.1", "AAY66706.1", "AAY66703.1",
"AAY66697.1","AAY66696.1", "AAY66682.1", "AAY66647.1", "AAY66625.1",
"AAY66623.1","AAY66620.1", "AAY66619.1", "AAY66616.1"," AAY66609.1", "AAY66607.1",
"AAY66586.1","AAY66564.1",]
d=len(ncbi)
print (d) 

#Presença dos identificadores
true_or_false=("AAY66586.1" in ncbi, "AAY66620.1"in ncbi,"AAY66640.1" in ncbi, "AAY66562.1" in ncbi, "AAY66816.1" in ncbi)
print(true_or_false)

#Elemento na posição 10
print(ncbi[10])

#Inserção de novos identificadores nas posições indicadas
ncbi.insert (11, "AAY66967.1")
ncbi.insert (15, "AAY66880.1")
ncbi.insert (18, "AAY66874.1")
print ("Nova Lista:", ncbi)