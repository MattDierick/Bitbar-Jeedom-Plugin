#!/usr/bin/env python
# -*- coding: utf-8 -*-
# <bitbar.title>Jeedom plugin</bitbar.title>
# <bitbar.version>1.0</bitbar.version>
# <bitbar.author>Matthieu DIERICK</bitbar.author>
# <bitbar.author.github>MattDierick</bitbar.author.github>
# <bitbar.desc>Keep an eye on Jeedom devices</bitbar.desc>
# <bitbar.dependencies>python</bitbar.dependencies>
# <bitbar.image>https://raw.githubusercontent.com/MattDierick/Bitbar-Jeedom-Plugin/master/images/screenshot2.png</bitbar.image>

import urllib2

HOSTNAME = "YOUR_HOSTNAME_FQDN:PORT"
JEEDOM_KEY = "YOUR_JEEDOM_KEY"

# Replace with desired ID. You can add more ID or Groups
idlistGRP1 = ['270', '282', '283', '477']
namelistGRP1 = ["Temp Piscine :", "PH :", "Chlore :", "Durée filtration :"]
unitlistGRP1 = ["°C", "", "", ""]

idlistGRP2 = ['449', '450']
namelistGRP2 = ["Temp jardin :", "Humidité :"]
unitlistGRP2 = ["°C", "%"]

idlistGRP3 = ['541']
namelistGRP3 = ["Caméra jardin :"]
unitlistGRP3 = [""]


print (' | image=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')
print "---"

for i in range(len(idlistGRP1)):
    url = "http://{}/core/api/jeeApi.php?apikey={}&type=cmd&id={}".format(HOSTNAME, JEEDOM_KEY, idlistGRP1[i])
    req = urllib2.Request(url)
    result = urllib2.urlopen(req).read()
    if result == "1":
        result = "on"
        COLORS = "green"
    elif result == "0":
        result = "off"
        COLORS = "red"
    else:
        COLORS = "black"
    print namelistGRP1[i], "{}".format(result), unitlistGRP1[i], "| color=black"

print "---"

for i in range(len(idlistGRP2)):
    url = "http://{}/core/api/jeeApi.php?apikey={}&type=cmd&id={}".format(HOSTNAME, JEEDOM_KEY, idlistGRP2[i])
    req = urllib2.Request(url)
    result = urllib2.urlopen(req).read()
    if result == "1":
        result = "on"
        COLORS = "green"
    elif result == "0":
        result = "off"
        COLORS = "red"
    else:
        COLORS = "black"
    print namelistGRP2[i], "{}" .format(result), unitlistGRP2[i], "| color=", COLORS

print "---"

for i in range(len(idlistGRP3)):
    url = "http://{}/core/api/jeeApi.php?apikey={}&type=cmd&id={}".format(HOSTNAME, JEEDOM_KEY, idlistGRP3[i])
    req = urllib2.Request(url)
    result = urllib2.urlopen(req).read()
    if result == "1":
        result = "on"
        COLORS = "green"
    elif result == "0":
        result = "off"
        COLORS = "red"
    else:
        COLORS = "black"
    print namelistGRP3[i], "{}" .format(result), unitlistGRP3[i], "| color=", COLORS
