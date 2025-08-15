# YT_Dowloader_CLI_ONLY

# 🚀 YouTube Downloader CLI (Command Line Interface)

Sebuah skrip Python sederhana namun kuat untuk mengunduh video dan audio dari YouTube langsung dari terminal Anda. Dibuat dengan `yt-dlp` dan didesain untuk kemudahan penggunaan, terutama untuk pengguna Termux di Android.

---

## 🔗 Tujuan Projek Ini

* **Unduh Fleksibel**: Memungkinkan pengguna memilih berbagai format video (MP4) dan audio (MP3) yang tersedia dari URL YouTube.
* **Integrasi Termux**: Dibuat agar dapat berjalan dengan lancar di Termux, dengan lokasi unduhan *default* di `/sdcard/Download/`.
* **Logging Transaksi**: Mencatat setiap unduhan yang berhasil ke dalam sebuah file log (`download.log`) untuk melacak riwayat unduhan.
* **Tampilan Interaktif**: Menyajikan daftar format yang tersedia dengan informasi lengkap (resolusi, ukuran file) dan *progress bar* saat mengunduh.

---

## 📦 Isi Kotak Proyek Ini

* **Konfigurasi Jalur**: Menentukan direktori unduhan (`/sdcard/Download`) dan file log (`download.log`).
* **Pilihan Format**: Fungsi untuk mengekstrak dan menampilkan semua format video dan audio yang tersedia dari URL.
* **Log Unduhan**: Fungsi untuk mencatat detail setiap unduhan yang berhasil ke dalam file log.
* **Pengunduh Berbasis `yt-dlp`**: Menggunakan `yt-dlp` untuk mengelola proses pengunduhan, konversi format (MP3), dan menampilkan progress.
* **Menu Interaktif**: Loop utama program yang meminta URL, menampilkan menu pilihan, dan memulai proses unduhan.

---

## ✨ Fitur-Fitur Kerennya

* **Pilihan Format Lengkap** 🎥
    Aplikasi akan secara otomatis mendeteksi dan menampilkan semua format video dan audio yang tersedia dari sebuah URL, lengkap dengan resolusi dan perkiraan ukuran file.

* **Pengunduhan MP3 Otomatis** 🎧
    Cukup pilih format audio, dan skrip akan menggunakan `ffmpeg` (yang dibutuhkan oleh `yt-dlp`) untuk mengekstrak audio dan mengonversinya menjadi file MP3.

* **Proses Pengunduhan Transparan** 📊
    Saat mengunduh, Anda akan melihat *progress bar* yang menampilkan persentase, kecepatan unduh, dan perkiraan waktu selesai (*ETA*).

* **Log Riwayat Unduhan** 📝
    Setiap unduhan yang berhasil akan dicatat dalam file `download.log` dengan informasi detail seperti tanggal, judul, format, dan nama file.

* **Fleksibilitas Penggunaan** 💻
    Bekerja dengan baik di lingkungan desktop maupun di terminal perangkat Android (Termux).

---

## 🛠️ Apa Yang Kamu Butuhkan

### Persyaratan Software

* **Python 3.x**
* **`yt-dlp`**: Perpustakaan utama untuk mengunduh video.
* **`ffmpeg`**: Diperlukan untuk konversi video ke audio (MP3).

Anda bisa menginstal semua perpustakaan yang dibutuhkan dengan pip:
```bash
pip install yt-dlp
