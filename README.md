# course-planning-scheduling
## Deskripsi Singkat Program
Aplikasi sederhana yang dapat menyusun
rencana pengambilan kuliah, dengan memanfaatkan algoritma Decrease and Conquer. Penyusunan
Rencana Kuliah diimplementasikan dengan menggunakan pendekatan Topological Sorting.
## Requirements dan Instalasi
### Instalasi
- Python >= versi 3.8
- Install pyinstaller
```
pip3 install pyinstaller
```
atau
```
pip install pyinstaller
```
### Requirements input file
```
<kode_kuliah_1>, <kode kuliah prasyarat - 1>, <kode kuliah prasyarat - 2>, <kode kuliah prasyarat - 3>.
<kode_kuliah_2>, <kode kuliah prasyarat - 1>, <kode kuliah prasyarat - 2>.
<kode_kuliah_3>, <kode kuliah prasyarat - 1>, <kode kuliah prasyarat - 2>, <kode kuliah prasyarat - 3>, <kode kuliah prasyarat - 4>.
<kode_kuliah_4>.
```
## Cara Menggunakan Program
### Menjalankan melalui executable file
- Pastikan sudah berada di direktori bin, kemudian ketikkan perintah berikut di terminal.
```
chmod +x main
```
- Apabila berhasil, jalankan program dengan perintah berikut.
```
./main
```
- Kemudian masukkan input file yang berisi nama mata kuliah beserta prerequisite-nya.
### Menjalankan melalui main,py
- Pastikan sudah berada di direktori src, kemudian ketikkan perintah berikut di terminal.
```
python3 main.py
```
atau
```
python main.py
```
- Kemudian masukkan input file yang berisi nama mata kuliah beserta prerequisite-nya.
### Contoh input dan output
- Input file
```
Matematika IA.
Fisika Dasar IA.
Olah Raga.
Pengenalan Komputasi.
Tata Tulis Karya Ilmiah.
Bahasa Inggris.
Matematika IIA, Matematika IA.
Fisika Dasar IIA, Fisika Dasar IA.
Dasar Pemograman, Pengenalan Komputasi.
Pengantar Rekayasa dan Desain, Tata Tulis Karya Ilmiah.
Kimia Dasar B, Matematika IA, Fisika Dasar IA.
Pengantar Analisis Rangkaian, Fisika Dasar IA.
Logika Komputasional, Matematika IIA, Dasar Pemograman.
Algoritma dan Struktur Data, Dasar Pemograman.
Matematika Diskrit, Matematika IIA.
Teori Bahasa Formal dan Otomata, Dasar Pemograman.
Aljabar Linier dan Geometri, Matematika IIA.
Organisasi dan Arsitektur Komputer, Dasar Pemograman.
Pemograman Berorientasi Objek, Algoritma dan Struktur Data.
Strategi Algoritma, Algoritma dan Struktur Data.
Probabilitas dan Statistika, Matematika Diskrit.
Sistem Operasi, Organisasi dan Arsitektur Komputer.
Basis Data, Matematika Diskrit, Logika Komputasional.
Rekayasa Perangkat Lunak, Teori Bahasa Formal dan Otomata.
```
- Output
```
You can follow this planning to grab your cumlaude
--------------------------------------------------
Semester 1 : Matematika IA, Fisika Dasar IA, Olah Raga, Pengenalan Komputasi, Tata Tulis Karya Ilmiah, Bahasa Inggris.

Semester 2 : Matematika IIA, Fisika Dasar IIA, Dasar Pemograman, Pengantar Rekayasa dan Desain, Kimia Dasar B, Pengantar Analisis Rangkaian.

Semester 3 : Logika Komputasional, Algoritma dan Struktur Data, Matematika Diskrit, Teori Bahasa Formal dan Otomata, Aljabar Linier dan Geometri, Organisasi dan Arsitektur Komputer.

Semester 4 : Pemograman Berorientasi Objek, Strategi Algoritma, Probabilitas dan Statistika, Sistem Operasi, Basis Data, Rekayasa Perangkat Lunak.
```
## Author
[Mgs. Tabrani (13519122)](https://github.com/mgstabrani)
