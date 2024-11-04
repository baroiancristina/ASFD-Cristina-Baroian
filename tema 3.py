from itertools import count

meniu = ['papanasi'] * 10 + ['ceafa'] * 3 + ["guias"] * 6
preturi = [["papanasi", 7], ["ceafa", 10], ["guias", 5]]
studenti = ["Liviu", "Ion", "George", "Ana", "Florica"]  # coada FIFO
comenzi = ["guias", "ceafa", "ceafa", "papanasi", "ceafa"]  # coada FIFO
tavi = ["tava"] * 7  # stiva LIFO
istoric_comenzi = []


papanasi_inceput = meniu.count("papanasi")
papanasi_comanda = comenzi.count("papanasi")
pret_papanasi = preturi[0][1]
castig_papanasi = papanasi_comanda * pret_papanasi
papanasi_ramasi = papanasi_inceput - papanasi_comanda


ceafa_inceput = meniu.count('ceafa')
ceafa_comanda = comenzi.count('ceafa')
pret_ceafa = preturi[1][1]
castig_ceafa= ceafa_comanda * pret_ceafa
ceafa_ramasa = ceafa_inceput - ceafa_comanda


guias_inceput = meniu.count ("guias")
guias_comanda = comenzi.count("guias")
pret_guias = preturi[2][1]
castig_guias = guias_comanda * pret_guias
guias_ramas = guias_inceput - guias_comanda

print(castig_guias, guias_ramas)

for i in range(len(studenti)) :
    student = studenti.pop(0)
    comanda = comenzi.pop(0)
    print(f" {student} a comandat {comanda}")
    istoric_comenzi.append([student, comanda])
    tavi.pop()

print(f" S-a comandat {papanasi_comanda} papanasi, {ceafa_comanda} ceafă, {guias_comanda} guias.")

if len(tavi) > 0:
    print(f"Mai sunt {len(tavi)} tavi")
else:
    print("Nu mai sunt tavi")

print(f"Mai sunt papanasi: {papanasi_ramasi == 9}")
print(f"Mai este ceafa: {ceafa_ramasa !=0}")
print(f"Mai este guias: {guias_ramas == 5}")
print(f"Cantina a încasat {castig_guias + castig_ceafa + castig_papanasi} lei")

