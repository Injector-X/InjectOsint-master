"""               Sherlock Tool made by @ByDog3r 
                            V.1.0.0                              """

import requests, os
from huepy import *

def banner():

    print(bold(lightpurple("""
 ██▓ ███▄    █  ▄▄▄██▀▀▀▓█████  ▄████▄  ▄▄▄█████▓ ▒█████    ██████  ██▓ ███▄    █ ▄▄▄█████▓
▓██▒ ██ ▀█   █    ▒██   ▓█   ▀ ▒██▀ ▀█  ▓  ██▒ ▓▒▒██▒  ██▒▒██    ▒ ▓██▒ ██ ▀█   █ ▓  ██▒ ▓▒
▒██▒▓██  ▀█ ██▒   ░██   ▒███   ▒▓█    ▄ ▒ ▓██░ ▒░▒██░  ██▒░ ▓██▄   ▒██▒▓██  ▀█ ██▒▒ ▓██░ ▒░
░██░▓██▒  ▐▌██▒▓██▄██▓  ▒▓█  ▄ ▒▓▓▄ ▄██▒░ ▓██▓ ░ ▒██   ██░  ▒   ██▒░██░▓██▒  ▐▌██▒░ ▓██▓ ░ 
░██░▒██░   ▓██░ ▓███▒   ░▒████▒▒ ▓███▀ ░  ▒██▒ ░ ░ ████▓▒░▒██████▒▒░██░▒██░   ▓██░  ▒██▒ ░ 
░▓  ░ ▒░   ▒ ▒  ▒▓▒▒░   ░░ ▒░ ░░ ░▒ ▒  ░  ▒ ░░   ░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░░▓  ░ ▒░   ▒ ▒   ▒ ░░   
 ▒ ░░ ░░   ░ ▒░ ▒ ░▒░    ░ ░  ░  ░  ▒       ░      ░ ▒ ▒░ ░ ░▒  ░ ░ ▒ ░░ ░░   ░ ▒░    ░    
 ▒ ░   ░   ░ ░  ░ ░ ░      ░   ░          ░      ░ ░ ░ ▒  ░  ░  ░   ▒ ░   ░   ░ ░   ░      
 ░           ░  ░   ░      ░  ░░ ░                   ░ ░        ░   ░           ░   
             ░                                                        ░                                                         ░                \n""")))


class Sherlock():

    def __init__(self, url, user, company_name):

        self.url = url
        self.user = user
        self.company = company_name

    def whois(self):

        try:

            self.page = requests.get(self.url+self.user)

            if self.page.status_code == 200:
                print(green("[" + white("+" + green("] " + white(self.company + green(" Encontrado! " + white(self.url+self.user)))))))

            else:
                print(green("[" + red("-" + green("] " + white(self.company + yellow("No encontrado."))))))

        except:
            print(bad("Ha ocurrido un error!"))



if __name__ == "__main__":
    pass

else:

    os.system('cls') if os.name == 'nt' else os.system('clear')
    banner()

    user = input(green("[" + white("+" + green("]" + (lightgreen(" Ingrese un nickname: "))))))


    """                           APIS                                  """

    facebook, instagram, twitter = "https://facebook.com/", "https://instagram.com/", "https://twitter.com/"

    github, youtube, reddit = "https://www.github.com/", "https://www.youtube.com/", "https://www.reddit.com/user/"

    pinterest, tumblr, steam = "https://www.pinterest.com/", "https://"+user+".tumblr.com", "https://steamcommunity.com/id/"

    vimeo, soundcloud, vk = "https://vimeo.com/", "https://soundcloud.com/", "https://vk.com/"

    imgur, pastebin, roblox = "https://imgur.com/user/", "https://pastebin.com/u/", "https://www.roblox.com/user.aspx?username="

    whattpad, canva, wikipedia = "https://www.wattpad.com/user/", "https://www.canva.com/", "https://www.wikipedia.org/wiki/User:"

    hackernews, ebay, ps4 = "https://news.ycombinator.com/user?id=", "https://www.ebay.com/usr/", "https://my.playstation.com/profile/"

    colourlovers, codementor, aboutme = "https://www.colourlovers.com/love/", "https://www.codementor.io/", "https://about.me/"

    linkedin, twitch, spotify = "https://www.linkedin.com/in/", "https://www.twitch.tv/", "https://open.spotify.com/user/"
    
    rockstar, tiktok, tradingview = "https://socialclub.rockstargames.com/member/", "https://www.tiktok.com/@", "https://es.tradingview.com/u/"
    
    """                  FIN DE LAS APIS                              """
    

    Sherlock(facebook, user, "Facebook: ").whois()

    Sherlock(instagram, user, "Instagram: ").whois()

    Sherlock(twitter, user, "Twitter: ").whois()

    Sherlock(youtube, user, "YouTube: ").whois()

    Sherlock(github, user, "Github: ").whois()

    Sherlock(reddit, user, "Reddit: ").whois()

    Sherlock(pinterest, user, "Pinterest: ").whois()

    Sherlock(steam, user, "Steam: ").whois()

    Sherlock(vimeo, user, "Vimeo: ").whois()

    Sherlock(soundcloud, user, "SoundCloud: ").whois()

    Sherlock(vk, user, "VK: ").whois()

    Sherlock(imgur, user, "Imgur: ").whois()

    Sherlock(pastebin, user, "Pastebin: ").whois()

    Sherlock(roblox, user, "Roblox: ").whois()

    Sherlock(whattpad, user, "Wattpad: ").whois()
    
    Sherlock(canva, user, "Canva: ").whois()

    Sherlock(wikipedia, user, "Wikipedia: ").whois()

    Sherlock(hackernews, user, "HackerNews: ").whois()

    Sherlock(ebay, user, "Ebay: ").whois()

    Sherlock(ps4, user, "PlayStation: ").whois()

    Sherlock(colourlovers, user, "ColourLovers: ").whois()

    Sherlock(codementor, user, "CodeMentor: ").whois()

    Sherlock(aboutme, user, "AboutMe: ").whois()

    Sherlock(linkedin, user, "Linkedin: ").whois()

    Sherlock(twitch, user, "Twitch: ").whois()

    Sherlock(spotify, user, "Spotify: ").whois()

    Sherlock(rockstar, user, "Rockstar Games: ").whois()
    
    Sherlock(tiktok, user, "Tik Tok:").whois()

    Sherlock(tradingview, user, "TradingView: ").whois()