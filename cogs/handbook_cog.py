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
            description="This bot features the following commands:",
            color=discord.Color.purple()
        )
        embed.add_field(
            name="/handbook",
            value="shows this handbook",
            inline=False)
        embed.add_field(
            name="/random_daily",
            value="chooses a random IMC or IMO problem",
            inline=False,
        )
        embed.add_field(
            name="/list [Endung]",
            value="shows all saved german words ending in 'Endung'",
            inline=False
        )
        embed.add_field(
            name="/madeline",
            value="sends a Madeline sticker chosen by the user",
            inline=False
        )
        embed.add_field(
            name="/badeline",
            value="sends a Badeline sticker chosen by the user",
            inline=False
        )
        embed.add_field(
            name="/celeste_quotes",
            value="sends a quote from celeste, the best game ever made, chosen by the user",
            inline=False
        )
        return embed

    @discord.slash_command(
        name = "handbook",
        description = "Shows handbook"
    )
    async def handbook(self,ctx):
        if ctx.author.bot:
            return
        await ctx.respond(embed=self.build_embed())




def setup(bot):
    bot.add_cog(Handbook(bot))