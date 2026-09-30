"""
Text to Speech
Convert teks jadi suara pakai Google Text-to-Speech (gTTS).

Author: Mhd Dimas Naufal
"""

import os
import sys
import argparse
from gtts import gTTS


# Bahasa yang didukung
LANGUAGES = {
    'id': 'Indonesia',
    'en': 'English',
    'ja': 'Japanese',
    'ko': 'Korean',
    'ar': 'Arabic',
    'zh-CN': 'Chinese (Simplified)',
    'es': 'Spanish',
    'fr': 'French',
    'de': 'German',
    'ru': 'Russian',
    'th': 'Thai',
    'vi': 'Vietnamese',
    'ms': 'Malay',
    'tl': 'Filipino',
    'hi': 'Hindi',
    'tr': 'Turkish',
    'pt': 'Portuguese',
    'it': 'Italian',
}


def text_to_speech(text, output_path, lang='id', slow=False):
    """
    Convert teks jadi suara.
    
    Args:
        text (str): Teks yang mau di-convert
        output_path (str): Path file output (.mp3)
        lang (str): Kode bahasa (default: 'id' untuk Indonesia)
        slow (bool): Mode lambat (default: False)
    
    Returns:
        bool: True kalau berhasil
    """
    try:
        print(f"🎵 Bahasa  : {LANGUAGES.get(lang, lang)}")
        print(f"🐢 Mode    : {'Lambat' if slow else 'Normal'}")
        print(f"📁 Output  : {output_path}")
        print()
        print("⏳ Sedang convert...")
        
        # Convert teks jadi suara
        tts = gTTS(text=text, lang=lang, slow=slow)
        tts.save(output_path)
        
        # Hitung ukuran file
        size = os.path.getsize(output_path)
        
        return True, size
    
    except Exception as e:
        print(f"❌ Error: {e}")
        return False, 0


def format_size(bytes_size):
    """Format ukuran bytes jadi KB/MB."""
    if bytes_size < 1024:
        return f"{bytes_size} B"
    elif bytes_size < 1024 * 1024:
        return f"{bytes_size / 1024:.2f} KB"
    else:
        return f"{bytes_size / (1024 * 1024):.2f} MB"


def list_languages():
    """Tampilkan daftar bahasa yang didukung."""
    print("=" * 50)
    print("   🌍 BAHASA YANG DIDUKUNG")
    print("=" * 50)
    for code, name in LANGUAGES.items():
        print(f"  {code:<6} : {name}")
    print("=" * 50)


def main():
    print("=" * 50)
    print("   🔊 TEXT TO SPEECH")
    print("=" * 50)
    print()
    
    parser = argparse.ArgumentParser(
        description="Convert teks jadi suara pakai Google TTS.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Contoh penggunaan:

  1. Convert teks ke suara (Indonesia):
     python main.py "Halo, selamat pagi!" output.mp3

  2. Convert dengan bahasa Inggris:
     python main.py "Hello, good morning!" output.mp3 -l en

  3. Convert dengan mode lambat:
     python main.py "Selamat pagi" output.mp3 --slow

  4. Lihat daftar bahasa:
     python main.py --list-langs

  5. Convert dari file teks:
     python main.py --file input.txt output.mp3
        """
    )
    
    parser.add_argument("text", nargs="?", help="Teks yang mau di-convert")
    parser.add_argument("output", nargs="?", default="output.mp3", help="Path file output (default: output.mp3)")
    parser.add_argument("-l", "--lang", default="id", help="Kode bahasa (default: id)")
    parser.add_argument("-s", "--slow", action="store_true", help="Mode lambat")
    parser.add_argument("--file", help="Convert dari file teks")
    parser.add_argument("--list-langs", action="store_true", help="Tampilkan daftar bahasa")
    
    args = parser.parse_args()
    
    # Tampilkan daftar bahasa
    if args.list_langs:
        list_languages()
        return
    
    # Cek bahasa valid
    if args.lang not in LANGUAGES:
        print(f"❌ Bahasa '{args.lang}' gak didukung!")
        print(f"   Pakai --list-langs buat lihat daftar bahasa.")
        return
    
    # Ambil teks
    text = ""
    if args.file:
        # Baca dari file
        if not os.path.exists(args.file):
            print(f"❌ File tidak ditemukan: {args.file}")
            return
        with open(args.file, 'r', encoding='utf-8') as f:
            text = f.read().strip()
        print(f"📄 Baca dari file: {args.file}")
    elif args.text:
        text = args.text.strip()
    else:
        # Mode interaktif
        print("📝 Masukkan teks (tekan Enter 2x buat selesai):")
        lines = []
        while True:
            try:
                line = input()
                if line == "" and len(lines) > 0 and lines[-1] == "":
                    break
                lines.append(line)
            except EOFError:
                break
        text = "\n".join(lines).strip()
    
    if not text:
        print("❌ Teks kosong!")
        return
    
    print(f"📝 Teks    : {text[:80]}{'...' if len(text) > 80 else ''}")
    print()
    
    # Pastikan output .mp3
    if not args.output.lower().endswith(".mp3"):
        args.output += ".mp3"
    
    # Convert
    success, size = text_to_speech(text, args.output, args.lang, args.slow)
    
    if success:
        print()
        print("=" * 50)
        print("   ✅ BERHASIL!")
        print("=" * 50)
        print(f"📁 File output : {args.output}")
        print(f"📊 Ukuran      : {format_size(size)}")
        print(f"🌍 Bahasa      : {LANGUAGES[args.lang]}")
        print("=" * 50)
    else:
        print()
        print("❌ Gagal convert teks ke suara.")


if __name__ == "__main__":
    main()