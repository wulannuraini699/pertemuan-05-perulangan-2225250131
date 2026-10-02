# Latihan 4: Validasi Tipe dan Ketuntasan Soal
# Input: Jumlah soal benar dari total 20 soal (teks -> int)
# Aturan: Validasi tipe int, rentang 0-20, batas tuntas >= 75%
# Output: Persentase dan status ketuntasan

teks = input("Jumlah soal benar dari 20: ").strip()

try:
    benar = int(teks)
except ValueError:
    print("Masukan ditolak: jumlah harus berupa bilangan bulat.")
else:
    if benar < 0 or benar > 20:
        print("Masukan ditolak: jumlah harus berada pada rentang 0 sampai 20.")
    else:
        persen = (benar / 20) * 100
        print(f"Persentase = {persen:.2f} persen")
        if persen >= 75:
            print("Tuntas")
        else:
            print("Belum tuntas")