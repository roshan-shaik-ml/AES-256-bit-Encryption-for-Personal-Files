from Crypto.PublicKey import RSA
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

# First, we need to read the encrypted data from the file
# We can use the open function to read the file in binary mode
filename = input("Enter encrypted filename: ")
with open(filename, "rb") as f:
    iv = f.read(16) # read the IV first
    ciphertext = f.read() # read the encrypted data

# Next, we need to create an AES cipher object with the key and IV
# We can use the AES.new function to create the cipher object
with open('key.bin', 'rb') as f:
    key = f.read()

cipher = AES.new(key, AES.MODE_CBC, iv)

# Now, we need to decrypt the data with the cipher object and unpad it
# We can use the decrypt function to decrypt the data
plaintext = unpad(cipher.decrypt(ciphertext), 16)

# Finally, we can write the decrypted data to a new file
output_filename = input("Enter output filename (with ext): ")
with open(output_filename, "wb") as f:
    f.write(plaintext)