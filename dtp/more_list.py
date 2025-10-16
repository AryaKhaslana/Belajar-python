# more list buah

buah = ["jeruk", "mangga", "apel", "durian"]
print(buah)

for i in (buah):
 print (i)

buah.remove("jeruk")
print(buah)

buah.append("susu")
print(buah)

# more list angka

angka=[1,2,3,4,6]

# def kuadrat(n):
#    return n*n

#      for x in angka:
#        kuadrat(x)

# hasil_kuadrat = map(kuadrat, angka)

hasil_kuadrat = map(lambda x: x**2, angka)
print(hasil_kuadrat)
print(list(hasil_kuadrat))

def ganjil(x):
    return x % 2 != 0

def genap(x):
    return x % 2 == 0 

bilangan_genap = filter(genap, angka)
print(list(bilangan_genap))

bilangan_ganjil = filter(ganjil, angka)
print(list(bilangan_ganjil))