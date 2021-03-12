from HydroBot import HydroBot
from Commands import commands
from MemePy import MemeGenerator, MemeFactory


with open("token.txt") as tokenfile:
    hydroBotToken = tokenfile.readlines()[0]
    tokenfile.close()

MemeGenerator.add_external_resource_dir("hydro_lib")

hydroBot = HydroBot(hydroBotToken, "-", commands)
hydroBot.run()
