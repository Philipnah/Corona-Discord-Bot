import requests
import lxml
from bs4 import BeautifulSoup
import discord
#from token import token

# ------------- start data gathering ---------------------- #
data = []

webpage = "https://www.worldometers.info/coronavirus/"
datapage = requests.get(webpage)

soup = BeautifulSoup(datapage.text, "lxml")

coronaData = soup.find_all(class_="maincounter-number")

def splicer():
     n = 0
     while n <= 2:
          coronaCases = str(coronaData[n]).split(">")
          coronaCases = coronaCases[2].split("<")
          coronaCases = coronaCases[0].replace(",", ".")

          data.append(coronaCases)
          n += 1


splicer()

print(data)

# ------------- end data gathering ---------------------- #