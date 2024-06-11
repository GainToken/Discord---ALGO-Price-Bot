import discord
from discord.ext import tasks, commands
import requests
import os
import asyncio

#Define the intents
intents = discord.Intents.default()
intents.presences = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents) #Pass intents parameter

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    update_price.start() #Start price update task when bot is ready

@tasks.loop(seconds=60) #Update every 60 seconds
async def update_price():
    token_id = "algorand" #Example: Algorand token ID
    price = get_token_price(token_id)
    price_formatted = f"${price:.3f}"  #Format price to 3 decimal places with "$" sign
    try:
        for guild in bot.guilds:
            await guild.me.edit(nick=price_formatted) #Update bot's nickname in each guild
        await bot.change_presence(activity=discord.Activity(name="ALGO Price", type=discord.ActivityType.watching)) #Update bot's activity
    except discord.errors.HTTPException as e:
        if e.status == 429:
            retry_after = e.response.headers.get('Retry-After', 5)
            await asyncio.sleep(int(retry_after))
            for guild in bot.guilds:
                await guild.me.edit(nick=price_formatted)
            await bot.change_presence(activity=discord.Activity(name="ALGO Price Bot", type=discord.ActivityType.watching))
        else:
            raise e

def get_token_price(token_id):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={token_id}&vs_currencies=usd"
    response = requests.get(url)
    data = response.json()
    return data[token_id]["usd"]

#Use environment variable for bot token
bot.run(os.getenv("TOKEN") or "INSERT DISCORD BOT TOKEN HERE")