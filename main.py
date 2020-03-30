import requests
import lxml
from bs4 import BeautifulSoup
import discord

# from details import token

from boto.s3.connection import S3Connection
s3 = S3Connection(os.environ['S3_KEY'], os.environ['S3_SECRET'])

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

client = discord.Client()

@client.event
async def on_message(message):

    # id = client.get_guild(idclient)
    if message.content == "-corona news":
        embed = discord.Embed(title="Corona News", color=0x00ff00)
        embed.add_field(name="Smittede", value=data[0] + "er infekterede.", inline=False)
        embed.add_field(name="Døde", value=data[1] + " er døde.", inline=False)
        embed.add_field(name="Raske", value=data[2] + " er raske igen.", inline=False)
        embed.add_field(name="Source", value=webpage, inline=False)
        await message.channel.send(embed=embed)
 
    if message.content == "-covid19 news":
        embed = discord.Embed(title="Corona News", color=0x00ff00)
        embed.add_field(name="Smittede", value=data[0] + "er infekterede.", inline=False)
        embed.add_field(name="Døde", value=data[1] + " er døde.", inline=False)
        embed.add_field(name="Raske", value=data[2] + " er raske igen.", inline=False)
        embed.add_field(name="Source", value=webpage, inline=False)
        await message.channel.send(embed=embed)

    if message.content == "-sars cov2 news":
        embed = discord.Embed(title="Corona News", color=0x00ff00)
        embed.add_field(name="Smittede", value=data[0] + "er infekterede.", inline=False)
        embed.add_field(name="Døde", value=data[1] + " er døde.", inline=False)
        embed.add_field(name="Raske", value=data[2] + " er raske igen.", inline=False)
        embed.add_field(name="Source", value=webpage, inline=False)
        await message.channel.send(embed=embed)


    
    # join channel first

    # if message.content == "adhd":
    #     await message.channel.send("-play corona adhd")



client.run(s3)