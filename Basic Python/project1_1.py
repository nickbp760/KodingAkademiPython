input_teks = input(" Tuliskan Teks ")
input_teks = input_teks.lower()
print("Total Karakter ", len(input_teks))
vokal_dict = dict()
for i in ['a', 'i', 'u', 'e', 'o']:
    vokal_dict[i] = 0
total_huruf_vokal = 0
for i in input_teks:
    if i in ['a', 'i', 'u', 'e', 'o']:
        vokal_dict[i] += 1
        total_huruf_vokal += 1
print("Total Huruf Vokal = ", total_huruf_vokal)
for i in vokal_dict:
    print(i, " = ", vokal_dict[i])