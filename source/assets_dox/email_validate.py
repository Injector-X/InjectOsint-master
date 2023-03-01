"""               Email Validate Tool made by @ByDog3r 
                            V.1.0.0                              """

import os, requests, json, sys, random
from time import sleep
from huepy import *

def banner():

    print(bold(grey("""
 ██▓ ███▄    █  ▄▄▄██▀▀▀▓█████  ▄████▄  ▄▄▄█████▓ ▒█████    ██████  ██▓ ███▄    █ ▄▄▄█████▓
▓██▒ ██ ▀█   █    ▒██   ▓█   ▀ ▒██▀ ▀█  ▓  ██▒ ▓▒▒██▒  ██▒▒██    ▒ ▓██▒ ██ ▀█   █ ▓  ██▒ ▓▒
▒██▒▓██  ▀█ ██▒   ░██   ▒███   ▒▓█    ▄ ▒ ▓██░ ▒░▒██░  ██▒░ ▓██▄   ▒██▒▓██  ▀█ ██▒▒ ▓██░ ▒░
░██░▓██▒  ▐▌██▒▓██▄██▓  ▒▓█  ▄ ▒▓▓▄ ▄██▒░ ▓██▓ ░ ▒██   ██░  ▒   ██▒░██░▓██▒  ▐▌██▒░ ▓██▓ ░ 
░██░▒██░   ▓██░ ▓███▒   ░▒████▒▒ ▓███▀ ░  ▒██▒ ░ ░ ████▓▒░▒██████▒▒░██░▒██░   ▓██░  ▒██▒ ░ 
░▓  ░ ▒░   ▒ ▒  ▒▓▒▒░   ░░ ▒░ ░░ ░▒ ▒  ░  ▒ ░░   ░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░░▓  ░ ▒░   ▒ ▒   ▒ ░░   
 ▒ ░░ ░░   ░ ▒░ ▒ ░▒░    ░ ░  ░  ░  ▒       ░      ░ ▒ ▒░ ░ ░▒  ░ ░ ▒ ░░ ░░   ░ ▒░    ░    
 ▒ ░   ░   ░ ░  ░ ░ ░      ░   ░          ░      ░ ░ ░ ▒  ░  ░  ░   ▒ ░   ░   ░ ░   ░      
 ░           ░  ░   ░      ░  ░░ ░                   ░ ░        ░   ░           ░   
             ░                                                        ░                \n""")))




    
def keys():
            
    keys = []
                
    with open('source/assets_dox/keys.txt', 'r') as f:
                    
        series = [key.strip() for key in f]
                    
        for item in series:
                base_split = item.split('\n')
                keys.append(base_split[0])
                        
    return keys

if __name__ == '__main__':
    pass

else:

    key = random.choice(keys())
            
    os.system('cls') if os.name == 'nt' else os.system('clear')
    banner()

    email = input(yellow("  Ingrese un correo: ")).strip()

    API = "https://app.verify-email.org/api/v1/"+key+"/verify/"+email

    data = requests.get(API).json()
    sys.stdout.flush()

    os.system('cls') if os.name == 'nt' else os.system('clear')
    banner()
            
    try:

        if data['status_description'] == "OK email":
            print(yellow("  Email Valido " + cyan(" : " + lightgreen(email) + "\n")))

        else:
            print(yellow("  Email Invalido " + cyan(" : " + lightgreen(email) + "\n")))
                    
    except:
        print(bad('Ingrese correctamente su correo.'))

