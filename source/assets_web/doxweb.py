"""         HackerTargetPy Made By: @ByDog3r
                         V.1.0.0               """

import os, requests, json, sys
from huepy import *
from time import sleep

def banner():

    print(bold(lightblue("""
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

YOURAPIKEY = "EXAMPLE OF YOUR API KEY"

class HackerTargetPy():

    def __init__(self, URL, message):
        self.API = URL
        self.message = message


    def RunApi(self):

        os.system('cls') if os.name == 'nt' else os.system('clear')
        banner()
        print(good(white(self.message)))
        
        self.target = input((info(white("Target: "))))
        self.webdox = self.API+self.target+"&apikey="+YOURAPIKEY
        print(requests.get(self.webdox).text)

HACKER_API = ["https://api.hackertarget.com/mtr/?q=",
            "https://api.hackertarget.com/nping/?q=",
            "https://api.hackertarget.com/dnslookup/?q=",
            "https://api.hackertarget.com/reversedns/?q=",
            "https://api.hackertarget.com/hostsearch/?q=",
            "https://api.hackertarget.com/findshareddns/?q=",
            "https://api.hackertarget.com/zonetransfer/?q=",
            "https://api.hackertarget.com/whois/?q=",
            "https://api.hackertarget.com/geoip/?q=",
            "https://api.hackertarget.com/reverseiplookup/?q=",
            "https://api.hackertarget.com/nmap/?q=",
            "https://api.hackertarget.com/subnetcalc/?q=",
            "https://api.hackertarget.com/httpheaders/?q=",
            "https://api.hackertarget.com/pagelinks/?q="]

def run():
    banner()
    print(green("\t\t\t["+white("1"+green("]  Traceroute."+green("\t["+white("2"+green("]  Ping Test.\n")))))))
    print(green("\t\t\t["+white("3"+green("]  DNS Lookup."+green("\t["+white("4"+green("]  Reverse DNS\n")))))))
    print(green("\t\t\t["+white("5"+green("]  Find DNS Host."+green("\t["+white("6"+green("]  Find Shared DNS.\n")))))))
    print(green("\t\t\t["+white("7"+green("]  Zone Transfer."+green("\t["+white("8"+green("]  Whois Lookup.\n")))))))
    print(green("\t\t\t["+white("9"+green("]  IP Location Lookup."+green("["+white("10"+green("] Reverse IP Lookup.\n")))))))
    print(green("\t\t\t["+white("11"+green("] TCP Port Scan."+green("\t["+white("12"+green("] Subnet Lookup.\n")))))))
    print(green("\t\t\t["+white("13"+green("] HTTP Header Check."+green("\t["+white("14"+green("] Extract Page Links.\n")))))))
    print(green("\t\t\t["+white("15"+green("] Version."+green("\t\t["+white("16"+green("] Exit\n")))))))

    try:

        dox = input(white("\n\tWich Option Number: "))

        if dox == '1':
            HackerTargetPy(HACKER_API[0], "Traceroute script running..").RunApi()

        elif dox == '2':
            HackerTargetPy(HACKER_API[1], "Ping Test script running..").RunApi()

        elif dox == '3':
            HackerTargetPy(HACKER_API[1], "DNS Lookup script running..").RunApi()

        elif dox == '4':
            HackerTargetPy(HACKER_API[1], "Reverse DNS script running..").RunApi()

        elif dox == '5':
            HackerTargetPy(HACKER_API[1], "Find DNS Host script running..").RunApi()

        elif dox == '6':
            HackerTargetPy(HACKER_API[1], "Find Shared DNS script running..").RunApi()

        elif dox == '7':
            HackerTargetPy(HACKER_API[1], "Zone Transfer script running..").RunApi()

        elif dox == '8':
            HackerTargetPy(HACKER_API[1], "Whois Lookup script running..").RunApi()

        elif dox == '9':
            HackerTargetPy(HACKER_API[1], "IP Location Lookup script running..").RunApi()

        elif dox == '10':
            HackerTargetPy(HACKER_API[1], "Reverse IP Lookup script running..").RunApi()

        elif dox == '11':
            HackerTargetPy(HACKER_API[1], "TCP Port Scan script running..").RunApi()

        elif dox == '12':
            HackerTargetPy(HACKER_API[1], "Subnet Lookup script running..").RunApi()
    

        elif dox == '13':
            HackerTargetPy(HACKER_API[1], "HTTP Header Check script running..").RunApi()

        elif dox == '14':
            HackerTargetPy(HACKER_API[1], "Extract Page Links script running..").RunApi()

        elif dox == '15':
            print("\t"+good(white("Version Checking..")))
            version_number = "1.0.5"
            sleep(3)
            print("\t"+good(white("Version : "+yellow(version_number))))

        elif dox == '16':
            exit()

    except:
        pass


if __name__ == '__main__':
  pass
else:
  run()