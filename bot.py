import discord
import random, os
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
@bot.command()
async def hello(ctx):
    await ctx.send(f'Hello {bot.user}! I am a bot!')
@bot.command()
async def mem(ctx):
    with open('images/mem1.png', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def memrand(ctx):
    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:
        picture = discord.File(f)
 
    await ctx.send(file=picture)

@bot.command()
async def recycle(ctx):
    recylist =["gazetenin tahmini ayrışma süresi 1-6 haftadır", "kartonun tahmini ayrışma süresi 2 aydır", "plastik poşetin tahmini ayrışma süresi 10-20 yıldır", "cam şişenin tahmini ayrışma süresi 1 milyon yıldır", "alüminyum kutunun tahmini ayrışma süresi 200-500 yıldır", "metal kutunun tahmini ayrışma süresi 50 yıldır", "plastik şişenin tahmini ayrışma süresi 450 yıldır", "plastik pipetin tahmini ayrışma süresi 200 yıldır", "plastik çatal bıçağın tahmini ayrışma süresi 100 yıldır", "plastik poşetin tahmini ayrışma süresi 10-20 yıldır","uzay mekiği atıkları yaklaşık 1 milyon yıldır", "sigara izmaritinin tahmini ayrışma süresi 1-5 yıldır", "plastik pipetin tahmini ayrışma süresi 200 yıldır", "plastik çatal bıçağın tahmini ayrışma süresi 100 yıldır", "plastik poşetin tahmini ayrışma süresi 10-20 yıldır","uzay mekiği atıkları yaklaşık 1 milyon yıldır", "sigara izmaritinin tahmini ayrışma süresi 1-5 yıldır"]
    randrecy = random.choice(recylist)
    await ctx.send(randrecy)
bot.run("TOKEN") 


