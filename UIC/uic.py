import argparse
import requests
import os
import time

parser = argparse.ArgumentParser()

parser.add_argument("-m","--mode",default="False",dest="mode",help="Change agressive(True) or passive(False) mode",required=True)

args = parser.parse_args()

def agressive():
    print("Packages request")
    print("Requesting SQL Injection...")
    requests.post("https://" + x + "/select+from+limit+27%")
    print("Packages request")
    print("Requesting SQL Injection...")
    requests.post("https://" + x + "/select+from+limit+27%")
    print("Packages request")
    print("Requesting SQL Injection...")
    requests.post("https://" + x + "/select+from+limit+27%")
    print("Packages request")
    print("Requesting SQL Injection...")
    requests.post("https://" + x + "/select+from+limit+27%")

def passive():
    print("Requesting...")
    requests.post("https://" + x)
    print("Requesting...")
    requests.post("https://" + x)
    print("Requesting...")
    requests.post("https://" + x)


import settings
x = input("https://")
url = open("./url.txt", "w")
url.write("https://" + x)
print("Starting requesting on https://" + x)
requests.get("https://" + x)

if args.mode == True:
    while True:
        try:
            agressive()
        except:
            break
elif args.mode == False:
    while True:
        try:
            passive()
        except:
            break

time.sleep(2)

print("Check handshake in file ./packages_from_url/TOKEN/saved/saved.json")

json_file = open("packages_from_url/TOKEN/saved//saved.json", "w")
json_file.write('''
{
  "save_in_pkg": 1,
  "HREF_SAVING": "scan_set.json / 6 {JavaContainer.files}",
  "HREF_save": "$this->Object",
  "JSON_SAVING": 1,
  "files": {
    "files": {
      "dir": [".","..","Hand_00_shake45sd21.json","content_type","coding:utf-8","dpy_injection","leader_check","html_content_type","json.inner_file"],
      "api.txt": ["API:", "L:r/js"]
    }
  }
}
''')