# Pertemuan 05 Perulangan Python

Nama: Wulan Nur'aini
NIM: 2225250131
Kelas: 3E

## Tujuan
Menggunakan `for` dan `while` untuk menyelesaikan masalah iteratif, menguji kondisi berhenti, melakukan tracing variabel, serta mengelola dokumentasi dan pengujian program.

## Cara Menjalankan

### Menjalankan Latihan
'''bash
python latihan/01_tabel_perkalian.py
python latihan/02_jumlah_bilangan.py
python latihan/03_validasi_input.py
python latihan/04_hitung_genap.py

### Menjalankan Kuis
'''bash
python kuis/kuis2_deret_aritmetika.py

## Algoritma Kuis 2
1. Membaca input nilai suku pertama ($a$) dan beda ($d$) dalam bentuk bilangan desimal (float).
2. Membaca input banyak suku ($n$) dalam bentuk bilangan bulat (int).
3. Melakukan validasi input nilai $n$ menggunakan perulangan while: jika $n \le 0$, program menampilkan pesan peringatan dan meminta pengguna memasukkan nilai $n$ kembali hingga diperoleh nilai $n > 0$.
4. Menginisialisasi variabel akumulator total = 0.0 untuk menyimpan jumlah keseluruhan deret.
5. Melakukan perulangan for sebanyak $n$ kali (menggunakan range(n) dengan indeks $i$ dari 0 sampai n - 1):
   Menghitung nilai suku ke-$(i + 1)$ dengan rumus: suku = a + i * d.
   Menambahkan nilai suku ke dalam variabel akumulator total.
   Menampilkan nomor suku beserta nilainya dengan format dua angka di belakang koma (:.2f).
6. Setelah perulangan selesai, menampilkan hasil akhir akumulasi jumlah deret dengan format dua angka di belakang koma (:.2f).

## Hasil Pengujian
### 1. File: `01_tabel_perkalian.py`

| Test Case | Input | Keluaran yang Diharapkan | Keluaran Aktual | Status |
| :---: | :--- | :--- | :--- | :---: |
| 1 | `Bilangan: 4` | Menampilkan tabel perkalian 4 x 1 s.d. 4 x 10 | Menampilkan 4 x 1 = 4 hingga 4 x 10 = 40 | **LULUS** |
| 2 | `Bilangan: -3` | Menampilkan tabel perkalian -3 x 1 s.d. -3 x 10 | Menampilkan -3 x 1 = -3 hingga -3 x 10 = -30 | **LULUS** |

---

### 2. File: `02_jumlah_bilangan.py`

| Test Case | Input | Keluaran yang Diharapkan | Keluaran Aktual | Status |
| :---: | :--- | :--- | :--- | :---: |
| 1 | `n: 1` | `Jumlah = 1` | `Jumlah = 1` | **LULUS** |
| 2 | `n: 5` | `Jumlah = 15` | `Jumlah = 15` | **LULUS** |
| 3 | `n: 10` | `Jumlah = 55` | `Jumlah = 55` | **LULUS** |

---

### 3. File: `03_validasi_input.py`

| Test Case | Input | Keluaran yang Diharapkan | Keluaran Aktual | Status |
| :---: | :--- | :--- | :--- | :---: |
| 1 | `120`, `-5`, `75` | Menolak 120 dan -5 (di luar 0-100), lalu menerima 75 | `Nilai tidak valid.`<br>`Nilai tidak valid.`<br>`Nilai diterima: 75.0` | **LULUS** |

---

### 4. File: `04_hitung_genap.py`

| Test Case | Input | Keluaran yang Diharapkan | Keluaran Aktual | Status |
| :---: | :--- | :--- | :--- | :---: |
| 1 | `n: 1` | `Banyak bilangan genap = 0` | `Banyak bilangan genap = 0` | **LULUS** |
| 2 | `n: 2` | `Banyak bilangan genap = 1` | `Banyak bilangan genap = 1` | **LULUS** |
| 3 | `n: 5` | `Banyak bilangan genap = 2` | `Banyak bilangan genap = 2` | **LULUS** |
| 4 | `n: 10` | `Banyak bilangan genap = 5` | `Banyak bilangan genap = 5` | **LULUS** |


### 5. File: `kuis2_deret_aritmetika.py`

| Test Case | Input ($a, d, n$) | Suku yang Diharapkan | Jumlah Diharapkan | Keluaran Aktual | Status |
| :---: | :--- | :--- | :---: | :--- | :---: |
| 1 | $a = 2$, $d = 3$, $n = 5$ | 2, 5, 8, 11, 14 | 40.00 | Suku ke-1 s.d. 5: 2.00, 5.00, 8.00, 11.00, 14.00<br>**Jumlah deret:** 40.00 | **LULUS** |
| 2 | $a = 10$, $d = -2$, $n = 4$ | 10, 8, 6, 4 | 28.00 | Suku ke-1 s.d. 4: 10.00, 8.00, 6.00, 4.00<br>**Jumlah deret:** 28.00 | **LULUS** |
| 3 | $a = 1.5$, $d = 0.5$, $n = 3$ | 1.5, 2.0, 2.5 | 6.00 | Suku ke-1 s.d. 3: 1.50, 2.00, 2.50<br>**Jumlah deret:** 6.00 | **LULUS** |

## Refleksi
Dalam proses pengerjaan latihan, kesalahan perulangan yang ditemukan terjadi pada berkas 04_hitung_genap.py, yaitu kesalahan indentasi (IndentationError).
Penyebab:
Blok kode di dalam struktur seleksi if (seperti jumlah_genap += 1) tidak diindentasi dengan benar (kurang spasi/tab di bawah pernyataan if), sehingga Python tidak dapat mengenali baris tersebut sebagai badan perintah dari kondisi if.
Cara Memperbaiki:
Memastikan seluruh baris perintah yang berada di dalam blok for maupun if memiliki indentasi yang konsisten, yaitu menggunakan 4 spasi untuk setiap tingkatan blok program.

