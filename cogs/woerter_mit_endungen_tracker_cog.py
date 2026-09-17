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
    @discord.slash_command(
        name="list",
        description="shows all saved german words ending in 'Endung'"
    )
    async def list(self,
                   ctx:discord.ApplicationContext,
                   endung=discord.Option(
                       str,
                       "choose Endung",
                       choices=["al", "ast", "ut", "est", "icht", "ang"]
                   )
                   ):
        WOERTER_FILE = "woerter_mit_endungen.json"
        woerter_dict = load_dict(WOERTER_FILE)
        await ctx.respond(embed=create_list_endung("-"+endung))


def setup(bot):
    bot.add_cog(WoerterMitEndungen(bot))