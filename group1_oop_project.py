import csv

class Pelanggan:
    def __init__(self,nama,jam,durasi):
        self.nama = nama
        self.jam = jam
        self.durasi = durasi
    
    @classmethod
    def input_data(cls):
        nama = input("Nama: ")
        jam = input("Mulai jam berapa: ")
        durasi = int(input("Berapa jam?: "))
        return nama,jam,durasi
    
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
        total = int(harga1jam*self.durasi)
        print("Harga yang harus dibayar = Rp",total)
        payment = int(input("Masukkan uang anda: "))
        return payment, total

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
    
    @classmethod
    def tampilkan_menu(cls):
        print('Selamat datang!')
        print("1. Booking lapangan")
        print("2. Jadwal reservasi")
        print("3. Cancel reservasi")
        print("4. Keluar")
    
    @classmethod
    def tampilkan_daftar(cls):
        print("Nama\t\tJam mulai   Jam berakhir")
        print("=========================================")
        for slot in cls.daftar:
            # print nama
            print(slot['nama'].title(),end="")
            if len(slot['nama']) < 16:
                for _ in range(16 - len(slot['nama'])):
                    print(" ",end="")
                print(str(slot['jam'])+".00\t   ",str(slot['jam']+1)+".00")
    
    def ketersediaan(self):
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
        return available, jam_mulai
                
    
    def isi_data_pelanggan(self,available,jam_mulai):
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

    @classmethod
    def hapus_data_pelanggan(cls):
        nama = input("Masukkan nama: ")
        cls.daftar = [d for d in cls.daftar if nama not in d.values()]

        

    
    def rincian_pemesanan(self,pelanggan):
        print("\nRincian pemesanan")
        print("======================")
        print(f"Nama: {pelanggan.nama}\nJam mulai: {pelanggan.jam}.00\nJam berakhir: {pelanggan.jam+pelanggan.durasi}.00\n======================\n")


    def verifikasi_pembayaran(self):
        ...
    


def main():
    # tampilkan menu
    RentalLapangan.tampilkan_menu()
    pilihan = int(input(""))
    while True:
        if pilihan == 1:
            # input data calon pelanggan
            nama,jam,durasi = Pelanggan.input_data()

            # buat objek pelanggan dan rental
            calon_p = Pelanggan(nama,jam,durasi)
            rental = RentalLapangan(calon_p)

            # cek ketersediaan reservasi
            available, jam_mulai = rental.ketersediaan()
        
            if available == 'yes':
                # pelanggan melakukan pembayaran
                payment, total = calon_p.bayar()
                if payment >= total:
                    if payment > total:
                        kembalian = payment - total
                        print("Kembalian anda = Rp",int(kembalian))
                    # apabila pembayaran telah diverifikasi, rental mengisi data pelanggan
                    rental.isi_data_pelanggan(available, jam_mulai)

                    # rental menampilkan rincian pemesanan pelanggan
                    rental.rincian_pemesanan(calon_p)
                else:
                    print("Maaf uang anda tidak mencukupi")      
            else:
                print("Maaf jam tidak tersedia untuk direservasi")
        elif pilihan == 2:
            # Tampilkan daftar pelanggan
            print(RentalLapangan.daftar)
            RentalLapangan.tampilkan_daftar()
        elif pilihan == 3:
            # cancel
            RentalLapangan.hapus_data_pelanggan()
        elif pilihan == 4:
            # simpan daftar ke file csv
            break
        else:
            print("Mohon masukkan input yang sesuai!")

        # tampilkan menu kembali
        RentalLapangan.tampilkan_menu()
        pilihan = int(input(""))


if __name__ == "__main__":
    main()
