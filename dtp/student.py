class siswa:
    def __init__(self):
        self.nama = "orang"
        self.kelas = "tidak diketahui"
        self.alamat = "belum diketahui"

    def info(self):
        print(f" Halo nama saya adalah {self.nama} dan saya kelas {self.kelas} dan alamat rumah saya adalah {self.alamat}")

murid = siswa()


murid.nama = "Arya"
murid.kelas = "XI TJAT 2"
murid.alamat = "Sidoarjo,gedangan"

print(murid.nama)
print(murid.kelas)
print(murid.alamat)

print(murid.info())
        