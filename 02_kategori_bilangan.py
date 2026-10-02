# Latihan 2: Kategori Bilangan
# Input: Bilangan bulat (int)
# Aturan: Membedakan negatif, nol, positif genap, dan positif ganjil
# Output: Kategori bilangan

x = int(input("Masukkan bilangan bulat: "))

if x < 0:
    print("Bilangan negatif")
elif x == 0:
    print("Nol")
elif x % 2 == 0:
    print("Bilangan positif genap")
else:
    print("Bilangan positif ganjil")