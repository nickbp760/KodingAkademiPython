Makhluk_Hidup = dict()
Makhluk_Hidup[1] = "Ayam"
Makhluk_Hidup[2] = "Sapi"
Makhluk_Hidup[3] = "Mawar"
Makhluk_Hidup[4] = "Kambing"
Makhluk_Hidup[5] = "Lily"
Copy_Makhluk_Hidup = Makhluk_Hidup.copy()
del Makhluk_Hidup[3]
del Makhluk_Hidup[5]
print(Makhluk_Hidup)
print(Copy_Makhluk_Hidup)
for i in Copy_Makhluk_Hidup.keys():
    if i % 2 == 1:
        Copy_Makhluk_Hidup[i] = "Hewan"
print(Copy_Makhluk_Hidup)
