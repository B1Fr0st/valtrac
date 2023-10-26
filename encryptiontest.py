import base64,hashlib


with open('main.py','r') as file:
  string = file.read()
encoded = base64.b64encode(base64.b64encode(base64.b64encode(string.encode()))).decode()
with open("encrypted_main.txt","w") as file:
    file.write(encoded+"."+hashlib.sha256(encoded.encode()).hexdigest().upper())

with open("encrypted_main.txt","r") as file:
  encoded = file.read()
encoded = encoded.split(".")
hash = encoded[1]
encoded = encoded[0]
if hashlib.sha256(encoded.encode()).hexdigest().upper() != hash:
  raise Exception("Hash mismatch;dirty cheater.")
decoded = base64.b64decode(base64.b64decode(base64.b64decode(encoded.encode()))).decode()
eval(compile(decoded,'testing.py','exec'))