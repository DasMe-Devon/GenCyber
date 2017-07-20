#!/usr/bin/env python

import markovify
import sys

f = open(sys.argv[1])
text = f.read()
model = markovify.NewlineText(text,state_size=2)

for i in range(4):
	#print(model.make_short_sentence(80))
	print(model.make_sentence(tries=100))
	print("...")
