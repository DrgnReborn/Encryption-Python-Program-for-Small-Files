
#First thing we want to do is import our cryptography libraries.
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes, serialization

#Then we need to load the public key we made.
with open("public_key.pem", "rb") as f:
    #Then we assign it to a variable for use.
    public_key = serialization.load_pem_public_key(f.read())

#Next we need to read the file we are encrypting.
with open("FirstEncryption.txt", "rb") as f:
    #We assign the file we have read into binary code to a variable.
    message = f.read()

#We then encrypt the message.
cyphertext = public_key.encrypt(message, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),algorithm=hashes.SHA256(),label=None))

#Then we save the encrypted data.
with open("encrypted.bin", "wb") as f:
    f.write(cyphertext)

print("The file has been encrypted.")