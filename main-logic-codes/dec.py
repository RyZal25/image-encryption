#!/usr/bin/env python3
# impor library pendukung algoritma Encription and Decryption
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto.Util.Padding import unpad

# pengenalan lingkungan OS untuk mempermudah otomatisasi program untuk melakukan operasi yang melibatkan OS
import os

# fungsi yang akan digunakan untuk mendekrip data menggunakan AES-CBC
def decrypt_data(enc: bytes, key: bytes, iv: bytes):
    key = SHA256.new(key).digest()
    aes = AES.new(key, AES.MODE_CBC, iv)
    msg = aes.decrypt(enc)
    return unpad(msg, AES.block_size)

# fungsi untuk melakukan dekrip berlapis sebanyak 2 stack dengan implementasi key berbeda
def double_decrypt(enc: bytes, keys: list):
    keys = keys[::-1]
    for key in keys:
        iv, enc = enc[:AES.block_size], enc[AES.block_size:]
        key = key
        enc = decrypt_data(enc, key, iv)
    return enc

# membaca isi file yang akan di dekrip valuenya
input_file = "nama_file_enkripsi.enc"
with open(input_file, "rb") as f:
    data = f.read()

# mendeskripsikan hasil keluaran berupa nama file dan menampilkan hasil dekrip file
output_file = "nama_file_output.jpg/.png/dll" #usahakan samakan ekstensi dengan file awalnya
keys = ["b'KEY 1","b'KEY 2"] #anda bisa copy dari file .txtnya
decrypted_data = double_decrypt(data, keys)
with open(output_file, "wb") as f:
    f.write(decrypted_data)

# memberikan informasi terkait hasil keluaran program pada pengguna
print("File '{}' ini berhasil didekrip dengan menggunakan kunci yang diberikan".format(input_file))
print("Hasil dekripsi disimpan pada file '{}'".format(output_file))
