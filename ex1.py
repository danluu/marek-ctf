#!/usr/bin/python

import struct

def _lcg(state):
    return (1103515245*state + 12345) % (2**31)

def lcg_generator(seed):
    state = seed
    while True:
        state = _lcg(state)
        yield state

with open('/dev/urandom', 'rb') as f:
    seed, = struct.unpack('I', f.read(4))

gen = lcg_generator(seed)

val = 1
while val != 1245434130:
  last_val = val
  val = gen.next()

print val
print last_val
