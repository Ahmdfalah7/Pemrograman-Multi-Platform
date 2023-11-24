length = int(input("Berapa Panjangnya: "))

x = 0
y = 1
iteration = 0

if length <=0:
    print("Masukkan Angka Lebih dari 0")
elif length == 1:
    print("Deretan Fibonacci ini Memiliki {} Element" .format(length),":")
    print(x)
else:
    print("Deretan Fibonacci ini Memiliki {} Element".format(length), ":")
while (iteration < length):
    print(x, end=',')
    z = x + y

    x = y
    y = z
    iteration += 1
    
    
