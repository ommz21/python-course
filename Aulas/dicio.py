dicio = {"A":"AMEIXA", "B":"BOLA", "C":"CACHORRO"}

print(dicio["A"])

print(dicio)

for chave in dicio:
    print(chave + "-" + dicio[chave])

for chave in dicio.items():
    print(chave)

for chave in dicio.values():
    print(chave)

for chave in dicio.keys():
    print(chave)