print("Silahkan Memilih Menu")
print("1. Penjumlahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")

while True:
    menu = input("Masukan Menu = ")
    if menu == "1":
        def penjumlahan(a, b):
            return a + b
        print(
            "Hasil Penjumlahan = ",
            penjumlahan(int(input("masukan angka pertama = ")), int(input("masukan angka kedua = "))))
    elif menu == "2":
        def pengurangan(a, b):
            return a - b
        print(
            "Hasil Pengurangan = ",
            pengurangan(int(input("masukan angka pertama = ")), int(input("masukan angka kedua = "))))
    elif menu == "3":
        def perkalian(a, b):
            return a * b
        print(
            "Hasil Perkalian = ",
            perkalian(int(input("masukan angka pertama = ")), int(input("masukan angka kedua = "))))
    elif menu == "4":
        def pembagian(a, b):
            return a / b
        print(
            "Hasil Pembagian = ",
            pembagian(int(input("masukan angka pertama = ")), int(input("masukan angka kedua = "))))

    ulang = input("Apakah Anda Ingin Melanjutkan? (y/n) ")
    if ulang == "y":
        continue
    else:
        break
