import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Bot setup
intents = discord.Intents.default()
intents.members = True  # Required for member join events
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Load cogs
async def load_cogs():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')
            print(f'Loaded cog: {filename}')

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    print(f'Bot is in {len(bot.guilds)} guild(s)')

async def main():
    async with bot:
        await load_cogs()
        await bot.start(os.getenv('DISCORD_TOKEN'))

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
