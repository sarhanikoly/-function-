def hitung_keliling_dan_luas(panjang, lebar):
    keliling = 2 * (panjang + lebar)
    luas = panjang * lebar
    return f"luas {luas}, keliling {keliling}"


panjang = 50
lebar = 3
hasil = hitung_keliling_dan_luas(panjang, lebar)
print(hasil)  
