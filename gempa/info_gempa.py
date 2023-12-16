from Gempa import gempa

Banten = gempa("Banten", 1.2)
Palu = gempa("Palu", 6.1)
Cianjur = gempa("Cianjur", 5.6)
Jayapura = gempa("Jayapura", 3.3)
Garut = gempa("Garut", 4.0)

Banten.dampak()
Palu.dampak()
Cianjur.dampak()
Jayapura.dampak()
Garut.dampak()