from MemePy import MemeFactory
import discord

descriptions = {
    "meme" : "Posts a meme created from your input",
    "definition" : "Get the definitions of a given word"
}

def help_general(command):
    if command == "meme": return help_meme()
    elif command == "definition": return help_definition()
    else: return discord.Embed(title="No command found by name: " + command, color=0xff6347)


def help_meme():
    embed = discord.Embed(title="-meme <template> <args>*\n"
                                + descriptions["meme"], color=0xff6347)
    embed.set_author(name="Help for -meme command")
    memes = MemeFactory.MemeLib
    for m in memes:
        non_optional = memes[m].count_non_optional()
        value = "Arguments: %i" % non_optional
        optional = len(memes[m].text_zones) - non_optional
        if optional > 0:
            value += " + %i optional." % optional
        embed.add_field(name=m, value=value, inline=False)
    return embed


def help_definition():
    embed = discord.Embed(title="-definition <word>\n"
                                + descriptions["definition"], color=0xff6347)
    embed.set_author(name="Help for -definition command")
    return embed