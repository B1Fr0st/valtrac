import base64,hashlib,json
from storyline import story
from time import time

print("Encrypting game...")
#Delete this after game is finalized, or comment it out.
start = time()
with open('maingame.py','r') as file:
  string = file.read()
encoded = base64.b64encode(base64.b64encode(base64.b64encode(string.encode()))).decode()
with open("encrypted_main.txt","w") as file:
    file.write(encoded+"."+hashlib.sha256(encoded.encode()).hexdigest().upper())


print("Encrypting story...")
dumped = json.dumps(story)
encoded = base64.b64encode(base64.b64encode(dumped.encode())).decode()
with open("encrypted.txt","w") as file:
  file.write(encoded+"."+hashlib.sha256(encoded.encode()).hexdigest().upper())
end = time()
t_time = end-start
print(f"Finished encryption; took {t_time} seconds.")