nilai = int(input("Masukkan Angka:"))

print ("Angka ganjil sampai", nilai,"adalah:")
for i in range (1,nilai,2):
    if (i %2 != 0) :
        print(i, end=" ")
    print()