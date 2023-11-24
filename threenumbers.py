n1 = int(input("Masukkan Nomor Pertama: "))
n2 = int(input("Masukkan Nomor Kedua: "))
n3 = int(input("Masukkan Nomor Ketiga: "))

if n1 >= n2 and n1 >= n3:
    Terbesar= num1
elif n2 >= n1 and n2 >= n3:
    Terbesar = n2
else:
    Terbesar = n3

print("Nomor Terbesar Adalah:", Terbesar)