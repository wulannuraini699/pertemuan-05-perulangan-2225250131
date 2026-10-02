
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
