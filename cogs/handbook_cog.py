import discord
from discord.ext import commands

class Handbook(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.handbook = ("help -> handbook\n"
                "random daily -> wählt eine zufällige aufgabe aus IMC und IMO")

    def build_embed(self):
        embed = discord.Embed(
            title="Handbook",
            description="Der bot featured folgende commands:",
            color=discord.Color.purple()
        )
        embed.add_field(
            name="help",
            value="zeigt dieses Handbook",
            inline=False)
        embed.add_field(
            name="random daily",
            value="wählt eine zufällige Aufgabe aus IMC und IMO",
            inline=False,
        )
        embed.add_field(
            name="list [Endung]",
            value="zeigt die gespeicherten Wörter mir der entsprechenden Endunge an",
            inline=False
        )
        return embed

    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.author.bot:
            return

        if msg.content.lower() == "help":
            await msg.channel.send(embed=self.build_embed())


def setup(bot):
    bot.add_cog(Handbook(bot))