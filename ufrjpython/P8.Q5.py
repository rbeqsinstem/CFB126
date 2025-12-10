sequencia=["ATGGCCATGCATGCAATAAATGC"]
cont_a = 0
for base in sequencia[0]:
    if base == "A":
        cont_a += 1
        print ("Número de Adeninas:", cont_a)