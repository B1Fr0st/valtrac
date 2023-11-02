import base64
import hashlib
import json
import os
import sys
import time
import random
import storyline #Remove this line when finalizing game, serves to reencode storyline each time the main game is run
from replit import audio

from variables import title, audio_titles, help_text, quit_text, death_text





def clr():os.system("clear")#A lot better than last years lol


#Load audio files
print("Loading audio files...")




audio_files = {}
i = 0
for item in audio_titles:
  i+=1
  if not os.path.isfile(f"./music/{item}.mp3"):
    print(f"AUDIO FILE NOT FOUND:{item}.mp3")
    exit()#This will crash the game later so crash it now
  audio_files[item] = f"./music/{item}.mp3"
  print(f"Loaded track {i}/{len(audio_titles)}: {item}.mp3")

#Double b64 encryption with a sha256checksum at the end, for both the story and main code.
with open("encrypted.txt","r") as file:
  encoded = file.read()
encoded = encoded.split(".")
hash = encoded[1]
encoded = encoded[0]
if hashlib.sha256(encoded.encode()).hexdigest().upper() != hash:
  raise Exception("Hash mismatch;dirty cheater.")
decoded = base64.b64decode(base64.b64decode(encoded.encode())).decode()
decoded = json.loads(decoded)
story = decoded
print("Loaded story")
time.sleep(1)
clr()




rprint = print #Just in case we need to utilize regular print for some reason.

def print(t,typing_speed=0.05):
  for char in t+"\n":
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(typing_speed)

def rem_print(t,typing_speed=0.05):
  """Slow prints a SINGLE line of text, and then removes it all one by one."""
  for char in t:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(typing_speed)
  time.sleep(1.5)
  for i in range(len(t)):
    rprint("\r"+t[:len(t)-i]+" ",end='\r')
    time.sleep(0.2)

  






#Attempts to play the title audio track; however, if the audio track fails to play, it raises a TimeoutError, the error count allows it to retry up to 3 times.
error_count = 0
while True:
  try:
    src = audio.play_file(audio_files["title"])
    break
  except TimeoutError:
    print("Retrying audio...")
    if error_count+1 == 3:
      print("Failed to start title audio track.")
      exit(1)




for line in title:
  rprint(line)
  time.sleep(0.3)
print("Commands:")
for command in help_text:
  print(command)
input("\n\n\nPress enter to continue...")
src.paused = True#pause title music

#Some people don't realize they should only press enter once
#This is to reassure them that the game is in fact starting.
clr()
print("Starting game...")
time.sleep(1)
clr()



inventory = {}
path = story["path"]
saved_path = ""
ending_1 = 0
ending_2 = 0
ending_3 = 0
disallowed_decisions = ["required_item","first_entry","first_entry_text","actions","go_back_not_allowed","text","inventory"] #All the hidden fields of a room that the user should not be able to access.




def finale(ending_1,ending_2,ending_3):
  pass #TODO


while True:
  game_path = path.split("-")
  storyline = story #Makes a copy of the true storyline so that we can select a specific room without changing the storyline.
  for item in game_path:
    storyline = storyline[item]#Turns a list of room paths into a dictionary path.

  #Path changing tags
  if "auto" in storyline:
    if "header" in storyline:
      rem_print(storyline["text"])
    else:
      print(storyline["text"])
    path += "-"+storyline["auto"]#go to next room specified by auto
    time.sleep(3)
    clr()
    continue
    
  if "clear" in storyline:
    if "header" in storyline:
      rem_print(storyline["text"])
    else:
      print(storyline["text"])
    path = storyline["clear"]#Clears story line and go to whatever path specified
    time.sleep(3)
    clr()
    continue
  if "audio" in storyline:
    src = audio.play_file(audio_files[storyline["audio"]])
  else:
    src.paused = True

  #Karma handling
  if "ending_1" in storyline:
    ending_1 += storyline["ending_1"]
    storyline["ending_1"] = 0
  if "ending_2" in storyline:
    ending_1 += storyline["ending_2"]
    storyline["ending_2"] = 0
  if "ending_3" in storyline:
    ending_1 += storyline["ending_3"]
    storyline["ending_3"] = 0
  
  
  clr()
  #Checks for a first_entry tag, if it's the players first time entering, print the special text instead of the normal text
  try:
    if storyline["first_entry"]:
      print(storyline["first_entry_text"])
      storyline["first_entry"] = False
    else:
      print(storyline["text"])
      
  except: 
    #If there is no special text, just print the regular text.
    print(storyline["text"])
  if "game_over" in storyline:
    time.sleep(2)
    clr()
    rem_print("GAME OVER")
    print(random.choice(death_text))
    time.sleep(1)
    exit()
  
  #Decision switching logic
  decision = ""
  while True:
    decision = input(">")
    if decision == "quit":
      print(random.choice(quit_text))
      exit(0)
    #ignore empty decisions
    if decision == "":
      continue
    elif decision == "help" or decision == "h":
      for line in help_text:
        print(line)
    #TODO
    elif decision == "ENDING LOGIC GOES HERE" and "ENDING ITEM GOES HERE" in inventory:
      finale(ending_1,ending_2,ending_3)
    
    elif decision == "back" and "go_back_not_allowed" not in storyline:
      #Remove the last decision made by the player
      path = "-".join(path.split("-")[:-1])
      
      break
      
    elif ("take" in decision or "get" in decision or "receive" in decision) and " ".join(decision.split(" ")[1:]) in storyline["inventory"]:
      itm = " ".join(decision.split(" ")[1:])
      inventory[itm] = storyline["inventory"].pop(itm)
      print(f"You got the {itm}")
      
    elif decision == "inventory":
      print("You are currently carrying:\n"+'\n'.join(inventory.keys()))
    elif "inspect" in decision and " ".join(decision.split(" ")[1:]) in inventory:
      itm = " ".join(decision.split(" ")[1:])
      if "inspect_text" in inventory[itm]:
        print(inventory[itm]["inspect_text"])
      else:
        print(f"Just a regular {itm}.")
    elif decision in storyline and decision not in disallowed_decisions:
      if "required_item" in storyline[decision]:
        if storyline[decision]["required_item"] not in inventory:
          print(f"You don't have the {storyline[decision]['required_item']} necessary to do that.")
        else:
          path += "-"+decision
          break
      else:
        path += "-"+decision
        break
    elif "actions" in storyline:
      if decision in storyline["actions"]:
        print(storyline["actions"][decision])
      else:
        print("invalid decision .")
    else:
      print("invalid decision.")


