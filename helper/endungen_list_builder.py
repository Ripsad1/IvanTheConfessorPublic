import discord
from helper.dict_saver_and_loader import load_dict

WOERTER_FILE = "woerter_mit_endungen.json"
MAX_FIELD = 1024
MAX_FIELDS = 25
MAX_TOTAL = 5800
ZWSP = "\u200b"


def _spalten(woerter, ziel=3):
    """Verteilt die Wörter auf Spalten, sodass keine über MAX_FIELD kommt.
    Erhöht die Spaltenzahl, bis es passt. None, wenn es nicht mehr reicht."""
    n = ziel
    while n <= MAX_FIELDS:
        k, r = divmod(len(woerter), n)
        teile, start = [], 0
        for i in range(n):
            size = k + (1 if i < r else 0)
            teile.append(woerter[start:start + size])
            start += size
        teile = [t for t in teile if t]
        if all(len("\n".join(t)) <= MAX_FIELD for t in teile):
            return teile
        n += 1
    return None


def create_list_endung(endung):
    """Baut den Embed für eine Endung. Fängt unbekannte und leere
    Endungen selbst ab und gibt immer einen sendbaren Embed zurück."""
    woerter_dict = load_dict(WOERTER_FILE)
    roh = woerter_dict.get(endung)

    if roh is None:
        bekannt = ", ".join(f"`{e.lstrip('-')}`" for e in sorted(woerter_dict))
        return discord.Embed(
            title="Unbekannte Endung",
            description=(f"`{endung}` wird nicht getrackt.\n\n"
                         f"Verfügbar: {bekannt or '—'}"),
            color=discord.Color.red(),
        )

    embed = discord.Embed(title=f"{endung} Liste", color=discord.Color.blue())

    woerter = sorted(dict.fromkeys(roh))
    if not woerter:
        embed.description = "Noch keine Wörter mit dieser Endung."
        return embed

    dupes = len(roh) - len(woerter)
    footer = f"{len(woerter)} Wörter"
    if dupes:
        footer += f" ({dupes} Duplikate ausgeblendet)"

    # Zeichenbudget einhalten (Embed gesamt max. 6000)
    passend, verbraucht = [], len(endung) + len(footer) + 40
    for w in woerter:
        if verbraucht + len(w) + 1 > MAX_TOTAL:
            break
        passend.append(w)
        verbraucht += len(w) + 1

    if len(passend) < len(woerter):
        footer += f" — nur die ersten {len(passend)} angezeigt"

    teile = _spalten(passend)

    for teil in teile:
        embed.add_field(name=ZWSP, value="\n".join(teil), inline=True)

    embed.set_footer(text=footer)
    return embed