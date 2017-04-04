#!/usr/bin/env python
# -*- coding: utf-8 -*-

# bulk json changer used for ASF and stuff
# by jfx
# run outside of the folder and modify the keys below
import os, json

dir = "test"
key = "ShutdownOnFarmingFinished"
value = False

for file in os.listdir(dir):
	if file.endswith(".json"):
		filepath = dir + "/" + file
		with open(filepath, 'r') as f:
			print "Reading file: " + file
			data = json.load(f)
			data[key] = value
		os.remove(filepath)
		with open(filepath, 'w') as f:
			json.dump(data, f, indent=4, sort_keys=False)
			print "Successfully modified file: " + file
