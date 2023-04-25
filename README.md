### AES 256-bit Encryption for Personal Files

## Description
This GitHub repository contains Python code for encrypting personal files using the AES 256-bit encryption algorithm. The code provides a simple and secure way to protect your sensitive files from unauthorized access.

To use this code, simply download or clone the repository, install the required dependencies, and run the encrypt.py script with the file or directory you want to encrypt as the input. The output will be a new encrypted file or directory with the .enc extension.

The code uses the PyCrypto library, which provides a robust implementation of the AES 256-bit encryption algorithm. The key for the encryption is generated from a user-provided passphrase, which is hashed using SHA-256 for added security.

The repository also includes a decrypt.py script for decrypting files or directories that have been encrypted with this code. To decrypt a file or directory, simply run the decrypt.py script with the encrypted file or directory as the input. The output will be a new decrypted file or directory with the original name and extension.

This repository is useful for anyone who wants to protect their personal files from unauthorized access or for developers who want to implement secure encryption in their own projects. The code is open-source and can be customized to fit specific use cases.

## Installation
To use this code, simply download or clone the repository and install the required dependencies:
```bash
pip install -r requirements.txt
```

## Contributing
Pull requests are welcome.

## License
[MIT](https://choosealicense.com/licenses/mit/)
