import pyAesCrypt

# encryption/decryption buffer size - 64K
bufferSize = 64 * 1024
password = "foopassword"
# encrypt
pyAesCrypt.encryptFile("dataset.csv", "dataset.aes", password, bufferSize)
