#!/usr/bin/env python

import discord
import discord.ext.commands as cms
from random import choice
import sys
from Util import find_word
import math

with open("token.txt") as tokenfile:
    hydroBotToken = tokenfile.readlines()[0]
    tokenfile.close()

hydroBot = cms.Bot(command_prefix="-")
hydroBot.remove_command("help")


@hydroBot.command()
async def pick(ctx, *args):
    await ctx.channel.send(choice(args))


@hydroBot.command()
async def roll(ctx, arg1, arg2=1):
    try:
        arg1 = int(arg1)
        arg2 = int(arg2)
        lower = min(arg1, arg2)
        higher = max(arg1, arg2)
        await ctx.channel.send(choice(range(lower, higher)))
    except (OverflowError, ValueError):
        await ctx.channel.send("Input numbers must be integers lower than " + str(sys.maxsize))


@hydroBot.command()
async def definition(ctx, word):
    message = find_word(word)
    if message is None:
        return await ctx.channel.send("No definition found for \"" + str(word) + "\"")
    else:
        embed = discord.Embed(title="Definition of: " + word, url="http://wordnetweb.princeton.edu/perl/webwn?s=" + word, color=0xff6347)
        embed.set_author(name="WordNet", url="https://wordnet.princeton.edu/")
        for category in message:
            for index, item in enumerate(message[category]):
                if index == math.floor(4/len(message.items())):
                    break
                embed.add_field(name=str(index+1) + ". " + category, value=item, inline=False)
        message = embed
    return await ctx.channel.send(embed=message)


print("Running HydroBot")
hydroBot.run(hydroBotToken)