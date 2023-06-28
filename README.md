### ReQTest 🕵️

[English Documentation](https://github.com/lahadiyani/ReQTest/blob/main/English.md)

## Deskripsi 😄
ReQTest adalah sebuah alat yang dirancang untuk melakukan pengujian keamanan dan performa terhadap sebuah website atau layanan dengan mengirimkan serangan flood menggunakan UDP dan mengirimkan request HTTP. Alat ini dapat membantu dalam mengidentifikasi kerentanan dan mengukur kinerja sistem.

## Requirement 😀
Alat ReQTest memerlukan instalasi beberapa dependensi dan modul Python berikut:
- Python 3.x
- requests
- colorama
- Tor

Anda dapat menginstal dependensi tersebut dengan menggunakan perintah berikut melalui pip:
```
pip install requests colorama
```

## Cara Penggunaan 😁
Berikut adalah langkah-langkah untuk menggunakan alat ReQTest:

1. Unduh kode sumber ReQTest dari repository GitHub.
2. Pastikan semua dependensi terinstal dengan menjalankan perintah `pip install -r requirements.txt`.
3. Buka terminal atau command prompt dan navigasikan ke direktori tempat Anda menyimpan kode ReQTest.
4. Jalankan alat ReQTest dengan menjalankan perintah `python reqtest.py`.
5. Anda akan melihat banner ReQTest dan beberapa pertanyaan yang harus dijawab untuk memulai pengujian.
6. Masukkan URL target yang ingin diuji.
7. Masukkan jumlah request yang diinginkan.
8. Masukkan max delay antara request (dalam detik).
9. Masukkan alamat IP target yang akan diserang flood.
10. Masukkan port target yang akan diserang flood.
11. Masukkan durasi serangan flood (dalam detik).
12. Alat ReQTest akan mulai mengirim request ke server target dan menampilkan status code, waktu respons server, dan status kesehatan situs.
13. Setelah selesai, hasil pengujian akan disimpan dalam file "hasil.txt" yang berisi informasi tentang setiap request yang dikirim dan respons dari server.
14. Selama serangan flood berlangsung, alat akan mencetak jumlah paket yang dikirim ke victim.

Pastikan Anda menggunakan alat ini hanya untuk tujuan pengujian yang sah dan tidak melanggar hukum atau merugikan pihak lain. Jangan menguji website atau sistem yang tidak Anda miliki izin untuk diuji.

## Alat yang Dibutuhkan 😅
- Python 3.x: Interpreter bahasa Python yang digunakan untuk menjalankan alat ReQTest.
- requests: Modul Python untuk mengirimkan request HTTP ke server target.
- colorama: Modul Python untuk memberikan warna pada output konsol.

Pastikan Anda memiliki versi Python yang sesuai dan menginstal semua modul yang diperlukan sebelum menggunakan alat ReQTest.

[saweria seikhlasnya](https://saweria.co/hadiani)
