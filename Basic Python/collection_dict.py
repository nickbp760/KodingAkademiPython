# user = dict()
# list_user = []
# user["nama"] = input("masukan Nama = ")
# user["umur"] = input("masukan Umur = ")
# user["alamat"] = input("masukan Alamat = ")
# user["username"] = input("masukan Username = ")
# user["password"] = input("masukan Password = ")
# print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# list_user.append(user)
# for i in list_user:
#     for key in user:
#         print(key, " = ", user[key])
# print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
buku_perpus = dict()
while True:
    print()
    action = input("Tambah/Hapus/DaftarBuku ?? ")
    if action == "Tambah":
        id_buku = input(" masukan id buku ")
        nama_buku = input(" masukan nama buku ")
        if id_buku not in buku_perpus:
            buku_perpus[id_buku] = nama_buku
        else:
            print("maaf id buku ini sudah terdaftar, silahkan gunakan id lain")
    elif action == "Hapus":
        print("list id buku dan nama buku")
        for key in buku_perpus:
            print(key, " = ", buku_perpus[key])
        id_hapus = input(" masukan id yang mau dihapus ")
        if id_hapus in buku_perpus:
            del buku_perpus[id_hapus]
            print("id buku berhasil dihapus")
        else:
            print("id tidak terdaftar")
    elif action == "DaftarBuku":
        print("list id buku dan nama buku")
        for key in buku_perpus:
            print(key, " = ", buku_perpus[key])
    else:
        break
