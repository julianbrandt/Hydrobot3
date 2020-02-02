import discord
import discord.ext.commands as cms
from bs4 import BeautifulSoup
import requests
import re


def get_soup_object(url, parser="html.parser"):
    return BeautifulSoup(requests.get(url).text, parser)


# Modified version of "meaning" in PyDictionary (https://github.com/geekpradd/PyDictionary)
def find_word(term, disable_errors=False):
    if len(term.split()) > 1:
        print("Error: A Term must be only a single word")
    else:
        try:
            html = get_soup_object(
                "http://wordnetweb.princeton.edu/perl/webwn?c=0&sub=Change&o2=&o0=1&o8=1&o1=1&o7=&o5=&o9=&o6=&o3=&o4=&i=-1&s={0}".format(
                    term))
            types = html.findAll("h3")
            lists = html.findAll("ul")
            out = {}
            for a in types:
                reg = str(lists[types.index(a)])
                meanings = []
                for x in re.findall(r'.*> \((.*)\) </li.*', reg):
                    if 'often followed by' in x:
                        pass
                    elif len(x) > 5 or ' ' in str(x):
                        meanings.append(x)
                name = a.text
                out[name] = meanings
            return out
        except Exception as e:
            if disable_errors == False:
                print("Error: The Following Error occured: %s" % e)