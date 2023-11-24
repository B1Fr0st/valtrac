import base64,hashlib
import encryption #Encodes everything, remove when fully published.


with open("encrypted_main.txt","r") as file:
  encoded = file.read()
encoded = encoded.split(".")
hash = encoded[1]
encoded = encoded[0]
if hashlib.sha256(encoded.encode()).hexdigest().upper() != hash:
  raise Exception("Hash mismatch;dirty cheater.")
decoded = base64.b64decode(base64.b64decode(base64.b64decode(encoded.encode()))).decode()
eval(compile(decoded,'testing.py','exec'))