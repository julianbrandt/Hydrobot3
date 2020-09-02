#!/usr/bin/env python

import discord
import sys
from Util import find_word, is_link
import math
from MemePy import MemeGenerator
from random import choice
import traceback
from PIL import UnidentifiedImageError


async def pick(ctx, *args):
    return await ctx.channel.send(choice(args))


async def roll(ctx, arg1, arg2=1):
    try:
        arg1 = int(arg1)
        arg2 = int(arg2)
        lower = min(arg1, arg2)
        higher = max(arg1, arg2)+1
        return await ctx.channel.send(choice(range(lower, higher)))
    except (OverflowError, ValueError):
        return await ctx.channel.send("Input numbers must be integers lower than " + str(sys.maxsize))


async def meme(ctx, template, *args):
    try:
        for s in args:
            if is_link(s):
                return await ctx.channel.send("Link-arguments must be surrounded by '<' '>' angle brackets.\n`<https://example.com/image.jpg>`")
            elif len(s) > 2 and is_link(s[1:-1]):
                pass
            elif len(str(s)) > 100:
                return await ctx.channel.send("Any argument cannot be longer than 100 characters.")
        meme_image_bytes = MemeGenerator.get_meme_image_bytes(template, list(args))
        return await ctx.channel.send(file=discord.File(meme_image_bytes, "meme.png"))
    except UnidentifiedImageError:
        print(traceback.format_exc())
        return await ctx.channel.send("Could not identify image file.")
    except Exception as e:
        print(traceback.format_exc())
        return await ctx.channel.send(str(e))


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