#tugas no1
kendaraan =["vario","motor",150,"pink","2"]
tambahan =(5000,"matic")
kendaraan.extend(tambahan)
kendaraan.insert(2,"honda")
print (kendaraan)

#tugas no 2
print("===alat hitung luas===")
print("pilih 1 untuk menghitung luas pesergi")
print("pilih 1 untuk menghitung luas lingkaran")
print("pilih 1 untuk menghitung luas segitiga")

pilihan =int(input("masukan pilihan (1/2/3)"))

match pilihan:
    case 1:
        s = int(input("masukkan panjang sisi persegi"))
        luas = s * s
        print (f"luas pesergi adalah: {luas}")
        
    case 2:
        r = int(input("masukkan jari jari lingkaran"))
        pi = 3,14
        luas = pi * r**2
        print (f*"luas lingkaran adalah: {luas}")
    
    case 3:
        a = int(input("masukkan alas segitiga"))
        t = int(input("masukkan tinggi segitiga"))
        luas = a * t /2
        print ("luas segitiga adalah: {luas}")
        
    case _:
        print("masukkan pilihan dengan benar")
