inputuser = input("Masukkan plat nomor: ")
try:
    plat = int(inputuser)
    if plat <= 3000:
        print("Plat nomor tersebut diperlukan untuk mobil")
    elif plat >= 3001 and plat <= 4000:
        print("Plat nomoe tersebut diperlukan untuk motor")
    elif plat >=4001 and plat <= 5000:
        print("Plat nomor tersebut diperlukan untuk angkatan umum")
except:
    print("Plat Nomor Tidak Terinidikasi, harus terdapat nomor kendaraan setelah kode daerah")