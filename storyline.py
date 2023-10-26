import base64, hashlib,json

story = {
  "path":"prologue", #What part of the story the player starts on. Can be edited for development purposes.
  "prologue":{
    "auto":"prologue1",
    "header":0,
    "text":"PROLOGUE",
    "prologue1":{
      "go_back_not_allowed":0,
      "text":"You wake up in a dark room. Your head is throbbing and you can't focus your eyes.",
      "actions":{"look around":"You look around and see a faint glow coming from the corner. Perhaps you could go to the corner?"},
      "go to corner":{
        "go_back_not_allowed":0,
        "text":"It's a flipped over phone, the screen is still on. Look at the screen?",
        "yes":{
          "auto":"prologue2",
          "text":"There's a single notification on the screen. On it it says...",
          "prologue2":{
            "clear":"ch1",
            "text":"You should have never woken up."
            }
        }
      }


    }
  },
  "ch1":{
    "auto":"ch1_01",
    "header":0,
    "text":"CHAPTER 1",
    "ch1_01":{
      "go_back_not_allowed":0,
      "first_entry": True,
      "audio":"rain",
      "first_entry_text":"It's pouring down outside as you swipe your hastily-copied keycard along the keycard reader.\nIt thinks for a second, then silently opens the silver door beside it, revealing a darkened room inside.",
      "text":"It's still pouring down outside.",
      "go inside":{
        "first_entry":True,
        "first_entry_text":"As you hurry inside, the motion sensitive lights inside flicker on.\nYou see the guard checkpoint ahead, and you pray that he doesn't know you were fired a few hours ago.As you approach the guarded checkpoint, you slow down from the breakneck run that you didn't quite realize you were doing.\nYou walk up to the solid plexiglass separating you from the guard.\n\nDIALOGUE OPTIONS:\n[make small talk]\n[kill him]\n[stay silent]",
        "text":"You walk up to the solid plexiglass separating you from the guard.\n\nDIALOGUE OPTIONS:\n[make small talk]\n[kill him]\n[stay silent]",
        "stay silent":{
          "clear":"ch1-ch1_02",
          "text":"tbd"
        },
        "kill him":{
          "clear":"ch1-ch1_02",
          "text":"tbd"
        },
        "make small talk":{
          "clear":"ch1-ch1_02",
          "text":"tbd"
        }
      }
    },
    "ch1_02":{
      "go_back_not_allowed":0,
      "text":"also tbd"
    },
    "ch1_03":{
      
    },
    "ch2_01":{
      
    }
  }
}
"""Guide to editing the story:
Each dictionary is a "room". Specifications:
R-"text": provides the text the user recieves when entering the room
"inventory: provides items that can be taken from that room
"required_item": tag that only allows the player into the room if they have the item
"first_entry": tag that indicates whether or not this is the players first time entering this room.
"first_entry_text": if the player enters while first_entry is true, print first_entry_text instead of the regular text.
"actions": Actions the player can take that won't take them out of their current room.
"auto": Tag that indicates whether or not the room will automatically proceed to the next, and what the next room is named.
"clear": Clears the path and sets the path to whatever the value of clear is.
"header": Whether or not to use rem_print on the text. Only checked for if "clear" or "auto" is also a tag.
"""


assignMode = True #Whether or not to be updating encrypted.txt
if assignMode is True:
  dumped = json.dumps(story)
  encoded = base64.b64encode(base64.b64encode(dumped.encode())).decode()
  with open("encrypted.txt","w") as file:
    file.write(encoded+"."+hashlib.sha256(encoded.encode()).hexdigest().upper())
  


