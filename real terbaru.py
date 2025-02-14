import pandas as pd
import os
import time as ts
import datetime as dt
import csv
from tabulate import tabulate

def clear():
    os.system('cls')

#------------------------------------------------ FUNGSI BOOKING -------------------------------------------------
def pemesanan ():
        nama_file = 'real_data.csv'
        with open(nama_file, 'r') as file:
            df = pd.read_csv(file)
        data_plat= df['PLAT'].tolist()
        data_pemesan = pd.read_csv('real_data.csv')
        data_pemesan1 = pd.read_csv("check_in.csv")
        real_data = pd.concat([data_pemesan,data_pemesan1],ignore_index= True)
        jumlah_loket_A = (real_data['LOKASI PARKIR'] == 'A').sum()
        jumlah_loket_B = (real_data['LOKASI PARKIR'] == 'B').sum()
        jumlah_loket_C = (real_data['LOKASI PARKIR'] == 'C').sum()
        total_mobil = jumlah_loket_A + jumlah_loket_B
        total_motor = jumlah_loket_C
        
        if total_motor>=100 and total_mobil>=100 :
            print(f'''
{"="*55}
|{"PARKIR MOTOR DAN MOBIL PENUH SILAHKAN CARI TEMPAT LAIN".center(48)}|
{"="*55}''')
            return

        elif total_mobil >= 100 :
            print(f'''
{"="*50}
|{"PARKIR MOBIL PENUH".center(48)}|
{"="*50}''')
            while True:
                ulang_mesan = str(input("\tAPAKAH ANDA INGIN PERGI KE MENU Y/N: "))
                ulang_mesan = ulang_mesan.upper()
                if ulang_mesan == 'Y' :
                    start()
                elif ulang_mesan == 'N':
                    break
                else:
                    print(f'''
{"="*50}
|{"HARAP HANYA MEMASUKKAN Y/N SAJA".center(48)}|
{"="*50}''')

        elif total_motor >= 100:
            print(f'''
{"="*50}
|{"PARKIR MOTOR PENUH".center(48)}|
{"="*50}''')
            while True:
                ulang_mesan = str(input("\tAPAKAH ANDA INGIN PERGI KE MENU Y/N: "))
                ulang_mesan = ulang_mesan.upper()
                if ulang_mesan == 'Y' :
                    start()
                elif ulang_mesan == 'N':
                    break
                else:
                    print(f'''
{"="*50}
|{"HARAP HANYA MEMASUKKAN Y/N SAJA".center(48)}|
{"="*50}''')

        while True :
            os.system("cls")
            print(f'''
    {"="*50}
    |{"SIPEPASWA".center(48)}|
    |{"(Sistem Pembookingan Parkir Swalayan)".center(48)}|
    {"="*50}
    |{"Mudah, Aman, dan Nyaman".center(48)}|
    {"="*50}''')
            
            plat_baru= (input("\tPLAT NOMOR: "))
            plat_baru= plat_baru.upper()
            if len(plat_baru)>9 or len(plat_baru)<3:
                print(f'''
    {"="*50}
    |{"HARAP MASUKKAN PLAT YANG BENAR".center(48)}|
    {"="*50}''')
            elif plat_baru in data_plat :
                print(f'''
    {"="*50}
    |{"PLAT SUDAH TERDAFTAR".center(48)}|
    {"="*50}''')
                while True :
                    ulang_plat= (input("\tAPAKAH ANDA INGIN MENGULANG Y/N: "))
                    ulang_plat= ulang_plat.upper()
                    
                    if ulang_plat == 'Y':
                        break
                    elif ulang_plat =='N':
                        os.system("cls")
                        print(f'''
    {"="*50}
    |{"TERIMA KASIH SUDAH MENGGUNAKAN".center(48)}|
    {"="*50}''')
                        break
                    else :
                        print(f'''
    {"="*48}
    |{"HARAP HANYA MEMASUKKAN Y/N".center(46)}|
    {"="*48}''')
                # if ulang_plat=='N':
                #     return
            else:
                print(f'''    {"="*50}''')
                konfirmasi_plat= str(input("\tAPAKAH ANDA YAKIN PLAT NYA BENAR Y/N: "))
                konfirmasi_plat= konfirmasi_plat.upper()
                if konfirmasi_plat == 'Y':
                    os.system("cls")
                    print(f'''
    {"="*50}
    |{"SILAHKAN LANJUT KE TAHAP SELANJUTNYA".center(48)}|
    {"="*50}''')
                    break
                elif konfirmasi_plat == 'N' :
                    continue
                else:
                    print(f'''
    {"="*50}
    |{"HARAP HANYA MEMASUKKAN Y/N SAJA".center(48)}|
    {"="*50}''')
                    
        while True:
            print(f'''
    {"="*50}''')
            nama_baru = str(input("\tNAMA: "))
            nama_baru = nama_baru.upper()
            print(f'''    {"="*50}''')
            ulang_nama= (input("\tAPAKAH NAMA SUDAH BENAR Y/N: "))
            ulang_nama= ulang_nama.upper()
            if ulang_nama == 'Y':
                os.system("cls")
                print(f'''
    {"="*50}
    |{"SILAHKAN LANJUT KE TAHAP SELANJUTNYA".center(48)}|
    {"="*50}''')
                break
            elif ulang_nama == 'N':
                continue
            else:
                print(f'''
    {"="*50}
    |{"HARAP HANYA MEMASUKKAN Y/N SAJA".center(48)}|
    {"="*50}''')


        while True :
            print(f'''
    {"="*50}''')
            jenis_kendaraan= str(input("\tmasukkan kendaraan MOBIL/MOTOR: "))
            jenis_kendaraan= jenis_kendaraan.upper()
            if jenis_kendaraan in ['MOBIL','MOTOR']:
                print(f'''    {"="*50}''')
                lanjut_kendaraan= str(input("\tAPAKAH JENIS KENDARAAN SUDAH BENAR Y/N: "))
                lanjut_kendaraan= lanjut_kendaraan.upper()
                if lanjut_kendaraan == 'Y' :
                    os.system("cls")
                    print(f'''
    {"="*50}
    |{"SILAHKAN LANJUT KE TAHAP SELANJUTNYA".center(48)}|
    {"="*50}''')
                    break
                elif lanjut_kendaraan == 'N' :
                    continue
                else:
                    print(f'''
    {"="*50}
    |{"HARAP HANYA MEMASUKKAN Y/N SAJA".center(48)}|
    {"="*50}''')
            else :
                print(f'''
    {"="*50}
    |{"HARAP HANYA MEMASUKKAN MOBIL/MOTOR SAJA".center(48)}|
    {"="*50}''')

        while True :
                print(f'''
    {"="*50}''')
                lokasi_baru = str(input("\tmasukkan LOKET A/B/C "))
                lokasi_baru= lokasi_baru.upper()
                if (lokasi_baru in ['C'] and jenis_kendaraan == 'MOBIL'):
                    os.system("cls")
                    print(f'''
    {"="*50}
    |{"LOKET C HANYA UNTUK MOTOR".center(48)}|
    {"="*50}''')
                elif (lokasi_baru in ["A","B",] and jenis_kendaraan=='MOTOR'):
                    os.system("cls")
                    print(f'''
    {"="*50}
    |{"LOKET C HANYA UNTUK MOTOR".center(48)}|
    {"="*50}''')
                elif lokasi_baru in ["A","B","C"]:
                    print(f'''    {"="*50}''')
                    ulang_lokasi =str(input("\tAPAKAH ANDA SUDAH BENAR Y/N: "))
                    ulang_lokasi= ulang_lokasi.upper()
                    if ulang_lokasi == "Y":
                        break
                    elif ulang_lokasi == "N":
                        continue
                    else :
                        print(f'''
    {"="*50}
    |{"HARAP HANYA MEMASUKKAN Y/N SAJA".center(48)}|
    {"="*50}''')
                else:
                    print(f'''
    {"="*50}
    |{"HARAP PILIH LOKASI YANG SUDAH DITENTUKAN".center(48)}|
    {"="*50}''')

        data_user_baru={
        "NAMA":[nama_baru],
        "PLAT":[plat_baru],
        "JENIS KENDARAAN":[jenis_kendaraan],
        "LOKASI PARKIR":[lokasi_baru]}

        os.system("cls")
        print(f'''
    {"="*50}
    |{"BIODATA".center(48)}|
    {"="*50}''')
        print (f'''
\tNAMA            : {nama_baru}
\tPLAT            : {plat_baru}
\tJENIS KENDARAAN : {jenis_kendaraan}
\tLOKASI PARKIR   : {lokasi_baru}''')
        print(f'''
    {"="*50}''')
        upload = str(input("\tAPAKAH ANDA YAKIN INGIN MEMESAN Y/N: "))
        upload = upload.upper()
        if upload == "Y" :
            os.system("cls")
            print(f'''
    {"="*50}
    |{"TERIMAKASIH SUDAH MEMESAN".center(48)}|
    {"="*50}''')
            dataf= pd.DataFrame(data_user_baru)
            with open(nama_file, 'r') as file2:
                datat = pd.read_csv(file2)
            data_baru = pd.concat([dataf,datat],ignore_index=True)
            with open(nama_file, 'w', newline='') as file:
                data_baru.to_csv(file, index=False)

            kembali_menu = str(input("\tAPAKAH ANDA INGIN KEMBALI KE MAIN MENU Y/N: "))
            kembali_menu = kembali_menu.upper()
            if kembali_menu == 'Y':
                start()
            elif kembali_menu == 'N':
                os.system("cls")
                print(f'''
{"="*50}
|{"TERIMAKASIH SUDAH MEMESAN".center(48)}|
{"="*50}''')

        elif upload == "N":
            os.system("cls")
            print(f'''
    {"="*50}
    |{"SILAHKAN MENGULANG DARI AWAL".center(48)}|
    {"="*50}''')
            return

#------------------------------------------------ FUNGSI CHECK IN -------------------------------------------------
def check_in ():
    nama_file1= 'real_data.csv'
    with open(nama_file1, 'r') as file:
            data_pemesan = pd.read_csv(file)
    while True:
        try:
            os.system("cls")
            print(f'''
    {"="*50}
    |{"CHECK IN".center(48)}|
    |{"="*48}|
    |{"SIPEPASWA".center(48)}|
    |{"="*48}|''')
            cek_plat = input("\tMASUKKAN PLAT YANG SUDAH TERDAFTAR: ")
            cek_plat= cek_plat.upper()
            data_plat = data_pemesan['PLAT'].tolist()
            baris_data = data_plat.index(cek_plat)
            biodata = data_pemesan.iloc[baris_data]
            biodata = biodata.tolist()
            print(f'''
    {"="*50}
    |{"SILAHKAN LANJUT KE TAHAP SELANJUTNYA".center(48)}|
    {"="*50}''')
            break
        except ValueError:
            print(f'''
    {"="*50}
    |{"PLAT TIDAK ADA DI DALAM LIST".center(48)}|
    {"="*50}''')
    
    while True :
        baris_data = data_plat.index(cek_plat)
        biodata = data_pemesan.iloc[baris_data]
        biodata = biodata.tolist()
        cek_nama = str(input("\tMASUKKAN NAMA: "))
        cek_nama= cek_nama.upper()
        if cek_nama == biodata[0]:
            print(f'''
    {"="*50}
    |{"SILAHKAN LANJUT KE TAHAP SELANJUTNYA".center(48)}|
    {"="*50}''')
            break
        else :
            print(f'''
    {"="*50}
    |{"HARAP MEMASUKKAN NAMA YANG SUDAH TERDAFTAR".center(48)}|
    {"="*50}''')
            continue

    jam_masuk = ts.ctime(ts.time())
    jam_masuk = jam_masuk.split(" ")
    jam_masuk = jam_masuk[-2:-1]
    durasi = "ONGOING"
    jam_keluar = "ONGOING"
    tanggal = tanggal= dt.datetime.now()
    tanggal = str(tanggal)
    tanggal = tanggal.split(" ")

    new_data_user = {
        "NAMA"           : [biodata[0]],
        "PLAT"           : [biodata[1]],
        "JENIS KENDARAAN": [biodata[2]],
        "LOKASI PARKIR"  : [biodata[3]],
        "TANGGAL"        : [tanggal[0]] ,
        "JAM MASUK"      : [jam_masuk],
        "JAM KELUAR"     : [durasi],
        "DURASI"         : [jam_keluar]}
    
    os.system("cls")
    print(f'''
    {"="*50}
    |{"BIODATA".center(48)}|
    {"="*50}''')
    print (f'''
\tNAMA            : {biodata[0]}
\tPLAT            : {biodata[1]}
\tJENIS KENDARAAN : {biodata[2]}
\tLOKASI PARKIR   : {biodata[3]}
\tTANGGAL         : {tanggal[0]}
\tJAM MASUK       : {jam_masuk}
\tJAM KELUAR      : {durasi}
\tDURASI          : {jam_keluar}''')

    print(f'''
    {"="*50}
    |{"BERHASIL MELAKUKAN CHECK IN".center(48)}|
    {"="*50}''')
    
    datax= pd.DataFrame(new_data_user)
    nama_file2= 'check_in.csv'
    with open (nama_file2, 'r') as file1:
        datay=pd.read_csv(file1)
    new_data = pd.concat([datax,datay],ignore_index=True)
    with open(nama_file2, 'w', newline='') as file:
        new_data.to_csv(file, index=False)


    data_pemesan = data_pemesan.drop(baris_data)

    with open(nama_file1, 'w', newline='') as file:
        data_pemesan.to_csv(file, index=False)
    
    kembali_menu = str(input("\tAPAKAH ANDA INGIN KEMBALI KE MAIN MENU Y/N: "))
    kembali_menu = kembali_menu.upper()
    if kembali_menu == 'Y':
        start()
    elif kembali_menu == 'N':
        os.system("cls")
        print(f'''
{"="*50}
|{"TERIMAKASIH SUDAH MEMESAN".center(48)}|
{"="*50}''')

#------------------------------------------------ FUNGSI CHECK OUT -------------------------------------------------
def check_out():
    os.system("cls")
    nama_file3 = 'check_in.csv'
    with open(nama_file3, 'r') as file:
        data_check_in = pd.read_csv(file)
    
    while True:
        # os.system("cls")
        print(f'''
{"="*50}
|{"CHECK OUT".center(48)}|
|{"="*48}|
|{"SIPEPASWA".center(48)}|
|{"="*48}|''')
        cek_plat = input(" MASUKKAN PLAT NOMER YANG SUDAH CHECK IN: ")
        cek_plat = cek_plat.upper()
        kendaraan = data_check_in[data_check_in['PLAT'] == cek_plat]
        if not kendaraan.empty:
            os.system("cls")
            print(f'''
{"="*50}
|{"SILAHKAN LANJUT KE TAHAP SELANJUTNYA".center(48)}|
{"="*50}''')
            break
        else:
            os.system("cls")
            print(f'''
{"="*50}
|{"PLAT TIDAK MELAKUKAN CHECK IN".center(48)}|
{"="*50}''')
    
    waktu_keluar = dt.datetime.now()
    jam_keluar = waktu_keluar.strftime("%H:%M:%S")
    tanggal_masuk = kendaraan['TANGGAL'].iloc[0]
    jam_masuk = kendaraan['JAM MASUK'].iloc[0]
    jam_masuk = jam_masuk.strip("[]'")
    waktu_masuk = dt.datetime.strptime(f"{tanggal_masuk} {jam_masuk}", "%Y-%m-%d %H:%M:%S")
    
    durasi = waktu_keluar - waktu_masuk
    jam_parkir = durasi.total_seconds() / 3600
    
    nama_file4 = 'daftar_harga.csv'
    with open(nama_file4, 'r') as file3:
        df = pd.read_csv(file3)
    
    if kendaraan['JENIS KENDARAAN'].iloc[0] == 'MOTOR':
        tarif_per_jam = df['Tarif per jam (Rp)'].iloc[0]
    else:
        tarif_per_jam = df['Tarif per jam (Rp)'].iloc[1]
    
    jam_parkir = max(1, jam_parkir)
    biaya = round(jam_parkir * tarif_per_jam)
    

    while True:
        try:
            print(f'HARGA YANG HARUS DIBAYAR ADALAH : Rp {biaya:,}')
            pembayaran = int(input("MASUKKAN PEMBAYARAN: "))
            if pembayaran < biaya:
                print("PEMBAYARAN KURANG! HARAP MASUKKAN JUMLAH YANG SESUAI.")
            else:
                kembalian = pembayaran - biaya
                os.system("cls")
                print(f'''
{"="*50}
|{"BIODATA".center(48)}|
{"="*50}''')
                print(f'''
                NAMA            : {kendaraan['NAMA'].iloc[0]}
                PLAT            : {kendaraan['PLAT'].iloc[0]}
                JENIS KENDARAAN : {kendaraan['JENIS KENDARAAN'].iloc[0]}
                LOKASI PARKIR   : {kendaraan['LOKASI PARKIR'].iloc[0]}
                TANGGAL MASUK   : {tanggal_masuk} 
                JAM MASUK       : {jam_masuk}
                TANGGAL KELUAR  : {waktu_keluar.strftime("%Y-%m-%d")}
                JAM KELUAR      : {jam_keluar}
                DURASI          : {durasi}
                BIAYA           : Rp {biaya:,}
                KEMBALIAN       : Rp {kembalian:,}
                ''')

                new_data_checkout = {
                    'NAMA': kendaraan['NAMA'].iloc[0],
                    'PLAT': kendaraan['PLAT'].iloc[0],
                    'JENIS KENDARAAN': kendaraan['JENIS KENDARAAN'].iloc[0],
                    'LOKASI PARKIR': kendaraan['LOKASI PARKIR'].iloc[0],
                    'TANGGAL MASUK': tanggal_masuk,
                    'JAM MASUK': jam_masuk,
                    'TANGGAL KELUAR': waktu_keluar.strftime("%Y-%m-%d"),
                    'JAM KELUAR': jam_keluar,
                    'DURASI': str(durasi),
                    'BIAYA': f"Rp {biaya:,}",
                    'KEMBALIAN': f"Rp {kembalian:,}"
                }

                nama_file5 = 'check_out.csv'
                try:
                    with open(nama_file5, 'a', newline='') as file5:
                        pd.DataFrame([new_data_checkout]).to_csv(file5, index=False, header=file5.tell() == 0)
                except Exception as e:
                    print(f"Error menimpan check-out data: {e}")
                
                try:
                    data_check_in = data_check_in[data_check_in['PLAT'] != cek_plat]
                    data_check_in.to_csv(nama_file3, index=False)
                    print(f'''
{"="*50}
|{"BERHASIL MELAKUKAN CHECK OUT".center(48)}|
{"="*50}''')
                except Exception as e:
                    print(f"Error menghapus data check-in: {e}")
                
                break
        except ValueError:
            print("HARAP HANYA MEMASUKKAN ANGKA")

#------------------------------------------------ FUNGSI TAMPILAN EXIT -------------------------------------------------
def awalan():
    clear()
    print(f'''
    {"="*50}
    |{"SIPEPASWA".center(48)}|
    {"="*50}
    |{"".center(48)}|
    |{"TERIMAKASIH dan SELAMAT SAMPAI TUJUAN".center(48)}|
    |{"".center(48)}|
    {"="*50}
    ''')

#------------------------------------------------ FUNGSI MAIN MENU -------------------------------------------------
def main_menu():
    clear()
    print(f'''
    +{"="*48}+
    |{"SIPEPASWA".center(48)}|
    |{"(Sistem Pembookingan Parkir Swalayan)".center(48)}|
    +{"="*48}+
    |{"Mudah, Aman, dan Nyaman".center(48)}|
    +{"="*48}+
    |{"Main Menu".center(48)}|
    +{"="*48}+
    |{"[1]. Login admin".ljust(48)}|
    |{"[2]. Cek Harga".ljust(48)}|
    |{"[3]. Cek tempat parkir".ljust(48)}|
    |{"[4]. Booking".ljust(48)}|
    |{"[5]. Check-In".ljust(48)}|
    |{"[6]. Check-Out".ljust(48)}|
    |{"[7]. Exit".ljust(48)}|
    +{"="*48}+
    ''')

#------------------------------------------------ FUNGSI LOGIN ADMIN -------------------------------------------------
def login_admin(): 
    clear()           
    data_account = [] 
    with open("data_admin.csv", mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            data_account.append(row)

    # Loop buat meminta input username dan password klo salah ngulang cuy
    while True:
        clear()
        print("+"+"-"*58+"+")
        print("|"+"LOGIN ADMIN".center(58)+"|")
        print("+"+"-"*58+"+")
        username = input("Masukkan Username: ")
        password = input("Masukkan Password: ")
        print("="*60)

        # ngecek ada apa nggak biar bisa masuk
        login_berhasil = False
        for data in data_account:
            if username == data['username'] and password == data['password']:
                login_berhasil = True
                input("Selamat Anda Berhasil Login. Klik \"ENTER\" Untuk Melanjutkan!")
                menu_admin()  # Panggil menu_admin() jika login berhasil
                break  # Keluar dari loop setelah login berhasil
        
        if login_berhasil:
            break  # Keluar dari loop utama jika login berhasil
        else:
            input("Username atau Password Salah. Klik \"ENTER\" Untuk Coba Lagi!")
            print("-"*60)   
            
#------------------------------------------------ FUNGSI MAIN MENU ADMIN -------------------------------------------------
def menu_admin():
    clear()
    print(f'''
    +{"="*50}+
    |{"+ SIPEPASWA +".center(50)}|
    +{"="*50}+
    |{"Mudah, Aman, dan Nyaman".center(50)}|
    +{"="*50}+
    |{"MENU ADMIN".center(50)}|
    +{"="*50}+
    |{"[1]. History User".ljust(50)}|
    |{"[2]. Kelola Data Pemesanan".ljust(50)}|
    |{"[3]. Lihat Kendaraan Masuk".ljust(50)}|
    |{"[4]. Ubah Harga".ljust(50)}|
    |{"[5]. Kembali".ljust(50)}|
    +{"="*50}+      
    ''')

    opsi = input("Masukkan Pilihan: ")
    if opsi == "1":
        history()
    elif opsi == "2":
        kelola_pemesanan()
    elif opsi == "3":
        lihat_kendaraan_in()
    elif opsi== "4":
        ubah_harga()
    elif opsi == "5":
        start()
    else:
        input("Pilihan tidak tersedia,klik \"ENTER\" Untuk Pilih Ulang")
        menu_admin()

#------------------------------------------------ FUNGSI CEK HARGA -------------------------------------------------
def cek_harga():
    clear()
    
    file_path = 'daftar_harga.csv'
    df = pd.read_csv(file_path)
    df = df.reset_index(drop=True)
    df.index+=1

    print("=================================================")
    print("               Daftar Harga Parkir")
    print("=================================================")
    print(tabulate(df, headers='keys', tablefmt='fancy_grid'))
    input("\nKlik \"ENTER\" untuk kembali!")
    start()

#-------------------------------------------- FUNGSI CEK TEMPAT PARKIR ----------------------------------------------
def cek_tempat_parkir():
    clear()
    print("\tDenah Sederhana Tempat Parkir".center(49))
    print("\t"+"-"*49)
    print("\t|\t\t|\t\t|\t\t|")
    print("\t|\tLOKET A\t|\tLOKET B\t|\tLOKET C\t|")
    print("\t|\t\t|\t\t|\t\t|")
    print("---------\t\t\t\t\t\t---------")
    print("|\t\t\t\t\t\t\t\t|")
    print("|\t"+"-"*49,"\t|")
    print("|K\t|\t\t\t\t\t\t|M\t|")
    print("|E\t|\t\t\t\t\t\t|A\t|")
    print("|L\t|\t\tSWALAYAN\t\t\t|S\t|")
    print("|U\t|\t\t\t\t\t\t|U\t|")
    print("|A\t|\t\t\t\t\t\t|K\t|")
    print("|R\t|\t\t\t\t\t\t|\t|")
    print("|\t"+"-"*49,"\t|")
    print("|\t|\t\t\t\t\t\t|\t|")
    print("--     --\t\t\t\t\t\t--     --")
    print("\n")

    data_pemesan = pd.read_csv('real_data.csv')
    data_pemesan1 = pd.read_csv("check_in.csv")
    real_data = pd.concat([data_pemesan,data_pemesan1],ignore_index= True)
    jumlah_loket_A = (real_data['LOKASI PARKIR'] == 'A').sum()
    jumlah_loket_B = (real_data['LOKASI PARKIR'] == 'B').sum()
    jumlah_loket_C = (real_data['LOKASI PARKIR'] == 'C').sum()
    print(f'''{"-"*38}
|{"Data Jumlah Kendaraan".center(36)}|
{"-"*38}
|{f"Jumlah kendaraan di loket A: {jumlah_loket_A}/50".ljust(36)}|
|{f"Jumlah kendaraan di loket B: {jumlah_loket_B}/50".ljust(36)}|
|{f"Jumlah kendaraan di loket C: {jumlah_loket_C}/100".ljust(36)}|
{"-"*38}''')

    # Menampilkan total kendaraan
    total_mobil = jumlah_loket_A + jumlah_loket_B
    total_motor = jumlah_loket_C
    print(f'''|{f"Total mobil: {total_mobil}/100".ljust(36)}|
|{f"Total motor: {total_motor}/100".ljust(36)}|
{"-"*38}''')
    
    print(f'''
{"="*38}
{"Silahkan Pilih Menu di Bawah Ini".center(38)}
{"="*38}
{"[1]. Pemesanan Tempat Parkir"}
{"[2]. Kembali"}
        ''')
    while True:
        opsi = input("Masukkan Pilihan: ")
        if opsi == "1":
            pemesanan()
            break
        elif opsi == "2":
            start()
            break
        else:
            print("Pilihan Invalid, silahkan coba lagi")

#------------------------------------------------ FUNGSI UBAH HARGA ADMIN -------------------------------------------------
def ubah_harga():

    os.system('cls')
    nama_file = 'daftar_harga.csv'

    while True:
        clear()
        with open(nama_file, 'r') as file:
            df = pd.read_csv(file)
            df = df.reset_index()
            df.index+=1
        
        print(f'''
+{"="*46}+
|{"UBAH HARGA".center(46)}|
+{"="*46}+

    {df}

+{"="*46}+
|{"[1]. UBAH HARGA MOTOR".ljust(46)}|
|{"[2]. UBAH HARGA MOBIL".ljust(46)}|
|{"[3]. Kembali".ljust(46)}|
+{"="*46}+      
''')
        
        try:
            ubah = int(input("MASUKKAN PILIHAN: "))
            if ubah == 1:
                ubah_motor = int(input("MASUKKAN HARGA BARU:Rp "))
                    
                # ngubah motor cuy anjay
                df.loc[df['Jenis Kendaraan'] == 'Motor', 'Tarif per jam (Rp)'] = ubah_motor
                        
                with open(nama_file, 'w', newline='') as file1:
                    df.to_csv(file1, index=False)
                    print(f'''{"-"*48}
{"Harga Motor berhasil diubah!"}''')
                    input("TEKAN \"ENTER\" UNTUK KEMBALI")
                    # menu_admin()
                    continue

            elif ubah == 2:
                ubah_mobil = int(input("MASUKKAN HARGA BARU:Rp "))
                    
                # ngubah mobil cuy anjay
                df.loc[df['Jenis Kendaraan'] == 'Mobil', 'Tarif per jam (Rp)'] = ubah_mobil
                    
                with open(nama_file, 'w', newline='') as file1:
                    df.to_csv(file1, index=False)
                    print(f'''{"-"*48}
{"Harga Motor berhasil diubah!"}''')
                    input("TEKAN \"ENTER\" UNTUK KEMBALI")
                    # menu_admin()
                    continue

            elif ubah == 3:
                menu_admin()
                break

            else:
                print("Pilihan tidak valid. Silakan klik \"ENTER\" untuk pilih lagi.")

        except ValueError:
                print("HARAP HANYA MEMASUKKAN ANGKA")

#------------------------------------------------ FUNGSI KELOLA PEMESANAN ADMIN -------------------------------------------------
def kelola_pemesanan():
    while True:
        nama_file = 'real_data.csv'
        with open(nama_file, 'r') as file:
            df = pd.read_csv(file)
            df = pd.DataFrame(df)

        os.system('cls')
        print(f'''
{"="*50}
|{"KELOLA DATA PEMESANAN".center(48)}|
{"="*50}
|{"[1]. Tampilkan Data".ljust(48)}|
|{"[2]. Hapus Data".ljust(48)}|
|{"[3]. Tambah Data".ljust(48)}|
|{"[4]. Edit Data".ljust(48)}|
|{"[5]. Kembali".ljust(48)}|     
{"="*50}''')

        pilihan = int(input("MASUKKAN PILIHAN: "))
        if pilihan == 1:
            os.system('cls')
            with open(nama_file, 'r') as file:
                df = pd.read_csv(file)
                df = df.reset_index(drop=True)
                df.index += 1
                
            print(tabulate(df, headers='keys', tablefmt='fancy_grid'))
            lanjut = input("TEKAN ENTER UNTUK KEMBALI")
        
        elif pilihan == 2:
            try:
                os.system('cls')
                with open(nama_file, 'r') as file:
                    df = pd.read_csv(file)
                    df = df.reset_index(drop=True)
                    df.index += 1
                print(df)
                print(f'''
{"="*50}
|{"HAPUS DATA".center(48)}|
{"="*50}''')
                indeks = int(input("Masukkan indeks baris yang ingin dihapus: "))
                df = df.drop(indeks)
                df.to_csv(nama_file, index=False)
                print("Data berhasil dihapus!")
            except ValueError:
                print("Indeks tidak valid!")
                return
            
        elif pilihan == 3:
            while True:
                os.system('cls')
                print(f'''
{"="*50}
|{"TAMBAH DATA".center(48)}|
{"="*50}''')
                plat_baru = input("\tPLAT NOMOR: ").upper()
                if len(plat_baru) > 9 or len(plat_baru) < 3:
                    print("HARAP MEMASUKKAN PLAT YANG BENAR")
                    continue
                
                konfirmasi_plat = input("\tAPAKAH ANDA YAKIN PLAT NYA BENAR Y/N: ").upper()
                if konfirmasi_plat != 'Y':
                    continue
                
                while True:
                    nama_baru = input("\tNAMA: ").upper()
                    ulang_nama = input("\tAPAKAH NAMA SUDAH BENAR Y/N: ").upper()
                    if ulang_nama == 'Y':
                        break
                    elif ulang_nama != 'N':
                        print("HARAP MEMASUKKAN Y/N SAJA")
                
                while True:
                    jenis_kendaraan = input("\tMasukkan kendaraan MOBIL/MOTOR: ").upper()
                    if jenis_kendaraan not in ['MOBIL', 'MOTOR']:
                        print("HARAP HANYA MEMASUKKAN MOBIL/MOTOR SAJA")
                        continue
                    
                    lanjut_kendaraan = input("\tAPAKAH JENIS KENDARAAN SUDAH BENAR Y/N: ").upper()
                    if lanjut_kendaraan == 'Y':
                        break
                    elif lanjut_kendaraan != 'N':
                        print("HARAP MEMASUKKAN Y/N SAJA")
                
                while True:
                    lokasi_baru = input("\tMasukkan LOKET A/B/C: ").upper()
                    if (lokasi_baru == 'C' and jenis_kendaraan == 'MOBIL'):
                        print("LOKET C HANYA UNTUK MOTOR")
                        continue
                    elif (lokasi_baru in ["A", "B"] and jenis_kendaraan == 'MOTOR'):
                        print("LOKET C HANYA UNTUK MOTOR")
                        continue
                    elif lokasi_baru not in ["A", "B", "C"]:
                        print("HARAP PILIH LOKASI YANG SUDAH DITENTUKAN")
                        continue
                    
                    ulang_lokasi = input("\tAPAKAH ANDA SUDAH BENAR Y/N: ").upper()
                    if ulang_lokasi == "Y":
                        break
                    elif ulang_lokasi != "N":
                        print("HARAP HANYA MEMASUKKAN Y/N SAJA")
                
                data_user_baru = {
                    "NAMA": [nama_baru],
                    "PLAT": [plat_baru],
                    "JENIS KENDARAAN": [jenis_kendaraan],
                    "LOKASI PARKIR": [lokasi_baru]
                }

                dataf = pd.DataFrame(data_user_baru)
                with open(nama_file, 'r') as file2:
                    datat = pd.read_csv(file2)
                data_baru = pd.concat([dataf, datat], ignore_index=True)
                with open(nama_file, 'w', newline='') as file:
                    data_baru.to_csv(file, index=False)
                break

        elif pilihan == 4: 
            try:
                os.system('cls')
                with open(nama_file, 'r') as file:
                    df = pd.read_csv(file)
                    df = df.reset_index(drop=True)
                    df.index += 1
                
                print(tabulate(df, headers='keys', tablefmt='fancy_grid'))
                print(f'''
{"="*50}
|{"+ EDIT DATA +".center(48)}|
{"="*50}''')
                
                indeks = int(input("MASUKKAN INDEKS BARIS: "))
                if indeks not in df.index:
                    print("INDEKS TIDAK VALID!")
                    input("TEKAN \"ENTER\" UNTUK KEMBALI")
                    continue

                clear()
                print(f'''
+{"="*48}+
|{"+ PILIH KOLOM YANG INGIN DI EDIT +".center(48)}|
+{"="*48}+
|{"[1]. NAMA".ljust(48)}|
|{"[2]. PLAT".ljust(48)}|
|{"[3]. JENIS KENDARAAN".ljust(48)}|
|{"[4]. LOKASI PARKIR".ljust(48)}|
+{"="*48}+''')
                
                kolom_pilih = int(input("MASUKKAN PILIHAN: "))
                
                if kolom_pilih == 1:
                    while True:
                        print("\n"+"="*50)
                        nama_baru = input("NAMA BARU: ").upper()
                        print("="*50)
                        konfirmasi = input("APAKAH NAMA SUDAH BENAR Y/N: ").upper()
                        print("="*50)
                        if konfirmasi == 'Y':
                            df.loc[indeks, 'NAMA'] = nama_baru
                            break
                        elif konfirmasi != 'N':
                            print("HARAP MEMASUKKAN Y/N SAJA")
                
                elif kolom_pilih == 2:
                    while True:
                        print("\n"+"="*50)
                        plat_baru = input("PLAT NOMOR BARU: ").upper()
                        if len(plat_baru) > 9 or len(plat_baru) < 3:
                            print("HARAP MEMASUKKAN PLAT YANG BENAR")
                            continue

                        print("="*50)
                        konfirmasi = input("APAKAH PLAT SUDAH BENAR Y/N: ").upper()
                        print("="*50)
                        if konfirmasi == 'Y':
                            df.loc[indeks, 'PLAT'] = plat_baru
                            break
                        elif konfirmasi != 'N':
                            print("HARAP MEMASUKKAN Y/N SAJA")
                
                elif kolom_pilih == 3:
                    while True:
                        print("\n"+"="*50)
                        jenis_baru = input("JENIS KENDARAAN BARU (MOBIL/MOTOR): ").upper()
                        if jenis_baru not in ['MOBIL', 'MOTOR']:
                            print("HARAP HANYA MEMASUKKAN MOBIL/MOTOR SAJA")
                            continue
                        
                        lokasi_sekarang = df.loc[indeks, 'LOKASI PARKIR']
                        if (jenis_baru == 'MOBIL' and lokasi_sekarang == 'C') or \
                            (jenis_baru == 'MOTOR' and lokasi_sekarang in ['A', 'B']):
                            print("PERUBAHAN JENIS KENDARAAN TIDAK SESUAI DENGAN LOKASI PARKIR")
                            continue

                        print("="*50)
                        konfirmasi = input("APAKAH JENIS KENDARAAN SUDAH BENAR Y/N: ").upper()
                        print("="*50)
                        if konfirmasi == 'Y':
                            df.loc[indeks, 'JENIS KENDARAAN'] = jenis_baru
                            break
                        elif konfirmasi != 'N':
                            print("HARAP MEMASUKKAN Y/N SAJA")
                
                elif kolom_pilih == 4:
                    jenis_kendaraan = df.loc[indeks, 'JENIS KENDARAAN']
                    while True:
                        print("\n"+"="*50)
                        lokasi_baru = input("LOKASI PARKIR BARU (A/B/C): ").upper()
                        if (lokasi_baru == 'C' and jenis_kendaraan == 'MOBIL'):
                            print("LOKET C HANYA UNTUK MOTOR")
                            continue
                        elif (lokasi_baru in ["A", "B"] and jenis_kendaraan == 'MOTOR'):
                            print("LOKET C HANYA UNTUK MOTOR")
                            continue
                        elif lokasi_baru not in ["A", "B", "C"]:
                            print("HARAP PILIH LOKASI YANG SUDAH DITENTUKAN")
                            continue
                        
                        print("="*50)
                        konfirmasi = input("APAKAH LOKASI SUDAH BENAR Y/N: ").upper()
                        print("="*50)
                        if konfirmasi == 'Y':
                            df.loc[indeks, 'LOKASI PARKIR'] = lokasi_baru
                            break
                        elif konfirmasi != 'N':
                            print("HARAP MEMASUKKAN Y/N SAJA")
                
                else:
                    print("PILIHAN TIDAK VALID!")
                    input("TEKAN \"ENTER\" UNTUK KEMBALI")
                    continue

                df.to_csv(nama_file, index=False)
                print("DATA BERHASIL DIUBAH!")
                input("TEKAN \"ENTER\" UNTUK KEMBALI")

            except ValueError:
                print("TERJADI KESALAHAN SAAT MENGEDIT DATA!")
                input("TEKAN \"ENTER\" UNTUK KEMBALI")

        elif pilihan == 5:
            menu_admin()
            break
        else:
            print("HARAP MASUKKAN ANGKA YANG SESUAI")

#------------------------------------------------ FUNGSI LIAT KENDARAAN -------------------------------------------------
def lihat_kendaraan_in():
    nama_file = 'check_in.csv'
    with open(nama_file, 'r') as file:
        df = pd.read_csv(file)
        df = pd.DataFrame(df)
        df = df.reset_index(drop=True)
        df.index+=1

    print(tabulate(df, headers='keys', tablefmt='fancy_grid'))
    kembali= input("TEKAN ENTER UNTUK KEMBALI")
    menu_admin()

#------------------------------------------------ FUNGSI HISTORY  -------------------------------------------------
def history():
    nama_file = 'check_out.csv'
    with open(nama_file, 'r') as file:
        df = pd.read_csv(file)
        df = df.reset_index(drop=True)
        df.index+=1
    
    print(tabulate(df, headers='keys', tablefmt='fancy_grid'))

    da = pd.read_csv(nama_file)
    da['BIAYA_NUMERIK'] = da['BIAYA'].str.replace('Rp ', '').str.replace(',', '').astype(int)
    total_pendapatan = da['BIAYA_NUMERIK'].sum()
    print (f'total pendapatan : Rp{total_pendapatan:,}')
    kembali = input("TEKAN ENTER UNTUK KEMBALI")
    menu_admin()

#------------------------------------------------ MAIN FUNGSI -------------------------------------------------
def start():
    clear()
    main_menu()
    
    opsi = input("Masukkan Pilihan: ")
    if opsi == "1":
        login_admin()
    elif opsi == "2":
        cek_harga()
    elif opsi == "3":
        cek_tempat_parkir()
    elif opsi == "4":
        pemesanan()
    elif opsi == "5":
        check_in()
    elif opsi == "6":
        check_out()
    elif opsi == "7":
        awalan()
    else:
        input("Pilihan Invalid, klik \"ENTER\" untuk memilih kembali!")
        start()

start()