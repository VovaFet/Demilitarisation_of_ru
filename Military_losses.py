import requests
from bs4 import BeautifulSoup
from time import sleep
import time
# from os import system
# import json
from user_agent import generate_user_agent
import re

headers = {
    "User-Agent": generate_user_agent()
}
url = 'https://www.oryxspioenkop.com/2022/02/attack-on-europe-documenting-equipment.html'

def all_losses_amount():
    req = requests.get(url, headers = headers).text
    soup = BeautifulSoup(req, "lxml")
    all_losses = soup.find("h3").find("span").text
    x = re.findall('\d+', all_losses)
    all_losses_dict = {
        "All losses":x[0],
        "Destroyed":x[1],
        "Damaged":x[2],
        "Abandoned":x[3],
        "Captured":x[4]
    }
    # y = re.split('\d+', all_losses)
    # all_losses_list = [x]
    # x = re.findall('\d', x)
    # all_losses_list.append(re.split('\D+', all_losses))
    print(all_losses_dict)

















if __name__ == "__main__":
    all_losses_amount()