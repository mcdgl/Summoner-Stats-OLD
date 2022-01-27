import discord
import requests
from bs4 import BeautifulSoup #webscraping library
import os
import webbrowser
from discord.ext import commands
my_secret = os.environ['token']
client = commands.Bot(command_prefix = "!")

@client.command()
async def opgg(ctx, region=None, sumName=None):
  if(region == None or sumName == None):
    await ctx.send(f'Invalid input; Enter as follows: "!opgg [region] [summoner name]" and try again')
  elif(len(region) > 3):
    await ctx.send(f'Invalid input; Enter as follows: "!opgg [region] [summoner name]" and try again')
  else:
    try:
      await ctx.send(f'Region: {region.upper()}')
      await ctx.send(f'Summoner name: {sumName}')
      if(region.upper() == "KR"):
        region = "www"
      search = (f'https://{region.lower()}.op.gg/summoner/userName={sumName}')
      page = requests.get(search, headers={'User-Agent': 'Mozilla/5.0'}).text
      #print(page) debug
      soup = BeautifulSoup(page, "html.parser")
      rank = soup.find("div", class_="TierRank").text
      rank = rank.rstrip()
      summLP = soup.select_one("span[class*=LeaguePoints]").text
      summLP = summLP.strip()
      
      await ctx.send(f'{sumName} is {rank}, {summLP}')
    except(Exception):
      await ctx.send(f'Summoner is either unranked or does not exist in this region.')

@client.event
async def on_ready():
  print("We have logged in as  {0.user}".format(client))





client.run(my_secret)
