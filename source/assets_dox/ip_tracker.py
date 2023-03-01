"""               IP TRACKER Tool made by @ByDog3r 
                            V.1.0.0                              """

import os, requests, json, sys
from time import sleep
from huepy import *

def banner():

    print(bold(lightred("""
 ██▓ ███▄    █  ▄▄▄██▀▀▀▓█████  ▄████▄  ▄▄▄█████▓ ▒█████    ██████  ██▓ ███▄    █ ▄▄▄█████▓
▓██▒ ██ ▀█   █    ▒██   ▓█   ▀ ▒██▀ ▀█  ▓  ██▒ ▓▒▒██▒  ██▒▒██    ▒ ▓██▒ ██ ▀█   █ ▓  ██▒ ▓▒
▒██▒▓██  ▀█ ██▒   ░██   ▒███   ▒▓█    ▄ ▒ ▓██░ ▒░▒██░  ██▒░ ▓██▄   ▒██▒▓██  ▀█ ██▒▒ ▓██░ ▒░
░██░▓██▒  ▐▌██▒▓██▄██▓  ▒▓█  ▄ ▒▓▓▄ ▄██▒░ ▓██▓ ░ ▒██   ██░  ▒   ██▒░██░▓██▒  ▐▌██▒░ ▓██▓ ░ 
░██░▒██░   ▓██░ ▓███▒   ░▒████▒▒ ▓███▀ ░  ▒██▒ ░ ░ ████▓▒░▒██████▒▒░██░▒██░   ▓██░  ▒██▒ ░ 
░▓  ░ ▒░   ▒ ▒  ▒▓▒▒░   ░░ ▒░ ░░ ░▒ ▒  ░  ▒ ░░   ░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░░▓  ░ ▒░   ▒ ▒   ▒ ░░   
 ▒ ░░ ░░   ░ ▒░ ▒ ░▒░    ░ ░  ░  ░  ▒       ░      ░ ▒ ▒░ ░ ░▒  ░ ░ ▒ ░░ ░░   ░ ▒░    ░    
 ▒ ░   ░   ░ ░  ░ ░ ░      ░   ░          ░      ░ ░ ░ ▒  ░  ░  ░   ▒ ░   ░   ░ ░   ░      
 ░           ░  ░   ░      ░  ░░ ░                   ░ ░        ░   ░           ░   
             ░                                                        ░                 \n""")))

API = "http://ip-api.com/json/"

if __name__ == "__main__":
    pass

else:

    os.system('cls') if os.name == 'nt' else os.system('clear')
    banner()

    IP = input(green("[" + white("+" + green("]" + (lightgreen(" Ingrese una IP: ")))))).strip()

    os.system('cls') if os.name == 'nt' else os.system('clear')
    banner()

    try:
        
        data = requests.get(API+IP).json()
        sys.stdout.flush()

        print(yellow("    Dirección IP      " + cyan(" :      " + lightgreen(IP))))
        sleep(0.6)
        print(yellow("    Ciudad            " + cyan(" :      " + lightgreen(data['city']))))
        sleep(0.6)
        print(yellow("    Región            " + cyan(" :      " + lightgreen(data['region']))))
        sleep(0.6)
        print(yellow("    País              " + cyan(" :      " + lightgreen(data['country'] + "\n"))))
        sleep(0.6)
        print(yellow("    Latitud           " + cyan(" :      " + lightgreen(data['lat']))))
        sleep(0.6)
        print(yellow("    Longitud          " + cyan(" :      " + lightgreen(data['lon']))))
        sleep(0.6)
        print(yellow("    Zona Horaria      " + cyan(" :      " + lightgreen(data['timezone']))))
        sleep(0.6)
        print(yellow("    Código de país    " + cyan(" :      " + lightgreen(data['countryCode']))))
        sleep(0.6)
        print(yellow("    Código Postal     " + cyan(" :      " + lightgreen(data['zip'] + "\n"))))
        sleep(0.6)
        print(yellow("    ISP               " + cyan(" :      " + lightgreen(data['isp']))))
        sleep(0.6)
        print(yellow("    ASN               " + cyan(" :      " + lightgreen(data['as'] + "\n"))))
        sleep(0.6)
        print(yellow("    Google Maps       " + cyan(" :      " + lightblue("https://maps.google.com/?q="+ str(data['lat']) + "," + str(data['lon']) + "\n"))))

    except:
        pass