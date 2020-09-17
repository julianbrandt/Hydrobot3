import discord.ext.commands as cms
import Funcs

commands = [
    cms.Command(
        Funcs.pick,
        name="pick",
        brief="Picks a random input",
        description="Picks and returns one of given arguments at random."
    ),
    cms.Command(
        Funcs.roll,
        name="roll",
        brief="Rolls a random number",
        description="Picks a random number between 1 and a given number (or optionally between two given numbers)."
    ),
    cms.Command(
        Funcs.meme,
        name="meme",
        brief="Makes a custom meme",
        description="Creates a meme with given text or images pasted onto a chosen template.\n"
                    "Do '-meme list' to list all available meme templates.\n"
                    "Visit https://github.com/julianbrandt/MemePy for full docs on the meme-engine"
    ),
    cms.Command(
        Funcs.definition,
        name="definition",
        brief="Gets the definition of a word",
        description="Gives the definition of an english word"
    )
]