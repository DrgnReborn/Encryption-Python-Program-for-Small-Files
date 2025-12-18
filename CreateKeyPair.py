
#To encrypt the file we need to import first.
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

#First thing we need to do is generate an RSA key pair.  
#The public_exponent variable is chosen because it is large 
# enough that it is safe but also fast and efficient.
private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)

#We need to save the Private and Public keys for future use.
with open("private_key.pem", "wb") as f:   #Opens file and writes in binary.
    f.write(private_key.private_bytes(     #Writes the private key into the file after converting it into bytes.
        encoding=serialization.Encoding.PEM, #Specifies the format which is PEM a Base64 format.
        format=serialization.PrivateFormat.TraditionalOpenSSL, #Format of the key using SSL compatible with many tools
        encryption_algorithm=serialization.NoEncryption() #This does not encrypt the private key file which you would want to in real production.
    ))

#Then we need to save the public key for future use.
public_key=private_key.public_key()  #This derives the public key from the private key object.
with open("public_key.pem", "wb") as f:
    f.write(public_key.public_bytes(
        encoding=serialization.Encoding.PEM, 
        format=serialization.PublicFormat.SubjectPublicKeyInfo)) #Saves the public key in standard X.509 format.
    
print("RSA key pair generated.")