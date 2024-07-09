# Fungsi lambda untuk menjumlahkan 10 argumen
sum_ten_args = lambda *args: sum(args)  # noqa

# Contoh penggunaan
result = sum_ten_args(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(f"Hasil penjumlahan 10 angka adalah: {result}")
