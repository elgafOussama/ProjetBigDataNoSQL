import pyAesCrypt
# encryption/decryption buffer size - 64K
bufferSize = 64 * 1024
password = "foopassword"
# decrypt
pyAesCrypt.decryptFile("dataset.aes", "datasetOUT.csv", password, bufferSize)