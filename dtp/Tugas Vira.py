print("-----Selamat datang, bisa saya bantu?------")

gejala = input("Apakah pasien mengalami konstipasi berat (Ya/tidak)")
usia = input("Apakah pasien lansia (Ya/tidak)")

obat = ""

if gejala == "Ya" and usia == "Ya":
    print("Obat yang anda butuhkan adalah Laktulosa ")
elif gejala == "Ya" and usia == "tidak":
    print("Obat yang anda butuhkan adalah Psyllium")
else:
    print("Solusi anda jika tidak terkena apa apa adalah Perbanyak makanan yang berserat dan jangan lupa minum air putih ")


print("Terimakasih telah mengecek kesehatan anda")