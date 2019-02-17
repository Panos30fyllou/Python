# coding=utf-8
import re
import urllib.request

url = input("Eisagete dieuthinsi: ") #eisagetai to url ap ton xrhsth

if not url.startswith("http"): #se periptosh pou ap to url leipei to http, h metavlhth tropopoieitai katallhla
    url += "http://"
ap = urllib.request.urlopen(url)
html = ap.read().decode()

l = len(re.findall(r'<a .*?href=".*?".*?>.*?<\/a>', html)) #arithmos link

nl = len(re.findall(r'<br .*?/?>', html))
nl += len(re.findall(r'<p .*?>.*?<\/p>', html)) #arithmos new line

print("H istoselida exei " + str(l) + " syndesmous")
print("H istoselida exei " + str(nl) + " allages grammhs")
