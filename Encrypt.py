
# AES256 is a symmetric encryption algorithm that uses a 256-bit key to encrypt and decrypt data
# To use AES256 in python, we can use the PyCryptodome library
# We can install PyCryptodome with pip: pip install pycryptodome
# First, we need to import the modules we need.
import hashlib
import getpass
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from Crypto.Protocol.KDF import PBKDF2
# Next, we need to generate a random 256-bit key and save it to a file
# We can use the get_random_bytes function to generate the key

# Then, we need to enter your password and generate a random salt

while(True):

    password = getpass.getpass("Enter your password: ")
    recheck_password = getpass.getpass("Re-enter your password: ")
    if(password == recheck_password):
        break
    print("Please try again, password didn't match")

password = str.encode(password)
# salt = get_random_bytes(16) # generate a random salt as an alternative
salt = getpass.getpass("Enter your salt: ")
salt = str.encode(salt)

# Hash text_input using pbkdf2_hmac() function
key = hashlib.pbkdf2_hmac('sha256', password, salt, iterations=100000) # more iterations more secure
# Convert hash object to hexadecimal string
hex_dig = key.hex()
print(hex_dig)

with open("key.bin", "wb") as f:
    f.write(key)

# Then, we need to create an AES cipher object with the key and a random initialization vector (IV)
# We can use the AES.new function to create the cipher object
# We can use the get_random_bytes function again to generate the IV
iv = get_random_bytes(16) # 32 bytes = 256 bits
cipher = AES.new(key, AES.MODE_CBC, iv)

# Now, we need to read the data from the file we want to encrypt and pad it to a multiple of 16 bytes
# We can use the open function to read the file in binary mode
# We can use the pad function to pad the data with PKCS7 padding
filename = input("Enter Filename: ")
with open(filename, "rb") as f:
    data = f.read()
data = pad(data, 16)

# Next, we need to encrypt the data with the cipher object and save it to a new file along with the IV
# We can use the encrypt function to encrypt the data
# We can use the open function again to write the file in binary mode
encrypted_filename = input("Enter encrypted filename (default is your filename.enc) ")
whitespace = [' ', '\t', '\n', '\b']
if (encrypted_filename == "" and encrypted_filename not in whitespace):

    encrypted_filename = filename.split('.')[0] + '.enc'
with open(encrypted_filename, "wb") as f:
    f.write(iv) # write the IV first
    f.write(cipher.encrypt(data)) # write the encrypted data

# Finally, we have encrypted the file with aes256 and saved it as file.enc
# To decrypt the file, we need to reverse the process using the same key and IV
