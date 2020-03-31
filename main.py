import requests
import lxml
from bs4 import BeautifulSoup
import discord
import os

token = os.environ.get("S3_KEY")
webpage = "https://www.worldometers.info/coronavirus/"

# ------------- start data gathering ---------------------- #
def DataGather():
    data = []

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

    coronaUpdate = soup.find("div", {"class": "content-inner"})
    update = coronaUpdate.findAll("div")[1].getText()
    data.append(update)

    print(update)
    return data

# ------------- end data gathering ---------------------- #

client = discord.Client()

@client.event
async def on_message(message):
    data = DataGather()

    if message.content == "-corona news" or message.content == "-covid19 news" or message.content == "-sars cov2 news":
        embed = discord.Embed(title="Corona News", color=0x00ff00)
        embed.add_field(name="Smittede", value=data[0] + "er infekterede.", inline=False)
        embed.add_field(name="Døde", value=data[1] + " er døde.", inline=False)
        embed.add_field(name="Raske", value=data[2] + " er raske igen.", inline=False)
        embed.add_field(name="Update", value=data[3], inline=False)
        embed.set_footer(text=webpage)
        await message.channel.send(embed=embed)


client.run(token)