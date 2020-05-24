import random
import time

rmdi = str(random.randint(1, 9))
_TOKEN_ = "f" + rmdi + "k" + rmdi + "l" + rmdi + "kf" + rmdi + "j29gk48fjJg92" + rmdi + "fm4jf"
def full(TOKEN, token_handshake="/packages_from_url/", msF5="json_w"):
    print(token_handshake + TOKEN + "/reader/" + msF5)
full(_TOKEN_)
time.sleep(0.8)
print("Setting sucessfuly")
print()