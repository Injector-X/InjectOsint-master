import os, requests
from source import internet_connection
from huepy import *
from time import sleep

def banner():
    
    print(bold(orange("""
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
    
    
def dox_menu():
    os.system('cls') if os.name == 'nt' else os.system('clear')
    banner()
    sleep(1)

    print(green('   [' + white('1' + green('] ' + lightgreen("Nickname research.\n")))))
    sleep(0.7)
    print(green('   [' + white('2' + green('] ' + lightgreen("Validate email.\n")))))
    sleep(0.7)
    print(green('   [' + white('3' + green('] ' + lightgreen("Geolocate by IP.\n")))))
    sleep(0.7)
    print(green('   [' + white('4' + green('] ' + lightgreen("Go back.\n")))))
    sleep(0.7)
    case = input(lightgreen("            [" + white('?' + lightgreen('] '))))
    
    if case == '1':
        import source.assets_dox.sherlock
        
    if case == '2':
        import source.assets_dox.email_validate
        
    if case == '3':
        import source.assets_dox.ip_tracker

    if case == '4':
        main_menu()


if __name__ == '__main__':
    
    
    os.system('cls') if os.name == 'nt' else os.system('clear')
    print(green('[' + white('*' + green('] ' + lightgreen("Loading payloads...")))))
    sleep(0.7)
    print(green('[' + white('*' + green('] ' + lightgreen("Loading Scripts...")))))
    sleep(1)
    os.system('cls') if os.name == 'nt' else os.system('clear')
    banner()
    sleep(1)

    print(green('   [' + white('1' + green('] ' + lightgreen("Dox personal.\n")))))
    sleep(0.7)
    print(green('   [' + white('2' + green('] ' + lightgreen("Dox web.\n")))))
    sleep(0.7)
    print(green('   [' + white('3' + green('] ' + lightgreen("Exit.\n")))))
    sleep(0.7)
    case = input(lightgreen("            [" + white('?' + lightgreen('] '))))
    
    if case == '1':
        dox_menu()

    if case == '2':
        os.system('cls') if os.name == 'nt' else os.system('clear')
        import source.assets_web.doxweb
    
    
    
else:
    print(red("</Hacking Productions>"))