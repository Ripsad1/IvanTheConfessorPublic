import discord
from discord.ext import commands

class Test(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # Slash command mit Auswahl
    @discord.slash_command(
        name = "test", # Der Name darf kein Leerzeichen haben
        description = "test"
    )
    async def test(self,
                   ctx:discord.ApplicationContext,
                   auswahl:discord.Option(
                       str,
                       "Wähle",
                       choices=["123", "456", "789"]
                   )):
        await ctx.respond(f"Test {auswahl}")

def setup(bot):
    bot.add_cog(Test(bot))