def hitung_jumlah_kata(kalimat):
    kata = kalimat.split()
    return len(kata)


kalimat = "Ini adalah contoh kalimat baik"
hasil = hitung_jumlah_kata(kalimat)
print(hasil)  
