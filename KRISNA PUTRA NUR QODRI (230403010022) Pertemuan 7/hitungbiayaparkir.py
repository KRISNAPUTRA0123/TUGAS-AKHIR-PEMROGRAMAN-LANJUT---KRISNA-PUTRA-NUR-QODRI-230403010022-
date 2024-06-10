from paketku import jeniskendaraanmulai, jeniskendaraanakhir, jammulai, jamakhir, namakendaraanmulai, namakendaraanakhir

def namakendaraan():
    namaawal = namakendaraanmulai("Kijang")
    namaakhir = namakendaraanakhir("Kijang")
    if namaawal == namaakhir:
        return(namaakhir)
    else:
        return("Nama Kendaraan tidak sesuai")

hasilnama = namakendaraan()
print("Nama Kendaraan : ", hasilnama)

def jeniskendaraan():
    jenisawal = jeniskendaraanmulai("mobil")
    jenisakhir = jeniskendaraanakhir("mobil")
    if jenisawal == jenisakhir:
        return(jenisakhir)
    else:
        return("Jenis Kendaraan tidak sesuai")
    

hasiljenis = jeniskendaraan()
print("Jenis Kendaraan : ", hasiljenis)

def biayaparkir():
    awalparkir = jammulai(7)
    akhirparkir = jamakhir(13)
    jam = akhirparkir - awalparkir
    if hasiljenis == "mobil":
        biayakendaraan = 5000
    elif hasiljenis == "motor" :
        biayakendaraan = 3000
    else:
        biayakendaraan = 8000

    biaya = 1000 * (jam - 1) + biayakendaraan
    return biaya

biaya = biayaparkir()
print("Biaya Parkir: ", biaya)