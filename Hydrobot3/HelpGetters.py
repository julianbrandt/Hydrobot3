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
    for m in MemeFactory.MemeLib:
        non_optional = m.meme_image.count_non_optional()
        value = "Arguments: " + non_optional
        optional = len(m.meme_image.text_zones) - non_optional
        if optional > 0:
            value += " + " + optional + " optional."
        embed.add_field(name=m, value=value, inline=False)
    return embed


def help_definition():
    embed = discord.Embed(title="-definition <word>\n"
                                + descriptions["definition"], color=0xff6347)
    embed.set_author(name="Help for -definition command")
    return embed