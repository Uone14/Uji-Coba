import os
import time
import prettytable 
import csv


def clear_screen():
    os.system('cls')

def loading(): 
    for i in range(5):
        print("\r{0}  {1}".format("Loading ","."*i),end="")
        time.sleep(0.5)

def batas():
    print('='*43)

def exit():
    clear_screen()
    batas()
    print("TERIMAKASIH SUDAH BERBELANJA".center(43))
    batas()

def daftar_menu():
    print('='*45)
    print('| WELCOME TO VEGETABLE MARKET |'.center(43))
    print('='*45)
    print('MENU'.center(39))
    with open('product.csv ','r') as fp :
        print((prettytable.from_csv(fp)))

simpan_sayur = []
total_harga = []
simpanjumlah = []
total_harga_sayur = []
satuan = []

def Tambah_pesanan():
    with open('product.csv', 'r') as hargaproduk:
        harga = []
        reader = csv.DictReader(hargaproduk)
        for row in reader:
            harga.append(row)
        batas()
        print('- Masukkan Data Sesuai Menu -'.center(43))
        print('- Data Tidak Akan Diinput Jika Tidak Sesuai -'.center(43))
        print('='*43)
        sayur = input('Masukkan Sayur: '.lower())
        jumlah = int(input('Masukkan Jumlah: '))
        for x in harga:
            if sayur in x['NamaBarang']:
                total = int(x['harga'])* jumlah
                total_harga_sayur.append(total)
                simpan_sayur.append(sayur)
                simpanjumlah.append(jumlah)
                satuan.append(x['satuan'])
                print(f'sayur {sayur} berhasil ditambakan ')
            
    pilihan = input('Tambah Pesanan Lagi (y/n): ')
    if pilihan == 'y':
        os.system('cls')
        daftar_menu()
        Tambah_pesanan()
    elif pilihan == 'n':
        clear_screen()
        daftar_menu()
        menu_aplikasi()
    else:
        print('Pilihan tidak tersedia')
        Tambah_pesanan()
    
def menu_aplikasi():
    print("="*45)
    print('1. Tambah Pesanan')
    print('2. Hapus Pesanan')
    print('3. Pesanan Anda')
    print('4. Chekout Pesanan Anda')
    print('5. Exit')
    print("="*45)

    opsi = input('Pilih Menu: ')
    if opsi == '1':
        Tambah_pesanan()
    elif opsi == '2':
        hapus_pesanan()
    elif opsi == '3':
        pesanan_anda()
    elif opsi == '4':
        bayar()
    elif opsi == '5':
        home()
    else:
        menu_aplikasi()

def lanjut():
    clear_screen()
    lanjut = input('''Tekan 'y' untuk menghapus lagi
    Tekan 'n' untuk kembali ke menu: ''')

    if lanjut == 'y':
        hapus_pesanan()
    elif lanjut == 'n':
        clear_screen()
        daftar_menu()
        menu_aplikasi()
    else:
        print('Inputan Anda Salah')
        lanjut()

def hapus_pesanan():
    os.system('cls')
    index = 0
    batas()
    print('Checkout Pesanan Anda'.center(43, '='))
    batas()
    print("Kode|",'Nama Sayur\t|','Jumlah |','Harga\t')
    for i in simpan_sayur:
        print((simpan_sayur.index(i)+1) ,'   |', (i),'\t\t','|',(simpanjumlah[index]),'\t |Rp.',(total_harga_sayur[index]),sep="")
        index += 1

    print('='*43)
    print('| Hapus Pesanan |'.center(43))
    print('='*43)
    hapus = input('pesanan yang ingin dihapus: ')
    if hapus in simpan_sayur:
        simpan_sayur.remove(hapus)
        print(f'Pesanan {hapus} Berhasil Di Hapus')
        time.sleep(1.5)
        lanjut()
    else:
        print('Pesanan Tidak Terdaftar')
        lanjut()

def pesanan_anda():
    os.system('cls')
    if simpan_sayur == []:
        batas()
        print('Belum Ada Pesanan'.center(43,' '))
        batas()
        keluar = input('Ingin Keluar (y/n): ')
        if keluar == 'y':
            clear_screen()
            daftar_menu()
            menu_aplikasi()
        else:
            pesanan_anda()

    elif simpan_sayur != []:
        index = 0
        print("="*57)
        print('Daftar Pesanan'.center(57, '='))
        print("="*57)
        print("Kode|",'Nama Sayur\t|','Jumlah |','Satuan \t|','Harga\t')
        for i in simpan_sayur:
            print((simpan_sayur.index(i)+1) ,'   |', (i),'\t\t','|',(simpanjumlah[index]),'\t |',(satuan[index]), '\t\t|Rp.', (total_harga_sayur[index]),sep="")
            index += 1
        print("="*57)

        pilihan = input('Apakah ingin keluar (y/n)?: ')
        if pilihan == 'y':
            clear_screen()
            daftar_menu()
            menu_aplikasi()
        else:
            pesanan_anda()

def bayar():
    os.system('cls')
    index = 0
    batas()
    print('Checkout Pesanan Anda'.center(43, '='))
    batas()
    print("Kode|",'Nama Sayur\t|','Jumlah |','Harga\t')
    for i in simpan_sayur:
        print((simpan_sayur.index(i)+1) ,'   |', (i),'\t\t','|',(simpanjumlah[index]),'\t |Rp.',(total_harga_sayur[index]),sep="")
        index += 1
    batas()
    print("Silahkan Melakukan Pembayaran di Kasir")
    batas()
    input("Tekan Enter Untuk Kembali")
    clear_screen()
    simpan_sayur.clear()
    daftar_menu()
    menu_aplikasi()
    
def back():
    print("")
    input("Tekan Enter Untuk Kembali")
    menu()

def reg():
    clear_screen()
    print('-'*35)
    print('MENU REGISTRASI'.center(35))
    print('-'*35)

    with open('akun.csv', mode='a', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        username = input("Masukkan Username : ")
        sandi = input("Masukkan Password : ")
        sandi2 = input("Masukkan Ulang Password : ")
        if sandi == sandi2:
            writer.writerow([username, sandi])
            print("Registrasi Berhasil, Silahkan Login")
            time.sleep(1)
        else:
            print("Konfirmasi Password Salah")
            back()
    login()

def login():
    clear_screen()
    print('-'*30)
    print('Menu Login'.center(30))
    print('-'*30)
    username = input("Masukkan Username Anda : ")
    sandi = input("Masukkan Password Anda : ")
    with open('akun.csv', mode='r') as csv_file:
        bacafile = csv.reader(csv_file, delimiter=',')
        for row in bacafile:
            if row == [username, sandi]:
                print()
                print("Anda Berhasil Login")
                input("Tekan Enter Untuk Melanjutkan...")
                loading()
                home()
                return True
    print("Username atau Password Salah")
    back()
    return False

def menu():
    clear_screen()
    print('-'*40)
    print("Silahkan Login atau Registrasi".center(40))
    print('-'*40)
    print("[1] Login")
    print("[2] Registrasi")
    print("[3] Keluar")
    pilih = input("Pilih menu> ")
    if pilih == '1':
        login()
    elif pilih == '2':
        reg()
    elif pilih == '3':
        exit()
    else:
        print("Pilih menu yang tersedia ya...")
        input("Tekan Enter Untuk Kembali")
        menu()

def home():
    clear_screen()
    print('-'*40)
    print('Selamat Datang di Toko'.center(40))
    print('-'*40)
    print('Apa yang Anda Inginkan?')
    print("[1] Menu Aplikasi")
    print("[2] Reset Password")
    print("[3] Kembali")
    user = input("Pilih Menu> ")
    if user == '1':
        clear_screen()
        daftar_menu()
        menu_aplikasi() 
    elif user == '2':
        time.sleep(1)
        reset()
    elif user == '3':
        menu()
    else:
        print('Menu tidak tersedia')
        home()

def reset():
    clear_screen()
    databaru=[]
    
    with open("akun.csv", mode='r', newline="") as csv_file:
      reader = list(csv.reader(csv_file, delimiter=','))
      print('-'*35)
      print("MENU GANTI PASSWORD".center(35))
      print('-'*35)
      username = input("Masukkan Username Anda : ")
      datasementara = reader

      for row in reader:
          for field in row:
                if field == username:
                    databaru.append(row)
                    baru = input("Masukkan Password yang Baru : ")
                    databaru[0][1] = baru
                          
      sandibaru(databaru,datasementara)
        
def sandibaru(databaru,datasementara):
    for index, row in enumerate(datasementara):
        for field in row:
            if field == databaru[0]:
                datasementara[index] = databaru
    
    with open("akun.csv","w",newline="") as csv_file:
        Writer = csv.writer(csv_file)
        Writer.writerows(datasementara)
        loading()
        print("\nPassword Berhasil Diperbarui")
        time.sleep(1)
        clear_screen()
    menu()
menu()