print("Deret Aritmetika")

# 1. Baca a dan d sebagai float
a = float(input("Suku pertama a: "))
d = float(input("Beda d: "))

# 2. Baca n sebagai integer
n = int(input("Banyak suku n: "))

# Validasi n dengan while (jika n tidak positif/n <= 0)
while n <= 0:
    print("Banyak suku n harus berupa bilangan positif (> 0).")
    n = int(input("Banyak suku n: "))

# 3. Inisialisasi akumulator total
total = 0.0

# 4. Perulangan for dari 0 sampai n - 1 untuk menghasilkan n suku
for i in range(n):
    # 5. Hitung nilai suku ke-(i+1)
    suku = a + i * d
    
    # 6. Tambahkan suku ke total dan tampilkan nomor suku beserta nilainya
    total += suku
    print(f"Suku ke-{i + 1}: {suku:.2f}")

# 7. Tampilkan jumlah akhir dengan dua angka di belakang koma (.2f)
print(f"Jumlah deret: {total:.2f}")