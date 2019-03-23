print("Kontrola težine prtljage")

tezina = float(input("\tMolimo unesite težinu prtljage: "))

while tezina <= 0 or tezina > 50:
    tezina = float(input("\tNedopušten unos. Unesite ponovno težinu: "))

if tezina > 0 and tezina <= 15:
    print("\tNema nadoplate")
elif tezina > 15 and tezina <= 50:
    print("\tNadoplata 100,00 kn")



