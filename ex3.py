#!/Users/danluu/Dropbox/classes/HS/marek-crypto/john-1.7.9/doc/test2/bin/python3

import time
import random
import string
import re
import requests


import urllib.request
f = urllib.request.urlopen("http://pragmaticcrypto.herokuapp.com/exercise3/")
site = f.read()
marek_delay = int(re.search(b'(\d+) seconds', site).groups()[0]) + 1
mytime = int(time.time())

time_guess = mytime - marek_delay

url = r'http://pragmaticcrypto.herokuapp.com/exercise3/'
a = 2348390

s = requests.Session()

for skew in range(-1, 2):
  for m in range(0, 256):
    random.seed((time_guess + skew) * 256 + m)
    secret = ''.join(random.choice(string.ascii_letters) for i in range(12))
    res = s.post(url, data={'password': secret})
    if res.status_code == 200:
      print(secret)
      print(res)
      break



