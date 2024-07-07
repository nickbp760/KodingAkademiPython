nilai = int(input(" masukan Nilai "))
print("Hasil Grade Nilai adalah")
if nilai <= 50:
    print("D")
elif nilai <= 70:
    print("C")
elif 70 < nilai <= 80:
    print("B")
# elif nilai > 80:
else:
    print("A")