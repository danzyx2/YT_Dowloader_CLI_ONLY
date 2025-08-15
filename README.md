# 🚀 YouTube Downloader CLI 📹

Sebuah skrip Python sederhana namun tangguh untuk mengunduh video dan audio dari YouTube langsung dari terminal Anda. Didesain khusus untuk kemudahan penggunaan di perangkat Android melalui aplikasi **Termux**.

---

## 💡 Fitur Unggulan

* **Pilihan Format Fleksibel** 🎛️
    Secara otomatis menampilkan semua format video (MP4) dan audio (MP3) yang tersedia, lengkap dengan informasi resolusi, kualitas, dan perkiraan ukuran file.

* **Unduhan Audio MP3 Otomatis** 🎧
    Cukup pilih format audio, dan skrip akan secara cerdas mengunduh audio terbaik dan mengonversinya menjadi file `.mp3` di perangkat Anda.

* **Status Pengunduhan *Real-time*** ⏳
    Dapatkan visualisasi kemajuan unduhan dengan *progress bar* interaktif yang menampilkan persentase, kecepatan, dan perkiraan waktu selesai.

* **Riwayat Unduhan Otomatis** 📜
    Setiap unduhan yang berhasil akan dicatat secara rapi dalam file `download.log`, sehingga Anda dapat melacak semua riwayat unduhan Anda.

* **Integrasi Termux Sempurna** 📱
    Dirancang untuk bekerja tanpa hambatan di Termux, dengan lokasi penyimpanan *default* di folder `Download` penyimpanan internal Anda.

---

## 🛠️ Persiapan Awal

Sebelum menjalankan skrip, pastikan Anda telah menginstal beberapa alat penting.

### 1. Instalasi di Termux

```bash
# Perbarui paket Termux
pkg update && pkg upgrade

# Instal Python
pkg install python

# Instal yt-dlp dan ffmpeg
# yt-dlp adalah pengunduh utamanya
# ffmpeg diperlukan untuk mengonversi video ke MP3
pip install yt-dlp
pkg install ffmpeg

# Berikan Termux izin untuk mengakses penyimpanan
termux-setup-storage
```

---

## 🚀 Cara Menggunakan

### Langkah 1: Simpan Kode

Salin kode `ytcli.py` ke folder mana pun di perangkat Anda, misalnya di `~/storage/shared/Download/`.

### Langkah 2: Jalankan dari Terminal

Buka Termux, navigasikan ke folder tempat Anda menyimpan skrip, dan jalankan perintah ini:

```bash
python ytcli.py
```

### Langkah 3: Ikuti Panduan

Program akan memandu Anda. Cukup masukkan **URL YouTube**, lalu pilih format video atau audio yang Anda inginkan dengan mengetikkan angka yang sesuai.

```
--- YouTube Downloader CLI ---
Masukkan URL YouTube: [tempel URL Anda di sini]
...
➡️ Pilihan Video (MP4):
  [0] 299 | 1080p | mp4
  [1] 137 | 1080p | mp4
...
➡️ Pilihan Audio (MP3):
  [10] 251 | Audio Only | mp4
...
Pilih format: [ketik angka, misal: 10]
```

File yang diunduh akan tersimpan otomatis di `~/storage/shared/Download/`.

---

## 📄 Lisensi

Proyek ini dirilis di bawah **Lisensi MIT**. Anda bebas menggunakan, memodifikasi, dan menyebarkannya untuk tujuan apa pun.

---

## 🤝 Kontribusi

Ide, saran, atau laporan *bug* sangat kami hargai! Jika Anda ingin berkontribusi:

1.  Buka **Issues** untuk melaporkan masalah atau mengusulkan fitur baru.
2.  Buat **Pull Request** dengan kode yang sudah Anda perbaiki.

Mari ciptakan alat-alat yang lebih baik bersama-sama!
