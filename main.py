import discord
import os
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = discord.Bot(intents=intents)

bot.load_extension("cogs.moderation_cog")
bot.load_extension("cogs.random_daily_task_cog")
bot.load_extension("cogs.handbook_cog")
bot.load_extension("cogs.woerter_mit_endungen_tracker_cog")
bot.load_extension("cogs.music_helper_cog")
bot.load_extension("cogs.wordle_cog")
bot.load_extension("cogs.test_cog")

bot.run(BOT_TOKEN)