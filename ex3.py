#!/usr/local/bin/python3

import time
import random
import string

print (int(time.time() * 256))
print (int(time.time()) - 123170)

random.seed(348946227264)
#tried this: for m in range(348946227264, 348946227294): ,didn't *256
#tried this: for m in range(1363071202, 1363071232):, did *256

for m in range(1363071202, 1363071232):
  random.seed(m*256)
  secret = ''.join(random.choice(string.ascii_letters) for i in range(12))
  print (secret)

