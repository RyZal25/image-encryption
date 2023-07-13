#!/usr/bin/env python3
# import library untuk membantu proses Encryption
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto.Util.Padding import pad

# pengenalan lingkukan OS ke program agar dapat melakukan operasi yang melibatkan OS
import os

# membaca file input yang akan di enkrip
input_file = "nama_file_yang_ingin_dienkripsi.jpg/.png/dll"
with open(input_file, "rb") as f:
    data = f.read()

# fungsi yang digunakan untuk mengenkrip data menggunakan AES-CBC
def encrypt_data(msg: bytes, key: bytes):
    key = SHA256.new(key).digest()
    iv = os.urandom(AES.block_size)
    aes = AES.new(key, AES.MODE_CBC, iv)
    enc = aes.encrypt(pad(msg, AES.block_size))
    return iv + enc

# fungsi untuk mengenkripsi data 2 stack dengan menggunakan key yang berbeda dan secara acak
def double_encrypt(msg: bytes):
    keys = [os.urandom(32) for _ in range(2)]
    for key in keys:
        msg = encrypt_data(msg, key)
    return keys, msg

# menuliskan hasil keluaran enkripsi pada nama file yang diinginkan dan lokasi yang diinginkan
output_file = "nama_file_enkripsi.enc"
keys, encrypted_data = double_encrypt(data)
with open(output_file, "wb") as f:
    f.write(encrypted_data)

# memberikan informasi terkait file hasil enkripsi
print("File '{}' berhasil dienkrip {}".format(input_file))
print("Hasil enkripsi disimpan di file '{}'".format(output_file))

# menyimpan kunci enkripsi di tempat berbeda dan usahakan di sembunyikan (Admin only) untuk mempermudah proses penerjemahan
output_key_file = "path/hidden/key.txt"
with open(output_key_file, "w") as f:
    f.write("Key :{}\n".format(keys))

print("Key telah diamankan")
