def pisahkan_negatif_positif(list_angka):
    positive_list = []
    negative_values = []
    for angka in list_angka:
        if angka >= 0:
            positive_list.append(angka)
        else:
            negative_values.append(angka)

    return positive_list, negative_values


list_angka = []
print("Masukan 10 buah angka:")
for index in range(10):
    string = "masukan angka ke-" + str(index) + " = "
    value = int(input(string))
    list_angka.append(value)

print(list_angka)

positive_values, negative_values = pisahkan_negatif_positif(list_angka)
print("Positive values:", positive_values)
print("Negative values:", negative_values)
