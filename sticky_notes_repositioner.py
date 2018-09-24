#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import json
import subprocess

# Read notes
file_path = os.path.expanduser('~') + '/.cinnamon/configs/sticky@scollins/sticky@scollins.json'
with open(file_path, "r") as json_file:
    data = json.load(json_file)

# Change note position
for i, value in enumerate(data["storedNotes"]["value"]):
    data["storedNotes"]["value"][i]['x'] = 1649

# Write notes with new position
with open(file_path, "w") as json_file:
    json.dump(data, json_file)

# Refresh note applet
dbus_command = "dbus-send --session --dest=org.Cinnamon.LookingGlass --type=method_call /org/Cinnamon/LookingGlass org.Cinnamon.LookingGlass.ReloadExtension string:'sticky@scollins' string:'APPLET'"
subprocess.Popen(dbus_command, shell=True, stdout=subprocess.PIPE)
