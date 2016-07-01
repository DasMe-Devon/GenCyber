#!/usr/bin/env python
	#Setup script to use python.

import requests
	# this library is used for making web requests.
import re
	# this library is used for pattern matching.

processed = []
	# this bucket is used to hold urls we have processed.
unprocessed = []
	# this bucket is used to hold urls we have not processed.
emails = []
	# this bucket holds email addresses we find.
target = raw_input("What URL should we crawl? ")
	# Asks the user for a URL.
href = re.compile('href="([^"]*)')
	# This defines a HREF pattern to search for.
email = re.compile('mailto:([^"]*)')
	# This defines an email pattern to search for.
fetch = requests.get(target)
	# This line requests a resource from a webserver and contains the response.

matches = href.findall(fetch.text)
ematches = email.findall(fetch.text)
# the .findall method will attempt to find all matching pattern. Returns a list of matches.
for site in matches:
	if(target in site):
		unprocessed.append(site)

for eaddr in ematches:
	if(eaddr not in emails):
		emails.append(eaddr)
		print "Found email: %s" % eaddr

#This loop will continue as long as their are new links to crawl.
while( len(unprocessed) > 0):
	target = unprocessed.pop()
	# Remove the last website added to the list.
	processed.append(target)	
		# This contains a website to scan.
	print "Scanning: %s" % target
	fetch = requests.get(target)
		# This retrieves a webpage and stores it in fetch.
	matches = href.findall(fetch.text)
	for link in matches:
		if(link not in processed and link not in unprocessed):
			if(target in link):
				unprocessed.append(link)
	#This block of code will store email addresses found.
	ematches = email.findall(fetch.text)	
	for eaddr in ematches:
		if(eaddr not in emails):
			emails.append(eaddr)
			print "Found email: %s" % eaddr

	print "Identified %i emails!" % len(emails)
	print "Processed %i urls!" % len(processed)
	
print "Found a total of %i urls!" % len(processed)
print "Found a total of %i emails!" % len(emails)