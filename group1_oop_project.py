import csv

class Pelanggan:
    def __init__(self,nama,jam,durasi):
        self.nama = nama
        self.jam = jam
        self.durasi = durasi
    
    @property
    def nama(self):
        return self._nama
    
    @nama.setter
    def nama(self,nama):
        self._nama = nama

    @property
    def jam(self):
        return self._jam
    
    @jam.setter
    def jam(self, jam):
        jam = int(jam.removesuffix('.00'))
        self._jam = jam
    
    @property
    def durasi(self):
        return self._durasi
    
    @durasi.setter
    def durasi(self, durasi):
        self._durasi = durasi

    def cancel(self):
        ...

    def bayar(self):
        print("- Biaya 1 jam adalah Rp. 150.000")
        harga1jam = 150000
        print("Harga yang harus dibayar = Rp",int(harga1jam*self.jam))

class PelangganLama(Pelanggan):
    def __init__ (self, nama):
        self.nama = nama

    
    # Fungsi bayar() di override
    def bayar(self):
        print("- Biaya 1 jam adalah Rp. 100.000")
        harga1jam = 100000
        print("Harga yang harus dibayar = Rp",int(harga1jam*self.jam))


    
class RentalLapangan:
    daftar = []

    def __init__(self,pelanggan=None):
        self.pelanggan = pelanggan
    
    def isi_data_pelanggan(self,pelanggan):
        # buat empty list untuk mengisi jam2
        jam_mulai = []
        m = 0

        # masukkan setiap 1 jam ke dalam list
        for _ in range(getattr(self.pelanggan,'durasi')):
            jam_mulai.append(getattr(self.pelanggan,'jam')+m)
            m+=1

        available = 'yes'
        # cek apakah jam yang dipesan pelanggan tersedia
        for slot in self.daftar:
            if slot['jam'] in jam_mulai:
                available = 'no'
                break
        
        if available == 'yes':
            # apabila jam yang diinput dalam jangka waktu jam 10 pagi hingga jam 10 malam maka masukkan data pelanggan
            if jam_mulai[0] >= 10 and jam_mulai[-1] <= 21:
                j = 0
                for _ in range(getattr(self.pelanggan,'durasi')):
                    new_data = {}
                    new_data["nama"] = getattr(self.pelanggan,'nama')
                    new_data["jam"] = getattr(self.pelanggan,'jam')+j
                    new_data["durasi"] = getattr(self.pelanggan,'durasi')
                    self.daftar.append(new_data)
                    j+=1
                return True
            else:
                print("Maaf kami tidak melayani reservasi sebelum jam 10 pagi atau setelah jam 10 malam")
                return False
        else:
            print("Maaf slot ini sudah direservasi\n")
            return False

    
    def rincian_pemesanan(self,pelanggan):
        print("\nRincian pemesanan")
        print("======================")
        print(f"Nama: {pelanggan.nama}\nJam mulai: {pelanggan.jam}.00\nJam berakhir: {pelanggan.jam+pelanggan.durasi}.00\n======================\n")


    def verifikasi_pembayaran(self):
        ...
    
    def tampilkan_daftar(self):
        print("Nama\t\tJam mulai   Jam berakhir")
        print("=========================================")
        for slot in self.daftar:
            # print nama
            print(slot['nama'].title(),end="")
            if len(slot['nama']) < 16:
                for _ in range(16 - len(slot['nama'])):
                    print(" ",end="")
                print(str(slot['jam'])+".00\t   ",str(slot['jam']+1)+".00")


    
def input_data():
    nama = input("Nama: ")
    jam = input("Mulai jam berapa: ")
    durasi = int(input("Berapa jam?: "))
    return nama,jam,durasi


def menu():
    print('Selamat datang!')
    print("1. Booking lapangan")
    print("2. Jadwal reservasi")
    print("3. Cancel reservasi")
    print("4. Keluar")




def main():
    menu()
    pilihan = int(input(""))
    while True:
        if pilihan == 1:
            # 1. input data calon pelanggan
            nama,jam,durasi = input_data()
            # 2. buat objek pelanggan dan rental
            calon_p = Pelanggan(nama,jam,durasi)
            rental = RentalLapangan(calon_p)
            # 3. pelanggan melakukan pembayaran
            ...
            # 4. apabila pembayaran telah diverifikasi, rental mengisi data pelanggan
            tersedia = rental.isi_data_pelanggan(calon_p)
            if tersedia == True:
                # 5. rental menampilkan rincian pemesanan pelanggan
                rental.rincian_pemesanan(calon_p)
            else:
                pass
        elif pilihan == 2:
            rental = RentalLapangan()
            print(rental.daftar)
            rental.tampilkan_daftar()
        elif pilihan == 3:
            ...
        elif pilihan == 4:
            # simpan daftar ke file csv
            break
        else:
            print("Mohon masukkan input yang sesuai!")

        
        menu()
        pilihan = int(input(""))


if __name__ == "__main__":
    main()
