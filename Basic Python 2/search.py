# Path file teks input dan output
input_file = 'Basic Python 2/input.txt'
output_file = 'Basic Python 2/output.txt'

# Baca isi file teks
with open(input_file, 'r') as file:
    text = file.read()

# Hitung jumlah kata "Gunung"
count_gunung = text.count('Gunung')

# Ganti kata "Gunung" dengan "pegunungan"
modified_text = text.replace('Gunung', 'pegunungan')

# Tulis hasil yang telah dimodifikasi ke file teks baru
with open(output_file, 'w') as file:
    file.write(modified_text)

# Tampilkan jumlah kata "Gunung" yang terhitung
print(f'Jumlah kata "Gunung" yang terhitung: {count_gunung}')
