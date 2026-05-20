import numpy as np

# soal1
posisi_awal = np.array([10, 10])
posisi_jalan = np.array([5, 2])
posisi_akhir = posisi_awal + posisi_jalan
print(f"Posisi akhir: {posisi_akhir}")

# soal2
ukuran = np.array([2, 4, 6, 8])
bonus_tambahan = [1, 1, 1, 1]
ukuran_baru = ukuran + bonus_tambahan
hasil = ukuran_baru * 3
print(f"Ukuran: {hasil}")

# soal3
posisi_awal_bola = np.array([0, 50])
kecepatan = np.array([0, 0])
gravitasi = np.array([0, -2])
for i in range(3):
    kecepatan = kecepatan + gravitasi
    posisi_awal_bola = posisi_awal_bola + kecepatan
    print(f"Posisi bola: {posisi_awal_bola}")
