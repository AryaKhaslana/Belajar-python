# baris_awal = int(input("masukkan bilangan awal : "))
# baris_akhir = int(input("masukkan bilangan akhir : "))

# for i in range (baris_awal, baris_akhir+1):
#     if i % 2 == 0 :
#         print (i, "ini adalah bilangan genap")
#     else:
#         print (i, "ini adalah bilangan ganjil")

print("kita mencari bilangan prima")

def is_prime (num):

    if num <= 1 :
        return False

    for i in range (2, int(num**0.5) + 1):
        if num % i == 0:

            return False

        return True

number = int(input("Masukkan bilangan anda : "))    

if is_prime(number):
    print(f"{number}Maka ini bilangan prima")
else:
    print(f"{number},kalo ini bukan bilangan prima")