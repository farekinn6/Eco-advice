import discord
import os
import random
from discord.ext import commands


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)


@bot.command()
async def ecoadvice(ctx):
    images = os.listdir('images')
    image_files = ['images/eco-2(4).jpg','images/otkhody.webp','images/globalwarming.png']
    random_image = random.choice(image_files)
    with open(random_image, 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)


@bot.command()
async def animals(ctx):
    images = os.listdir('images')
    image_files = ['images/panda.jpeg','images/parrot.jpeg','images/wolf.jpeg']
    random_image = random.choice(image_files)
    with open(random_image, 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def mem(ctx):
    images = os.listdir('images')
    image_files = ['images/mem1.jpg','images/mem2.jpg','images/mem3.jpg']
    random_image = random.choice(image_files)
    with open(random_image, 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)



