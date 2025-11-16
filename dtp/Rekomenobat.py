print("Selamat datang di pengecekan")

gejala = input("Apakah pasien mengalami konstipasi berat ? (ya/tidak) ")

if gejala == "ya":

    print("Gejala sudah terkonfirmasi, sekarang masukan usia !")
    usia = input("Apakah pasien lansia ? (ya/tidak) ")

    nama_obat = ""
    efek_samping = ""
    saran_dosis = ""

    if usia == "ya":
        nama_obat = "laktulosa"
        efek_samping = "Efek samping obat laktulosa yang paling umum terjadi adalah gangguan pencernaan ringan"
        saran_dosis = "Saran dosis laktulosa bervariasi tergantung pada kondisi yang diobati (sembelit atau ensefalopati hepatik) dan usia pasien"

    elif usia == "tidak":
        nama_obat = "Psyllium"
        efek_samping = "Efek samping umum dari psyllium umumnya ringan dan berhubungan dengan pencernaan. Namun, reaksi yang lebih serius dapat terjadi, terutama jika tidak dikonsumsi dengan benar. "
        saran_dosis = "Dosis psyllium bervariasi tergantung usia, kondisi, dan bentuk obatnya. Sangat penting untuk selalu membaca dan mengikuti petunjuk pada kemasan produk atau anjuran dokter"

    else:
        print("Tolong masukkan ya atau tidak")
        exit()

    print("-------- obat dan informasi tambahan ------")
    print(f"Obat yang disarankan : {nama_obat}")
    print(f"Efek samping dari obat : {efek_samping}")
    print(f"saran dosis obat : {saran_dosis}")
    print("semoga cepat sembuh")

elif gejala == "tidak":
    print("tetap perbanyak makan makanan yang berserat dan jangan lupa minum air putih")

print("Terima kasih sudah mengecek disini, semoga cepat sembuh ya !!")