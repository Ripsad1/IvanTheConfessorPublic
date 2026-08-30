import discord
from discord.ext import commands
from helper.dict_saver_and_loader import load_dict, save_dict
from helper.endungen_list_builder import create_list_endung

class WoerterMitEndungen(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Automatisch neue Wörter in Liste hinzufügen
    @commands.Cog.listener("on_message")
    async def track_woerter(self, msg):

        if msg.author.bot:
            return

        WOERTER_FILE = "woerter_mit_endungen.json"
        woerter_dict = load_dict(WOERTER_FILE)

        content = msg.content.lower()

        for word in content.split():
            word = word.strip(".,!?")
            for end in ["al", "ast", "ut", "est", "icht", "ang"]:
                if word.endswith(end):
                    endung = "-" + end
                    if word not in woerter_dict[endung]:
                        await msg.channel.send("Woah! Das ist neu. Genial!")
                        woerter_dict[endung].append(word)
            # spezielle Schreibweisen separat behandelt
            endung = None
            if word.endswith("ahl"):
                endung = "-al"
            elif word.endswith("asst"):
                endung = "-ast"
            if endung is not None:
                if word not in woerter_dict[endung]:
                    await msg.channel.send("Woah! Das ist neu. Genial!")
                    woerter_dict[endung].append(word)

        save_dict(WOERTER_FILE, woerter_dict)

    # Listen anzeigen
    @commands.Cog.listener("on_message")
    async def zeige_liste(self, msg):

        if msg.author.bot:
            return

        WOERTER_FILE = "woerter_mit_endungen.json"
        woerter_dict = load_dict(WOERTER_FILE)

        if msg.content.startswith("list "):
            teile = msg.content.split(maxsplit=1)
            endung = "-" + teile[1].strip().lstrip("-").lower() if len(teile) > 1 else "-"
            await msg.channel.send(embed=create_list_endung(endung))





def setup(bot):
    bot.add_cog(WoerterMitEndungen(bot))