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
## Author
[Mgs. Tabrani (13519122)](https://github.com/mgstabrani)
