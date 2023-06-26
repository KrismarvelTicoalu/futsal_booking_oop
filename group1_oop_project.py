import csv
import datetime

# Get the current datetime
current_datetime = datetime.datetime.now()

# Mendapatkan tanggal hari ini
current_date = current_datetime.date()

# Mendapatkan tanggal hari besok
tommorow_date = current_date + datetime.timedelta(days=1)

tanggal = tommorow_date



class Pelanggan:
    harga1jam = 150000

    def __init__(self,nama,jam,durasi):
        self.nama = nama
        self.jam = jam
        self.durasi = durasi
    
    @classmethod
    def input_nama(cls):
        while True:
            nama = (input("Masukkan nama: ")).strip()
            nama1 = nama.replace(' ','')
            nama2 = nama.split()
            if nama1.isalpha():
                if len(nama2) == 1:
                    return nama
                else:
                    print("Mohon masukkan hanya nama depan anda")
                    pass
            else:
                print("Mohon masukkan nama anda dengan benar")
                pass
    
    @classmethod
    def input_jam(cls):
        print("Note\n- Pemesanan hanya bisa dilakukan dalam satuan per jam")
        print("- Tidak dapat booking di luar jam buka (10.00 - 22.00)")
        print("- Input jam harus dibulatkan")
        print("contoh: 14.00 --> benar")
        print("        14.30 --> salah")
        print("        14.03 --> salah")
        while True:
            try:
                jam = int(input("Masukkan jam mulai: ").removesuffix(".00"))
                if jam/jam!=1 :
                    print("Mohon masukkan input yang sesuai")
                    pass
                else:
                    return jam
            except ValueError :
                print("Mohon masukkan input yang sesuai")
                pass
    
    @classmethod
    def input_durasi(cls):
        while True:
            try:
                durasi = int(input("Berapa jam? "))
                if durasi >= 1:
                    return durasi
                else:
                    print("Mohon masukkan input yang sesuai")
                    pass
            except ValueError:
                print("Mohon masukkan input yang sesuai")
                pass
    
    @classmethod
    def input_data(cls):
        nama = cls.input_nama()
        jam = cls.input_jam()
        durasi = cls.input_durasi()
        return nama,jam,durasi
    
    def bayar(self):
        print("- Biaya 1 jam adalah Rp. 150.000")
        total = int(self.harga1jam*self.durasi)
        print("Harga yang harus dibayar = Rp",int(total))
        payment = int(input("Masukkan uang anda: "))
        self.total = int(total)
        return payment, int(total)

class PelangganLama(Pelanggan):
    def __init__ (self, nama, jam, durasi):
        self.nama = nama
        self.jam = jam
        self.durasi = durasi

    # Fungsi bayar() di override
    def bayar(self):
        print("- Biaya 1 jam adalah Rp. 150.000")
        total_diskon = self.diskon()
        total = int(self.harga1jam*self.durasi) - total_diskon
        print("Harga yang harus dibayar = Rp", int(total))
        payment = int(input("Masukkan uang anda: "))
        self.total = int(total)
        return payment, int(total)
        

    
    def diskon(self):
        total_diskon = 0
        if self.durasi >= 2:
            total_diskon = self.harga1jam*(20/100)
        return total_diskon
        



    
class RentalLapangan:
    # data member private
    __pemasukan_harian = 0

    # data member public
    daftar = []

    def __init__(self,pelanggan=None):
        self.pelanggan = pelanggan
    
    @classmethod
    def setor(cls,total):
        cls.__pemasukan_harian+=total
    
    @classmethod
    def simpan_pemasukan_harian(cls):
        try:
            with open("rincian_pemasukan.csv", "a") as file:
                writer = csv.DictWriter(file, fieldnames=["pemasukan", "tanggal"])
                writer.writerow({"pemasukan": cls.__pemasukan_harian, "tanggal": tanggal})
        except FileNotFoundError:
            file = open("rincian_pemasukan.csv","w")
            file.close()

    @classmethod
    def tampilkan_menu(cls):
        print('Selamat datang!')
        print("1. Booking lapangan")
        print("2. Jadwal reservasi")
        print("3. Cancel reservasi")
        print("4. Keluar")
    
    @classmethod
    def tampilkan_daftar(cls):
        sorted_daftar = sorted(cls.daftar, key=lambda x: x['jam'])
        print("Nama\t\tJam mulai   Jam berakhir")
        print("=========================================")
        for slot in sorted_daftar:
            # print nama
            print(slot['nama'].title(),end="")
            if len(slot['nama']) < 16:
                for _ in range(16 - len(slot['nama'])):
                    print(" ",end="")
                print(str(slot['jam'])+".00\t   ",str(slot['jam']+1)+".00")
    



    
    def simpan_data_pelanggan(self,pelanggan):
        with open("riwayat_pelanggan.csv", "a") as file:
            writer = csv.DictWriter(file, fieldnames=["nama", "tanggal","total"])
            writer.writerow({"nama": pelanggan.nama, "tanggal": tanggal, "total" : pelanggan.total})
    
    @classmethod
    def cek_status_pelanggan(cls,nama):
        try:
            with open("riwayat_pelanggan.csv","r") as file:
                csv_reader = csv.DictReader(file, fieldnames=["nama","tanggal"])
                j = 0
                for row in csv_reader:
                    if row['nama'] == nama:
                        j+=1
                if j >= 3:
                    return True
                else:
                    return False
        except FileNotFoundError:
            file = open("riwayat_pelanggan.csv","w")
            csv_writer = csv.writer(file)
            csv_writer.writerow(["nama","tanggal","total"])
            file.close()
                
    
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
                new_data["total"] = getattr(self.pelanggan,'total')
                self.daftar.append(new_data)
                j+=1
            return True
        else:
            print("Maaf kami tidak melayani reservasi sebelum jam 10 pagi atau setelah jam 10 malam")
            return False

    @classmethod
    def hapus_data_pelanggan(cls):
        nama = input("Masukkan nama: ")



        # refund 50% uang
        cls.refund(nama)

        with open("riwayat_pelanggan.csv", 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['nama'] == nama and row['tanggal'] == str(tanggal):
                    rows = row
                    rows['total'] = int(row['total']) - (int(row['total'])*2)
                    with open("riwayat_pelanggan.csv", 'a', newline='') as file:
                        writer = csv.DictWriter(file, fieldnames=["nama","tanggal","total"])
                        writer.writerow(rows)
                        break

        cls.daftar = [d for d in cls.daftar if nama not in d.values()]
    
    @classmethod
    def refund(cls,nama):
        for slot in cls.daftar:
            if slot['nama'] == nama:
                cls.__pemasukan_harian-=slot['total']
                break
        


    def rincian_pemesanan(self,pelanggan):
        print("\nRincian pemesanan")
        print("======================")
        print(f"Nama: {pelanggan.nama.title()}\nJam mulai: {pelanggan.jam}.00\nJam berakhir: {pelanggan.jam+pelanggan.durasi}.00\n======================\n")





def main():
    # tampilkan menu
    RentalLapangan.tampilkan_menu()
    pilihan = int(input(""))
    while True:
        if pilihan == 1:
            # input data calon pelanggan
            nama,jam,durasi = Pelanggan.input_data()

            # cek apakah pelanggan lama
            status = RentalLapangan.cek_status_pelanggan(nama)
            
            if status == True:
                # buat objek pelanggan lama
                calon_p = PelangganLama(nama,jam,durasi)
            else:
                # buat objek pelanggan
                calon_p = Pelanggan(nama,jam,durasi)
            
            # buat objek rental
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
                    rental.simpan_data_pelanggan(calon_p)

                    # rental menyetor uang ke data member private pemasukan harian
                    RentalLapangan.setor(total)

                    # rental menampilkan rincian pemesanan pelanggan
                    rental.rincian_pemesanan(calon_p)
                else:
                    print("Maaf uang anda tidak mencukupi")      
            else:
                print("Maaf jam tidak tersedia untuk direservasi")
        elif pilihan == 2:
            # Tampilkan daftar pelanggan
            RentalLapangan.tampilkan_daftar()
        elif pilihan == 3:
            # cancel
            RentalLapangan.hapus_data_pelanggan()
        elif pilihan == 4:
            RentalLapangan.simpan_pemasukan_harian()
            break
        else:
            print("Mohon masukkan input yang sesuai!")

        # tampilkan menu kembali
        RentalLapangan.tampilkan_menu()
        pilihan = int(input(""))


if __name__ == "__main__":
    main()
