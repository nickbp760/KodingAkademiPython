print("Silahkan pilih menu makanan")
print("1.Nasi Goreng")
print("2.Mie Goreng")
print("3.Es Teh")
print("4.Es Jeruk")

list_pesanan = []
while True:
    pesanan = input("Silahkan ketikan menu yang akan dipesan ")
    list_pesanan.append(pesanan)
    ingin_memesan_lagi = input("Masih ingin memesan ? (Ya/Tidak) ")
    if ingin_memesan_lagi != "Ya":
        break

print()
print("Menu Pesanan anda =")
for i in list_pesanan:
    print(i)

print("Harganya adalah 20000 x", len(list_pesanan), "=", 20000 * len(list_pesanan))