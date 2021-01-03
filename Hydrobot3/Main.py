from HydroBot import HydroBot
from Commands import commands


with open("token.txt") as tokenfile:
    hydroBotToken = tokenfile.readlines()[0]
    tokenfile.close()


hydroBot = HydroBot(hydroBotToken, "-", commands)
hydroBot.run()
