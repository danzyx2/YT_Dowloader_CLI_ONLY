import os
import yt_dlp
from datetime import datetime

# Konfigurasi
DOWNLOAD_DIR = "/sdcard/Download"
LOG_FILE = "download.log"

# Pastikan folder download ada
if not os.path.exists(DOWNLOAD_DIR):
    os.makedirs(DOWNLOAD_DIR)

def log_download(title, format_type, filename):
    """Mencatat riwayat unduhan ke dalam file log."""
    with open(LOG_FILE, 'a') as log:
        log.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | {title} | {format_type} | {filename}\n")

def my_hook(d):
    """Fungsi hook untuk menampilkan progress bar saat mengunduh."""
    if d['status'] == 'downloading':
        percent_str = d.get('_percent_str', 'N/A')
        speed_str = d.get('_speed_str', 'N/A')
        eta_str = d.get('_eta_str', 'N/A')
        print(f"⏳ {percent_str} | Kecepatan: {speed_str} | ETA: {eta_str}", end='\r')
    elif d['status'] == 'finished':
        print("\n✅ Pengunduhan selesai!")

def get_formats(url):
    """Mengambil dan menampilkan daftar format video/audio dari URL."""
    print("Mengekstrak informasi video...")
    ydl_opts = {
        'quiet': True,
        'forcejson': True,
        'simulate': True,
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            print("\n" + "="*50)
            print(f"Judul: {info.get('title')}")
            print(f"Durasi: {info.get('duration_string')}")
            print("="*50 + "\n")
            
            # Pisahkan format video dan audio
            video_formats = [f for f in info['formats'] if f.get('vcodec') != 'none']
            audio_formats = [f for f in info['formats'] if f.get('acodec') != 'none' and f.get('ext') == 'm4a'] 
            
            print("➡️ Pilihan Video (MP4):")
            for i, f in enumerate(video_formats):
                size = f.get('filesize') or f.get('filesize_approx')
                size_str = f"{size / 1024**2:.2f} MB" if size else "Tidak diketahui"
                print(f"  [{i}] {f.get('format_id')} | {f.get('resolution')} | {f.get('ext')} | {size_str}")
            
            print("\n➡️ Pilihan Audio (MP3):")
            for i, f in enumerate(audio_formats):
                size = f.get('filesize') or f.get('filesize_approx')
                size_str = f"{size / 1024**2:.2f} MB" if size else "Tidak diketahui"
                print(f"  [{i+len(video_formats)}] {f.get('format_id')} | Audio Only | {f.get('ext')} | {size_str}")

            return info, video_formats, audio_formats
    except Exception as e:
        print(f"❌ Gagal mengambil data: {e}")
        return None, None, None

def download_file(url, format_id, is_mp3, title):
    """Mengunduh video/audio berdasarkan format yang dipilih."""
    filename = "".join(x for x in title if x.isalnum() or x in " -_")
    
    if is_mp3:
        output_path = os.path.join(DOWNLOAD_DIR, f"{filename}.mp3")
    else:
        output_path = os.path.join(DOWNLOAD_DIR, f"{filename}.mp4")

    ydl_opts = {
        'outtmpl': output_path,
        'progress_hooks': [my_hook],
    }

    if is_mp3:
        ydl_opts.update({
            # Gunakan format bestaudio untuk konversi ke MP3
            'format': 'bestaudio', 
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }]
        })
    else:
        # Menggabungkan video dan audio stream secara otomatis
        # Kita perlu menggabungkan format video yang dipilih dengan audio terbaik
        ydl_opts['format'] = f"{format_id}+bestaudio"

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        log_download(title, 'MP3' if is_mp3 else 'MP4', filename)
        print(f"\n🎉 File tersimpan di: {output_path}")
    except Exception as e:
        print(f"❌ Gagal mengunduh: {e}")

def main():
    """Fungsi utama program."""
    while True:
        print("\n" + "#"*50)
        print("  YouTube Downloader CLI (Ketuk ENTER untuk keluar)")
        print("#"*50)
        url = input("Masukkan URL YouTube: ")
        
        if not url:
            break

        info, video_formats, audio_formats = get_formats(url)
        if not info:
            continue

        try:
            all_formats = video_formats + audio_formats

            choice_str = input("Pilih format (contoh: '0' untuk video, '10' untuk audio) atau 'exit': ")
            if choice_str.lower() == 'exit':
                break
            
            choice_index = int(choice_str)
            
            if choice_index < 0 or choice_index >= len(all_formats):
                print("Pilihan tidak valid.")
                continue
            
            selected_format = all_formats[choice_index]
            
            is_mp3_option = choice_index >= len(video_formats)

            if is_mp3_option:
                download_file(url, 'bestaudio', True, info.get('title'))
            else:
                download_file(url, selected_format['format_id'], False, info.get('title'))

        except (ValueError, IndexError):
            print("Input tidak valid. Silakan masukkan angka.")
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")

if __name__ == "__main__":
    main()
