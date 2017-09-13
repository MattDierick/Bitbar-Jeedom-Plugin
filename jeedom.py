#!/usr/bin/env python
# -*- coding: utf-8 -*-
# <bitbar.title>Jeedom plugin</bitbar.title>
# <bitbar.version>1.0</bitbar.version>
# <bitbar.author>Matthieu DIERICK</bitbar.author>
# <bitbar.author.github>MattDierick</bitbar.author.github>
# <bitbar.desc>Keep an eye on Jeedom devices</bitbar.desc>
# <bitbar.dependencies>python</bitbar.dependencies>
# <bitbar.image>https://github.com/MattDierick/Bitbar-Jeedom-Plugin/blob/master/images/screenshot.png</bitbar.image>

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


print "Jeedom"
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
