#!/usr/bin/env python

import discord
import discord.ext.commands as cms
from random import choice
import sys
from Util import find_word
import math
from MemePy import MemeGenerator
import traceback

with open("token.txt") as tokenfile:
    hydroBotToken = tokenfile.readlines()[0]
    tokenfile.close()

hydroBot = cms.Bot(command_prefix="-")
hydroBot.remove_command("help")


@hydroBot.command()
async def help(ctx):
    return await ctx.channel.send("Help yourself.")


@hydroBot.command()
async def pick(ctx, *args):
    return await ctx.channel.send(choice(args))


@hydroBot.command()
async def roll(ctx, arg1, arg2=1):
    try:
        arg1 = int(arg1)
        arg2 = int(arg2)
        lower = min(arg1, arg2)
        higher = max(arg1, arg2)
        return await ctx.channel.send(choice(range(lower, higher)))
    except (OverflowError, ValueError):
        return await ctx.channel.send("Input numbers must be integers lower than " + str(sys.maxsize))


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


@hydroBot.command()
async def meme(ctx, template, *args):
    try:
        for s in args:
            if len(str(s)) > 100:
                return await ctx.channel.send("Any argument cannot be longer than 100 characters.")
        meme_image_bytes = MemeGenerator.get_meme_image_bytes(template, args)
        return await ctx.channel.send(file=discord.File(meme_image_bytes, "meme.png"))
    except Exception as e:
        print(traceback.format_exc())
        return await ctx.channel.send(str(e))


print("Running HydroBot")
hydroBot.run(hydroBotToken)