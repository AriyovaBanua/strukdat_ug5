class Karyawan:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
        self.jenisKelamin = None
        self.upahPerHari = None

    def setJenisKelamin(self, jenisKelamin):
        self.jenisKelamin = jenisKelamin

    def setUpahPerHari(self, upahPerHari):
        self.upahPerHari = upahPerHari

    def printInfo(self):
        print("======== Info ========")
        print(f"Nama \t\t: {self.nama}")
        print(f"Umur \t\t: {self.umur}")
        print(f"Jenis kelamin \t: {self.jenisKelamin}")
        print(f"Upah per hari \t: {self.upahPerHari}")

    def hitungGajiBulanan(self, hari):
        if self.upahPerHari is None:
            print("Error: Upah per hari belum diisi")
        else:
            gajiBulanan = self.upahPerHari * hari
            print(f"Gaji bulanan {self.nama} adalah: {gajiBulanan}")


orang1 = Karyawan("Haniif", 90)
orang1.printInfo()
# Output:
# Info
# Nama         : Haniif
# Umur         : 90
# Jenis kelamin: None
# Upah per hari: None

orang2 = Karyawan("Sindu", 190)
orang2.setJenisKelamin("Laki-laki")
orang2.setUpahPerHari(30000)
orang2.printInfo()
# Output:
# Info
# Nama         : Sindu
# Umur         : 190
# Jenis kelamin: Laki-laki
# Upah per hari: 30000

orang1.hitungGajiBulanan(28)
# Output:
# Error: Upah per hari belum diisi

orang2.hitungGajiBulanan(30)
# Output:
# Gaji bulanan Sindu adalah: 900000