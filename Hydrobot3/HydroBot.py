#!/usr/bin/env python

import discord.ext.commands as cms

class HydroBot(cms.Bot):
    def __init__(self, token, prefix, commands=None):
        self._token = token
        super().__init__(prefix)
        if commands is not None:
            self.add_commands(commands)

    def add_commands(self, commands):
        for c in commands:
            self.add_command(c)

    def run(self):
        while True:
            print("Starting Bot")
            super().run(self._token)
