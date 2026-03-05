import random
import math

class RSAProgram:

    # =================================
    # Inisialisasi + Key Generation
    # =================================
    def __init__(self):
        self.p = self.random_prime()
        self.q = self.random_prime()

        while self.q == self.p:
            self.q = self.random_prime()

        self.n = self.p * self.q
        self.phi = (self.p - 1) * (self.q - 1)

        self.e = self.select_e()
        self.d = self.calculate_d(self.e, self.phi)

    # =================================
    # Mengecek apakah bilangan prima
    # =================================
    def check_prime(self, num):
        if num <= 1:
            return False
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True

    # =================================
    # Membuat bilangan prima acak
    # =================================
    def random_prime(self, start=100, end=300):
        while True:
            value = random.randint(start, end)
            if self.check_prime(value):
                return value

    # =================================
    # Menentukan nilai e
    # =================================
    def select_e(self):
        e = 3
        while math.gcd(e, self.phi) != 1:
            e += 2
        return e

    # =================================
    # Extended Euclidean Algorithm
    # =================================
    def egcd(self, a, b):
        if b == 0:
            return a, 1, 0
        gcd, x1, y1 = self.egcd(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return gcd, x, y

    # =================================
    # Menghitung d (modular inverse)
    # =================================
    def calculate_d(self, e, phi):
        gcd, x, y = self.egcd(e, phi)
        if gcd != 1:
            raise Exception("Modular inverse tidak ditemukan")
        return x % phi

    # =================================
    # Proses Enkripsi
    # =================================
    def encrypt(self, message):
        cipher = pow(message, self.e, self.n)
        return cipher

    # =================================
    # Proses Dekripsi
    # =================================
    def decrypt(self, cipher):
        plain = pow(cipher, self.d, self.n)
        return plain


# =================================
# MAIN PROGRAM
# =================================

rsa = RSAProgram()

print("===== PEMBANGKITAN KUNCI =====")
print("p =", rsa.p)
print("q =", rsa.q)
print("n =", rsa.n)
print("phi(n) =", rsa.phi)

print("Public Key  :", (rsa.e, rsa.n))
print("Private Key :", (rsa.d, rsa.n))

# contoh pesan
message = 20

ciphertext = rsa.encrypt(message)
decrypted = rsa.decrypt(ciphertext)

print("\n===== PROSES ENKRIPSI =====")
print("Plaintext  :", message)
print("Ciphertext :", ciphertext)

print("\n===== PROSES DEKRIPSI =====")
print("Hasil Dekripsi :", decrypted)
