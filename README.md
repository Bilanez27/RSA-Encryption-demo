# Implementasi Algoritma RSA (Rivest, Shamir, Adleman)

## 1. Pengantar Singkat

RSA merupakan salah satu algoritma kriptografi kunci publik (asymmetric cryptography) yang diperkenalkan pada tahun 1977 oleh tiga ilmuwan yaitu Ron Rivest, Adi Shamir, dan Leonard Adleman. Algoritma ini menggunakan dua jenis kunci yang berbeda yaitu public key dan private key.

Public key dapat dibagikan kepada siapa saja untuk melakukan proses enkripsi, sedangkan private key hanya diketahui oleh pemiliknya dan digunakan untuk proses dekripsi. Dengan metode ini, pesan dapat dikirim secara aman tanpa harus bertukar kunci rahasia secara langsung.

RSA banyak digunakan dalam berbagai sistem keamanan digital, seperti pengamanan koneksi internet melalui HTTPS, digital signature untuk memverifikasi keaslian dokumen, serta pertukaran kunci pada sistem enkripsi lainnya seperti AES.

---

## 2. Pembangkitan Kunci (Key Generation)

Proses pertama dalam algoritma RSA adalah membuat pasangan kunci yang terdiri dari public key dan private key.

Langkah-langkahnya adalah sebagai berikut:

1. Memilih dua bilangan prima berbeda, yaitu p dan q. Dalam implementasi nyata, bilangan ini biasanya sangat besar agar tingkat keamanan lebih tinggi.

2. Menghitung nilai n dengan rumus:

n = p × q

Nilai n akan digunakan pada public key dan private key.

3. Menghitung fungsi Euler menggunakan rumus:

φ(n) = (p − 1)(q − 1)

Nilai φ(n) digunakan untuk menentukan pasangan kunci.

4. Menentukan nilai e sebagai bagian dari public key, dengan syarat nilai e harus relatif prima terhadap φ(n).

5. Menghitung nilai d sebagai private key dengan persamaan:

d × e ≡ 1 (mod φ(n))

Setelah proses ini selesai, diperoleh pasangan kunci:

Public Key : (e, n)  
Private Key : (d, n)

---

## 3. Proses Enkripsi dan Dekripsi

Setelah pasangan kunci dibuat, RSA dapat digunakan untuk mengamankan pesan.

### Proses Enkripsi

Pesan asli (plaintext) terlebih dahulu diubah menjadi bentuk bilangan yang disebut m. Kemudian dilakukan proses enkripsi menggunakan public key dengan rumus:

c = m^e mod n

Hasil dari proses ini adalah ciphertext (c), yaitu pesan yang telah terenkripsi dan tidak dapat dibaca secara langsung.

Ciphertext kemudian dapat dikirimkan melalui jaringan komunikasi.

### Proses Dekripsi

Penerima yang memiliki private key dapat mengembalikan ciphertext menjadi pesan asli menggunakan rumus:

m = c^d mod n

Hasil dari perhitungan ini akan menghasilkan kembali nilai m yang kemudian dikonversi kembali menjadi plaintext sehingga pesan asli dapat dibaca.

---

## Program RSA

Repository ini berisi implementasi sederhana algoritma RSA menggunakan bahasa pemrograman Python. Program ini menunjukkan proses:

- Key Generation
- Enkripsi
- Dekripsi

Program dibuat tanpa menggunakan library kriptografi eksternal sehingga seluruh proses RSA dihitung secara manual.

---

## Cara Menjalankan Program

1. Clone repository ini
git clone https://github.com/Bilanez7/RSA-Encryption-demo.git

3. Masuk ke folder project
cd RSA-Encryption-demo

4. Jalankan program
python rsa_encryption.py

Program akan menampilkan proses pembangkitan kunci, enkripsi, dan dekripsi.

OUTPUT

===== PEMBANGKITAN KUNCI =====

p = 137

q = 191

n = 26167

phi(n) = 25840

Public Key  : (3, 26167)
Private Key : (17227, 26167)

===== PROSES ENKRIPSI =====

Plaintext  : 20

Ciphertext : 8000


===== PROSES DEKRIPSI =====

Hasil Dekripsi : 20


Artinya:

plaintext → pesan asli

ciphertext → pesan terenkripsi

dekripsi → kembali ke pesan asli
