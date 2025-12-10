cor=11.25
cozi=18
sal= 10.75
quar=9.50
banh=9.50
CASA=["corredor",cor, "cozinha",cozi, "sala",sal, "quarto",quar, "banheiro",banh]
CASA2 = CASA + ["poolhouse", 24.5]
print (CASA2)

#Usando o método .append ()
CASA.append(["poolhouse",24.5])
print (CASA)

#Usando o método .extend()
CASA.extend(["poolhouse", 24.5])
print (CASA)