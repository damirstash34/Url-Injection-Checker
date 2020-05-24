import random

import requests
from time import sleep

version = "1.0"
creator = "damirstash34"
package = False
def adminSettings():
    requests.post("https://github.com/stleary/JSON-java.git")
    JSON = ".json"
    sleep(0.9)
    print("Starting set()")
    sleep(1)
    asd = 1
    while asd < 100:
        print(random.randint(100, 999))
        sleep(0.1)
        asd += 1

    print("Settings sucesfully!")

adminSettings()