nama  = input("Masukkan Nama Lengkap Anda : ")
prodi = input("Masukkan Prodi Anda : ")
inputuser = input("Masukkan nilai (dalam huruf) tang anda dapat : ")

try:
    nilai = int(inputuser)
    if nilai >= 0:
        print("E")
    elif nilai >= 1.0:
        print("D")
    elif nilai >=2.0:
        print("C")
    elif nilai >= 2.25:
        print("C+")
    elif nilai >= 2.75:
        print("B-")
    elif nilai >= 3.0:
        print("B")
    elif nilai >= 3.25:
        print("B+")
    elif nilai >= 3.75:
        print("A-")
    elif nilai >= 4.0:
        print("A")

except:
    print("Inputan nilai yang anda masukkan tidak valid")
