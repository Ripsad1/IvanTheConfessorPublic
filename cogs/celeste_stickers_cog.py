import discord
from discord.ext import commands

faces_madeline = {
    "neutral": "https://media.discordapp.net/attachments/1305175146281173034/1508928766376677506/image.png?ex=6a1752ec&is=6a16016c&hm=a85b06ed5e6b1e8892b2ba9b493f30331feee2fd181b69ae3ff23c3e354e58f5&=&format=webp&quality=lossless",
    "seriously": "https://media.discordapp.net/attachments/1305175146281173034/1508929045017133097/image.png?ex=6a17532e&is=6a1601ae&hm=25599cbb9cfcbd5b4044b78079a09588b85141bf2433869033337b5bc2bc195a&=&format=webp&quality=lossless",
    "disappointed": "https://media.discordapp.net/attachments/1305175146281173034/1508929124243214376/image.png?ex=6a175341&is=6a1601c1&hm=64985b1cecc89ac8b71b75f1437dfede93b695f1e3e338d8b5efc923dc685662&=&format=webp&quality=lossless",
    "angry": "https://media.discordapp.net/attachments/1305175146281173034/1508928937806532678/image.png?ex=6a175315&is=6a160195&hm=332a2402e5b52db798f4e0d14dcc27d196d58ab9f23745d9e6227f1443a83192&=&format=webp&quality=lossless",
    "hm": "https://media.discordapp.net/attachments/1305175146281173034/1508929254983733318/image.png?ex=6a175360&is=6a1601e0&hm=4bf82fcd050d4974b0232be670421f5e35605c4d416223cbc8f8a1d85befd95c&=&format=webp&quality=lossless",
    "closed eyes": "https://media.discordapp.net/attachments/1305175146281173034/1508929485507006464/image.png?ex=6a175397&is=6a160217&hm=e15b55629534fcecf0e4e2c6c893290db914c520d4f2a9bf4878a75d731db4fe&=&format=webp&quality=lossless",
    "happy": "https://media.discordapp.net/attachments/1305175146281173034/1508929580134568058/image.png?ex=6a1753ae&is=6a16022e&hm=af4bc47556b37fa67b16cac39de0679b5f4d465040ddde9f766144d26d99d1fe&=&format=webp&quality=lossless",
    "happy_o": "https://media.discordapp.net/attachments/1305175146281173034/1508929622283259964/image.png?ex=6a1753b8&is=6a160238&hm=f72dcd858a5e587b5783efc40e32b08c2ce7f6133a8c895390cc530b6f887382&=&format=webp&quality=lossless",
    "medium_happy": "https://media.discordapp.net/attachments/1305175146281173034/1508929673848029234/image.png?ex=6a1753c4&is=6a160244&hm=115f2bddee125db7f6bd81283853f916e201a625c14f46c198bfb466a93b7e5e&=&format=webp&quality=lossless",
    "ecchi": "https://media.discordapp.net/attachments/1305175146281173034/1508929727648239657/image.png?ex=6a1753d1&is=6a160251&hm=e6e74a273d2bfa7ca50fc37d06c48a371ca30ddaf650cdeee0a4902b80697c60&=&format=webp&quality=lossless",
    "fear": "https://media.discordapp.net/attachments/1305175146281173034/1508929842811502613/image.png?ex=6a1753ed&is=6a16026d&hm=f1bbcb78f6a892fbad931b4c99090bca4e811e32d9282916ab156e9e59aba3a4&=&format=webp&quality=lossless",
    "content": "https://cdn.discordapp.com/attachments/1305175146281173034/1508929937799774249/image.png?ex=6a175403&is=6a160283&hm=722a48ad8620b38fe0e2741fcf107e9e3e7de5bcd71cc352b505f7daa3ab58d8",
    "I know": "https://cdn.discordapp.com/attachments/1305175146281173034/1508931769347342526/image.png?ex=6a17fe78&is=6a16acf8&hm=b12eb2d45318452902a84490891052225942341cb36ac343c5f1e7080935e1a7",
    "annoyed": "https://cdn.discordapp.com/attachments/1305175146281173034/1508931921168830506/image.png?ex=6a17fe9c&is=6a16ad1c&hm=42d64fc13502d6661dde2fd7ec4fc5f2782a3607f53fae7e7a83fd148eaa376d",
    "sad": "https://media.discordapp.net/attachments/1305175146281173034/1508932028194885792/image.png?ex=6a17feb6&is=6a16ad36&hm=b447a86b38248f506069e33f70f99c985faee32f10690ea543f8f3e6bf370ac7&=&format=webp&quality=lossless",
    "shocked": "https://media.discordapp.net/attachments/1305175146281173034/1508932154430853241/image.png?ex=6a17fed4&is=6a16ad54&hm=47bf4920968d41c0f8d52af6137b9c13e37908f56851dbcb2594a98ec79afdf6&=&format=webp&quality=lossless",
    "shocked_o": "https://media.discordapp.net/attachments/1305175146281173034/1508932256444453057/image.png?ex=6a17feec&is=6a16ad6c&hm=8af920243761aed96cc3014f25cb43c42769f0a8006978184538ebd0ce39bfb6&=&format=webp&quality=lossless",
    "shocked_e": "https://media.discordapp.net/attachments/1305175146281173034/1508932329421148220/image.png?ex=6a17fefd&is=6a16ad7d&hm=2c19713c58136fa5c453714ac3e6c8f1ccc2c074b8244923d5406d96cd4e369f&=&format=webp&quality=lossless",
    "evil": "https://media.discordapp.net/attachments/1305175146281173034/1508932500267991211/image.png?ex=6a17ff26&is=6a16ada6&hm=fe8673798548090f6fea8804b127e72f7a646f16e9c13d13c538889ef14e405b&=&format=webp&quality=lossless",
    "annoyed 2": "https://media.discordapp.net/attachments/1305175146281173034/1508932610489847878/image.png?ex=6a17ff40&is=6a16adc0&hm=0ebb83d776fb5a32894dc6935ebc1e19cf974f887e03836659a0288b94a29baa&=&format=webp&quality=lossless",
    "annoyed 3": "https://media.discordapp.net/attachments/1305175146281173034/1508932650583457813/image.png?ex=6a17ff4a&is=6a16adca&hm=57f7c7e83b46a18ecad8be6561e297c84f8c32cc39401c26817cd4963742379e&=&format=webp&quality=lossless",
    "annoey closed eyes": "https://media.discordapp.net/attachments/1305175146281173034/1508932677414293624/image.png?ex=6a17ff50&is=6a16add0&hm=d9447b0ef811c168f16dae486a3609bbff415e1aca975d78e963d87de6b9df9b&=&format=webp&quality=lossless",
    "hey": "https://media.discordapp.net/attachments/1305175146281173034/1508932778195157173/image.png?ex=6a17ff68&is=6a16ade8&hm=68c9441f0c528b87624c55c6f562ba18664331eeef156e4826536b8f76bf0cf5&=&format=webp&quality=lossless",
    "hey ö": "https://media.discordapp.net/attachments/1305175146281173034/1508932816828895372/image.png?ex=6a17ff72&is=6a16adf2&hm=40459dd57d62e685c4d98996e8355d7b7fa408320fbc83582840f49cf46a0b2c&=&format=webp&quality=lossless",
    "madeline & theo shocked": "https://media.discordapp.net/attachments/1305175146281173034/1512139095541813370/image.png?ex=6a2300c6&is=6a21af46&hm=c49d6aae8ef09c175d2735cd08bb208df27d9581148ae9547db5d09537b059cd&=&format=webp&quality=lossless"
}

faces_badeline = {
    "annoyed": "https://media.discordapp.net/attachments/1509579385781620746/1509579488760037560/image.png?ex=6a19b0f4&is=6a185f74&hm=9ba9f42e117b13db9dcacddb0894e1223fb1391e718a9034a3024ec60fa0bed9&=&format=webp&quality=lossless",
    "disgust": "https://media.discordapp.net/attachments/1509579385781620746/1509579488760037560/image.png?ex=6a19b0f4&is=6a185f74&hm=9ba9f42e117b13db9dcacddb0894e1223fb1391e718a9034a3024ec60fa0bed9&=&format=webp&quality=lossless",
    "freak_1": "https://media.discordapp.net/attachments/1509579385781620746/1509579721606828226/image.png?ex=6a19b12c&is=6a185fac&hm=1debb5efbd8b2a61f10bb0f965252ec5d29303e76be81bc5a55917fd985b103b&=&format=webp&quality=lossless",
    "freak_2": "https://media.discordapp.net/attachments/1509579385781620746/1509579805144907887/image.png?ex=6a19b140&is=6a185fc0&hm=d84d4fb0b78977b426e4ec958176b24bf737f5c34266c46b665a24515b0c0cec&=&format=webp&quality=lossless",
    "bored": "https://media.discordapp.net/attachments/1509579385781620746/1509585240753045604/image.png?ex=6a19b650&is=6a1864d0&hm=adcd505b102925988f873cec64f95ec28f6a2ee70162d6cb640795fa9bba2b45&=&format=webp&quality=lossless",
    "bored_to_sleep": "https://media.discordapp.net/attachments/1509579385781620746/1509585417517797480/image.png?ex=6a19b67a&is=6a1864fa&hm=211cdd65e36c585104537fe807ae4fbefc228a26759b89cf5f1e3cef539b9cea&=&format=webp&quality=lossless",
    "why would you say that": "https://media.discordapp.net/attachments/1305175146281173034/1516145988518154332/image.png?ex=6a31947c&is=6a3042fc&hm=39595373bb084e958782bd16a856f0b7e7d53feab7e2c5cd9dec5331103b69cc&=&format=webp&quality=lossless"
}

celeste_lines = {
    "who cares": "https://media.discordapp.net/attachments/1305175146281173034/1516143607759765756/image.png?ex=6a319244&is=6a3040c4&hm=49cd2055e5ae34ca1fee12bb5e19ecabcc58b8ffb750a64bcde31a0836640748&=&format=webp&quality=lossless",
    "i hate it": "https://media.discordapp.net/attachments/1305175146281173034/1516143668690686146/image.png?ex=6a319253&is=6a3040d3&hm=87e99f9b225ea6d9a5b24eefec0699ca7c3bce71d9f96baca9f67a13d2b09646&=&format=webp&quality=lossless",
    "thanks for teaching me that": "https://media.discordapp.net/attachments/1305175146281173034/1516143743508418661/image.png?ex=6a319265&is=6a3040e5&hm=9fe978289cab13b10e6f4da94b1ea9f28ecac7c62192e8c66d00a24f1965e812&=&format=webp&quality=lossless",
    "don't jinx it": "https://media.discordapp.net/attachments/1305175146281173034/1516145363256610876/image.png?ex=6a3193e7&is=6a304267&hm=8c7146ef20e22d9b5d0eeaeac3497e2495096639caa994c9f7c78e932fd29e1a&=&format=webp&quality=lossless",
    "all pointless": "https://media.discordapp.net/attachments/1305175146281173034/1516143034876694578/image.png?ex=6a3191bc&is=6a30403c&hm=0fdc520cf961cd3b614d1ade1bf885eb06a57945d990d6c753d37e2150b17aa0&=&format=webp&quality=lossless",
    "helpful": "https://media.discordapp.net/attachments/1305175146281173034/1516143282055545035/image.png?ex=6a3191f7&is=6a304077&hm=1a0614f8e559a5203f3b7ee42bbd519cf564753d9239b9ff3d6ebaedbcb8e456&=&format=webp&quality=lossless",
    "not helpful": "https://media.discordapp.net/attachments/1305175146281173034/1516143400414609559/image.png?ex=6a319213&is=6a304093&hm=9c242b4519d51d39ce052d04e31c77bf8676ceda97bcef95238185f0529e7a12&=&format=webp&quality=lossless"
}

class CelesteSticker(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(
        name = "madeline",
        description = "Sends a Madeline sticker"
    )
    async def madeline(self,
                       ctx:discord.ApplicationContext,
                       choice=discord.Option(
                           str,
                           "choose a face",
                           choices=faces_madeline.keys()
                       )
                       ):
        await ctx.respond(faces_madeline[choice])

    @discord.slash_command(
        name = "badeline",
        description = "Sends a Badeline sticker"
    )
    async def badeline(self,
                       ctx:discord.ApplicationContext,
                       choice=discord.Option(
                           str,
                           "choose a face",
                           choices=faces_badeline.keys()
                       )
                       ):
        await ctx.respond(faces_badeline[choice])

    @discord.slash_command(
        name = "celeste_quotes",
        description = "Sends a celeste quote"
    )
    async def celeste_quote(self,
                            ctx:discord.ApplicationContext,
                            choice=discord.Option(
                                str,
                                "choose a quote",
                                choices=celeste_lines.keys()
                            )
                            ):
        await ctx.respond(celeste_lines[choice])

def setup(bot):
    bot.add_cog(CelesteSticker(bot))