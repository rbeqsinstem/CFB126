sequencia = "atgcgagaatgcatacaagtataacaa"
print(sequencia.upper())
for stop in range (3,len(sequencia)+1,3):
    substring= sequencia [0:stop]
    print(substring)