# 🔊 Text-to-Speech

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![gTTS](https://img.shields.io/badge/gTTS-Google%20Text--to--Speech-red)](https://gtts.readthedocs.io/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

**Text-to-Speech** adalah tool sederhana berbasis Python untuk mengubah teks menjadi suara menggunakan **Google Text-to-Speech (gTTS)**. Hasil konversi dapat langsung disimpan sebagai file **MP3**.

Tool ini cocok digunakan untuk kebutuhan sederhana seperti membuat audio dari teks, pembelajaran bahasa, eksperimen text-to-speech, maupun pembuatan suara secara cepat melalui terminal.

> **Catatan:** gTTS memerlukan koneksi internet karena proses sintesis suara menggunakan layanan Google Text-to-Speech.

---

## 📑 Daftar Isi

- [Fitur](#-fitur)
- [Teknologi](#-teknologi)
- [Instalasi](#-instalasi)
- [Cara Pakai](#-cara-pakai)
- [Bahasa yang Didukung](#-bahasa-yang-didukung)
- [Contoh](#-contoh)
- [Struktur Project](#-struktur-project)
- [Troubleshooting](#-troubleshooting)
- [Kontribusi](#-kontribusi)
- [Author](#-author)
- [Lisensi](#-lisensi)

---

## ✨ Fitur

- 🎙️ Convert teks menjadi suara dalam format **MP3**
- 🌍 Mendukung **18+ bahasa**
- 🐢 Mode lambat untuk pengucapan yang lebih jelas
- 📄 Dapat mengubah isi file teks menjadi suara
- 💬 Mode interaktif untuk memasukkan teks langsung dari terminal
- ⚡ Ringan dan cepat digunakan
- 🔑 Tidak membutuhkan API key
- 🆓 Gratis untuk digunakan sesuai ketentuan layanan gTTS/Google

---

## 🛠️ Teknologi

| Teknologi | Keterangan |
|---|---|
| **Python 3.8+** | Bahasa pemrograman utama |
| **gTTS** | Library Google Text-to-Speech |
| **CLI** | Antarmuka berbasis Command Line |
| **MP3** | Format file audio hasil konversi |

Library yang digunakan:

```text
gTTS
```

---

## 📦 Instalasi

### 1. Clone repository

```bash
git clone https://github.com/dimasnaufal18/text-to-speech.git
cd text-to-speech
```

### 2. Pastikan Python sudah terpasang

Periksa versi Python:

```bash
python --version
```

Pastikan menggunakan **Python 3.8 atau lebih baru**.

### 3. Install dependency

```bash
pip install -r requirements.txt
```

Atau langsung install gTTS:

```bash
pip install gTTS
```

Setelah instalasi selesai, project siap digunakan.

---

## 🚀 Cara Pakai

### Convert teks menjadi suara

```bash
python main.py "Halo, selamat pagi!" output.mp3
```

### Menggunakan bahasa Inggris

```bash
python main.py "Hello, good morning!" output.mp3 -l en
```

### Menggunakan mode lambat

Mode `--slow` dapat digunakan untuk menghasilkan pengucapan yang lebih lambat dan jelas.

```bash
python main.py "Selamat pagi" output.mp3 --slow
```

### Convert dari file teks

Siapkan file, misalnya `input.txt`, kemudian jalankan:

```bash
python main.py --file input.txt output.mp3
```

### Melihat daftar bahasa

```bash
python main.py --list-langs
```

### Mode interaktif

Jalankan tanpa argumen:

```bash
python main.py
```

Kemudian ikuti instruksi yang muncul di terminal.

---

## 🌍 Bahasa yang Didukung

| Kode | Bahasa |
|---|---|
| `id` | Indonesia |
| `en` | English |
| `ja` | Japanese |
| `ko` | Korean |
| `ar` | Arabic |
| `zh-CN` | Chinese Simplified |
| `es` | Spanish |
| `fr` | French |
| `de` | German |
| `ru` | Russian |
| `th` | Thai |
| `vi` | Vietnamese |
| `ms` | Malay |
| `tl` | Filipino |
| `hi` | Hindi |
| `tr` | Turkish |
| `pt` | Portuguese |
| `it` | Italian |

> Daftar bahasa mengikuti dukungan yang tersedia pada gTTS dan dapat berubah seiring waktu.

---

## 💡 Contoh

### Bahasa Indonesia

```bash
python main.py "Selamat datang di project Text-to-Speech!" output.mp3 -l id
```

Hasil:

```text
output.mp3
```

### Bahasa Inggris

```bash
python main.py "Welcome to the Text-to-Speech project!" output.mp3 -l en
```

### Bahasa Jepang

```bash
python main.py "おはようございます" output.mp3 -l ja
```

### Dari file teks

Contoh isi `input.txt`:

```text
Selamat datang.
Ini adalah contoh penggunaan Text-to-Speech menggunakan Python dan gTTS.
```

Kemudian jalankan:

```bash
python main.py --file input.txt output.mp3
```

File audio akan tersimpan sebagai:

```text
output.mp3
```

---

## 📁 Struktur Project

```text
text-to-speech/
├── main.py
├── requirements.txt
├── README.md
├── LICENSE
└── examples/
    └── output/
```

### Penjelasan

- `main.py` — Program utama untuk proses text-to-speech.
- `requirements.txt` — Daftar dependency Python yang diperlukan.
- `README.md` — Dokumentasi project.
- `LICENSE` — Lisensi MIT.
- `examples/output/` — Folder untuk menyimpan contoh file audio hasil konversi.

---

## 🔧 Troubleshooting

### `ModuleNotFoundError: No module named 'gtts'`

Install library gTTS dengan:

```bash
pip install gTTS
```

Jika menggunakan beberapa versi Python, coba:

```bash
python -m pip install gTTS
```

### Tidak dapat membuat file MP3

Pastikan perangkat memiliki **koneksi internet yang aktif**, karena gTTS membutuhkan akses ke layanan Google Text-to-Speech.

### Perintah `python` tidak ditemukan

Pada beberapa sistem, Python dapat dipanggil menggunakan `python3`:

```bash
python3 main.py "Halo, dunia!" output.mp3
```

Instalasi Python dapat dilakukan melalui [python.org](https://www.python.org/).

### Bahasa tidak tersedia

Gunakan perintah berikut untuk melihat bahasa yang tersedia pada versi project yang digunakan:

```bash
python main.py --list-langs
```

---

## 🤝 Kontribusi

Kontribusi sangat terbuka. Jika ingin membantu mengembangkan project ini, silakan:

1. **Fork** repository.
2. Buat branch baru:

```bash
git checkout -b fitur-baru
```

3. Lakukan perubahan dan pengujian.
4. Commit perubahan:

```bash
git commit -m "Menambahkan fitur baru"
```

5. Push branch:

```bash
git push origin fitur-baru
```

6. Buat **Pull Request**.

Untuk perubahan besar, disarankan membuka issue terlebih dahulu agar perubahan dapat didiskusikan.

---

## 👤 Author

**Mhd Dimas Naufal**

- GitHub: [@dimasnaufal18](https://github.com/dimasnaufal18)

---

## 📄 Lisensi

Project ini menggunakan **MIT License**.

Anda bebas menggunakan, menyalin, memodifikasi, dan mendistribusikan project ini dengan tetap mengikuti ketentuan yang tercantum pada file [`LICENSE`](LICENSE).

---

<p align="center">
  Made using Python & gTTS
</p>
