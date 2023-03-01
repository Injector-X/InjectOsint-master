import requests, os
from huepy import *

if __name__ == "__main__":
    print("NO ALLOW")

else:
    try:
        requests.get("https://motherfuckingwebsite.com/")

    except:
        print(bad("NO INTERNET CONNECTION."))
        exit()