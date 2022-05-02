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

list_of_vechicles = ["All vechicle", "Tanks", "Armoured Fighting Vehicles", "Infantry Fighting Vehicles", "Armoured Personnel Carriers", "Mine-Resistant Ambush Protected",
                    "Infantry Mobility Vehicles", "Command Posts And Communications Stations", "Engineering Vehicles And Equipment", "Heavy Mortars",  "Towed Artillery",
                    "Self-Propelled Artillery", "Multiple Rocket Launchers", "Anti-Aircraft Guns", "Self-Propelled Anti-Aircraft Guns", "Surface-To-Air Missile Systems",
                    "Radars", "Jammers And Deception Systems ", "Aircraft", "Helicopters", "Unmanned Aerial Vehicles", "Naval Ships", "Logistics Trains", 
                    "Trucks, Vehicles and Jeeps"]

def all_losses_amount():
    _ = []
    all_losses_list = []
    req = requests.get(url, headers = headers).text
    soup = BeautifulSoup(req, "lxml")
    all_losses = soup.find("h3").find("span").text
    vechicles_losses = soup.find_all("h3")
    
    for vechicle in vechicles_losses:
        vechicle = vechicle.text.replace('\n', '')
        _.append(vechicle)
    all_losses_list= list(filter(None, _))
    # print(all_losses_list)
    return all_losses_list
    # print(all_losses_list)
    # for item in all_losses_list:
def printer(all_losses_list):
    _ = []
    try:
        for item in all_losses_list[0:6]:
            x = re.findall('\d+', item)
            b = {
                "All_losses":x[0],
                "Destroyed":x[1],
                "Damaged":x[2],
                "Abandoned":x[3],
                "Captured":x[4]}
            _.append(b)
        
        for i in range(0, len(all_losses_list)):
            y = {
                f"{list_of_vechicles[i]}":_[i]
            }
            print(y)
    # all_list.append([_])
    # for strings in _:
    #     all_list_losses.append([strings])
    # print(all_list_losses)
    # print(all_losses_list[1])
    # tanks_losses = soup.find_previous("span", class_="mw-headline")
    # x = re.findall('\d+', all_losses)
    # all_losses_dict = {
        # "All_losses":x[0],
        # "Destroyed":x[1],
        # "Damaged":x[2],
        # "Abandoned":x[3],
        # "Captured":x[4]
    # }
    
    
    # print(tanks_losses)



if __name__ == "__main__":
    all_losses_list = all_losses_amount()
    printer(all_losses_list)