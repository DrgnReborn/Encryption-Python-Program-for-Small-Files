
#First thing is to import what we need from the cryptography library.
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes, serialization

#We then need to load the private key we created for use with decryption.
with open("private_key.pem", "rb") as f:
    private_key = serialization.load_pem_private_key(f.read(), password=None)

#Next we need to open the file we encrypted by reading it into a variable.
with open("encrypted.bin", "rb") as f:
    ciphertext = f.read()

#Then we decript the data we read into the variable with our private key.
plaintext = private_key.decrypt(ciphertext, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),algorithm=hashes.SHA256(),label=None))

#Then we save the decrypted data
with open("decrypted.txt", "wb") as f:
    f.write(plaintext)

print ("File decrypted.")