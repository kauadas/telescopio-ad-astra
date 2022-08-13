import requests

from bs4 import BeautifulSoup

code = "f1a8344e01eba430b9871a6b16c603bc65fcee6923d6744054311604f78ba699"
link="https://weather.com/weather/today/l/"+code

temperature="CurrentConditions--tempValue--3a50n"

phrase="CurrentConditions--phraseValue--2Z18W"


def get_temp():
    page = requests.get(link)

    soup=BeautifulSoup(page.text,"html.parser")

    temp=soup.find_all(class_=temperature)[0]
    temp=temp.get_text()
    temp=temp.replace("°","")
    temp=int((int(temp)-30) * (5/9))
    return temp


def get_state():
    page = requests.get(link)

    soup=BeautifulSoup(page.text,"html.parser")

    state = soup.find_all(class_="CurrentConditions--phraseValue--2Z18W")[0]

    state = state.get_text()

    return state