def cek_palindrom(kata):
    if kata == kata[::-1]:
        return f"{kata} adalah palindrom"
    else:
        return f"{kata} bukan palindrom"


kata = "level"
hasil = cek_palindrom(kata)
print(hasil)  