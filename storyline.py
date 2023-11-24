
from colorama import Fore,Style
story = {
  "path":"ch1", #What part of the story the player starts on. Can be edited for development purposes.
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
        "text":"It's a flipped over phone, the screen is still on. Look at the screen? [yes/yes]",
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
      "help_threshold": 4,
      "help_text":"go inside.",
      "actions":{"look around":"Stop screwing around out here. You need to go inside."},
      "first_entry_text":"It's pouring down outside as you swipe your hastily-copied keycard along the keycard reader.\nIt thinks for a second, then silently opens the silver door beside it, revealing a darkened room inside.",
      "text":"It's still pouring down outside.",
      "go inside":{
        "first_entry":True,
        "first_entry_text":"As you hurry inside, the motion sensitive lights inside flicker on.\nYou see the guard checkpoint ahead, and you pray that he doesn't know you were fired a few hours ago.\nAs you approach the guarded checkpoint, you slow down from the breakneck run that you didn't quite realize you were doing.\nYou walk up to the solid plexiglass separating you from the guard.\n\nDIALOGUE OPTIONS:\n[make small talk]\n[kill him]\n[stay silent]",
        "text":"You walk up to the solid plexiglass separating you from the guard.\n\nDIALOGUE OPTIONS:\n[make small talk]\n[kill him]\n[stay silent]\n[seduce him]",
        "stay silent":{
          "auto":"wondering",
          "text":"You decide that you'll stay silent no matter what he says.\n\n'Well hey there! How ya doin today?'\n...\n...\n...\n'Nothin huh? Well, I need to see your- oh, you've been precleared! Great, go on through.'",
          "wondering":{
            "clear":"ch1-ch1_02",
            "ending_1":1,
            "text":Fore.LIGHTBLUE_EX+"Precleared huh? That was a stroke of luck. What were you thinking, staying silent? You should've been executed on the spot. Fortune favors the idiotic apparently..."+Style.RESET_ALL
          }
        },
        "kill him":{
          "game_over":0,
          "text":"You're overcome with a murderous rage as you realize that this was the man that slept with your wife!\nYou draw your weapon, and try to shoot him through the glass. The glass almost seems to give way for a second, but it merely cracks.\nAs your mind scrambles, trying to figure out what to do next, the guard presses a button on his desk.\nTwo automated sentry bots drop down from the ceiling, and summarily execute you."
        },
        "make small talk":{
          "clear":"ch1-ch1_02",
          "ending_2":1,
          "text":"You recognize the security guard. It's Jeff, that one guy who you got donuts for because he saved your hide that one time.\nYou're not the best of friends, but hopefully you can smooth talk your way through.\n\n'Hey Big Tim, how's it smoking?'\n\n'What?'\n\n'Nothing, inside joke. Listen, can you let me in?'\n...\n...\n...\n'Yeah sure, whatever.'"
        },
        "seduce him":{
          "clear":"ch1-ch1_02",
          "ending_3":1,
          "text":"You decide that you'll try and seduce that big man. You press yourself awkwardly against the glass, thinking you look good. You don't, but A+ for confidence.\nThe public radio plays romantic saxophone, while you make vulgar facial expressions at the guard. He seems disgusted, yet intrigued.\nYou try your best to look like the most distressed damsel with doe eyes piercing his skin. 'OH! If only an unnamed man with big strong arms would save the day for me!' you cry.\nYou think about all the nights you will be sobbing, cringing at yourself. The man who wasn't particularly attractive opens the door and lets you inside.\nHe gives you a piece of paper with a phone number and told you to call him.\n\nYou eat the paper out of spite. "
        }
      }
    },
    "ch1_02":{
      "go_back_not_allowed":0,
      "inventory":{"screwdriver":{"description":"An old screwdriver, it's missing chunks of plastic from the handle."},"box":{}},
      "text":"As the door slides shut behind you, you walk into a small room. There's a door ahead, and cardboard boxes scattered around.",
      "actions":{"look around":"You glance around the room, searching for something that might help you. There! There's a screwdriver on top of a box. Try taking it. You might be able to open the door with it."},
      "open door":{
        "go_back_not_allowed":0,
        "required_item":"screwdriver",
        "text":"You consider the panel for a second, before absolutely stabbing the crap out of it with the screwdriver.\nThe door grinds halfway open, then stops.\nOPTIONS:\n[squeeze through]\n[ask it politely to open]\n[brute force it open]",
        "squeeze through":{
          "clear":"ch1-ch1_03",
          "ending_2":1,#Pragmatic approach
          "text":"You suck in your stomach, and try not to think about the possibility of being cut in half.\nYou start to slowly squeeze through, and halfway through you get stuck.\nAfter what seems like an eternity, you barely manage to make it to the other side, panting and gasping.",
        },
        "ask it politely to open":{
          "auto":"narrator_opening",
          "ending_1":1,#Idiotic approach
          "text":"You straighten up, throw a mint in your mouth, and put on your best charming smile.\n\n'Hey there, I don't wanna inconvenience you, but could you possibly open the door for me?'\nYou get the sense of the door blushing as well as a door can blush.\nThe door quickly slides all the way open, and you saunter on through.",
          "narrator_opening":{
            "clear":"ch1-ch1_03",
            "text":Fore.LIGHTBLUE_EX+"You... asked it politely? IN WHAT SCREWED UP WORLD DOES THAT WORK?!?"
          }
        },
        "brute force it open":{
          "clear":"ch1-ch1_03",
          "ending_3":1,#Misc approach/big man approach
          "text":"You crack your knuckles, snort a scoop of pre-workout, and wrap some tape around your hands.\nThe door seems to shake in fear as you loom over it, preparing to absolutely rip it open.\nAs you're doing some jumping jacks and pushups to warm up, the door is positively trembling in fear now, and it shakes itself open before you can tear it open.",
        }
        
      }
    },
    "ch1_03":{
      "go_back_not_allowed":0,
      "text":""
    },
    "ch2_01":{
      
    }
  }
}
"""Guide to editing the story:
Each dictionary is a "room". Specifications:
Required-"text": provides the text the user recieves when entering the room
"go_back_not_allowed": whether or not you can go back from that room.
"inventory: provides items that can be taken from that room, which are dictionaries.
"required_item": tag that only allows the player into the room if they have the item
"remove_item": tag that removes the specified item from the players inventory
"first_entry": tag that indicates whether or not this is the players first time entering this room.
"first_entry_text": if the player enters while first_entry is true, print first_entry_text instead of the regular text.
"actions": Actions the player can take that won't take them out of their current room.
"auto": Tag that indicates whether or not the room will automatically proceed to the next, and what the next room is named.
"clear": Clears the path and sets the path to whatever the value of clear is.
"header": Whether or not to use rem_print on the text. Only checked for if "clear" or "auto" is also a tag.
"game_over": Ends the game.
"help_threshold": How many times an invalid command can be entered before the game offers help
"help_text": Text that will be displayed if help is accepted.
"""



