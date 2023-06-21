class Pelanggan:
    def __init__(self,nama,tanggal,jam_mulai,jam_berakhir,slot):
        self.nama = nama
        self.tanggal = tanggal
        self.jam_mulai = jam_mulai
        self.jam_berakhir = jam_berakhir
        self.slot = slot
    
    def __str__(self):
        return f"\nNama: {self.nama}\nTanggal: {self.tanggal}\nJam mulai: {self.jam_mulai}\nJam berakhir: {self.jam_berakhir}\nSlot: {self.slot}"

    @property
    def nama(self):
        return self._nama
    
    @nama.setter
    def nama(self,nama):
        self._nama = nama

    @property
    def tanggal(self):
        return self._tanggal
    
    @tanggal.setter
    def tanggal(self, tanggal):
        self._tanggal = tanggal

    @property
    def jam_mulai(self):
        return self._jam_mulai
    
    @jam_mulai.setter
    def jam_mulai(self, jam_mulai):
        self._jam_mulai = jam_mulai

    @property
    def jam_berakhir(self):
        return self._jam_berakhir
    
    @jam_berakhir.setter
    def jam_berakhir(self, jam_berakhir):
        self._jam_berakhir = jam_berakhir

    @property
    def slot(self):
        return self._slot
    
    @slot.setter
    def slot(self, slot):
        self._slot = slot

    def pesan(self):
        ...

    def cancel(self):
        ...

    def bayar(self):
        ...

    
class RentalLapangan:
    def __init__(self):
        ...

    def tambah_pelanggan(self):
        ...
    
    def isi_data_pelanggan(self):
        ...
    
    def verifikasi_pembayaran(self):
        ...
    
    def tampilkan_daftar(self):
        ...

def input_pelanggan():
    nama = input("Nama: ")
    tanggal = input("Tanggal: ")
    jam_mulai = input("Jam mulai: ")
    jam_berakhir = input("Jam berakhir: ")
    slot = input("Slot: ")
    return Pelanggan(nama,tanggal,jam_mulai,jam_berakhir,slot)

def main():
    p1 = input_pelanggan()
    print(p1)

   

if __name__ == "__main__":
    main()
