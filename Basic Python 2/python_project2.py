from tabulate import tabulate


class Pegawai:
    def __init__(self, nama, status_kerja, tahun_masuk, gaji, id_number):
        self.nama = nama
        self.status_kerja = status_kerja
        self.tahun_masuk = tahun_masuk
        self.gaji = gaji
        self.id_number = id_number


dict_pegawai = dict()

# Contoh penggunaan
pegawai1 = Pegawai("Budi", "Full Time", 2015, 5000000, "001")
dict_pegawai[pegawai1.id_number] = pegawai1
pegawai2 = Pegawai("Ani", "Part Time", 2018, 3000000, "002")
dict_pegawai[pegawai2.id_number] = pegawai2

while True:
    print("Selamat datang di Sistem Informasi Pegawai")
    print("Pilih Menu")
    print("1. Tambah Pegawai")
    print("2. Edit Pegawai")
    print("3. Hapus Pegawai")
    print("4. Tampilkan Pegawai")
    menu = input("Masukkan menu: ")
    if menu == "1":
        nama = input("Masukkan nama: ")
        status_kerja = input("Masukkan status kerja: ")
        tahun_masuk = int(input("Masukkan tahun masuk: "))
        gaji = int(input("Masukkan gaji: "))
        id_number = input("Masukkan ID number: ")
        pegawai = Pegawai(nama, status_kerja, tahun_masuk, gaji, id_number)
        dict_pegawai[id_number] = pegawai
        print("Pegawai berhasil ditambahkan")
    elif menu == "2":
        id_number = input("Masukkan ID number: ")
        if id_number in dict_pegawai:
            nama = input("Masukkan nama: ")
            status_kerja = input("Masukkan status kerja: ")
            tahun_masuk = int(input("Masukkan tahun masuk: "))
            gaji = int(input("Masukkan gaji: "))
            pegawai = Pegawai(nama, status_kerja, tahun_masuk, gaji, id_number)
            dict_pegawai[id_number] = pegawai
            print("Pegawai berhasil diedit")
        else:
            print("Pegawai tidak ditemukan")
    elif menu == "3":
        id_number = input("Masukkan ID number: ")
        if id_number in dict_pegawai:
            del dict_pegawai[id_number]
            print("Pegawai berhasil dihapus")
        else:
            print("Pegawai tidak ditemukan")
    elif menu == "4":
        data = []
        for id_number in dict_pegawai:
            pegawai = dict_pegawai[id_number]
            data.append([pegawai.id_number, pegawai.nama, pegawai.status_kerja,
                         pegawai.tahun_masuk, pegawai.gaji])
        print(tabulate(data, headers=["ID Number", "Nama Pegawai", "Status Kerja",
                                      "Tahun Masuk", "Gaji"], tablefmt="grid"))
    else:
        print("Menu tidak valid")
