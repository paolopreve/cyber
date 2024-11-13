#!/usr/bin/env python3
import random
import sys
import time
"""
cur_time = str(time.time()).encode('ASCII')
random.seed(cur_time)

msg = input('Your message: ').encode('ASCII')
key = [random.randrange(256) for _ in msg]
c = [m ^ k for (m,k ) in zip(msg + cur_time, key + [0x88]*len(cur_time))]

with open(sys.argv[1], "wb") as f:
    f.write(bytes(c))
"""
with open("top_secret", "rb") as f:
    input = f.read()

#print(input)
c = [chr(m ^ k) for (m,k ) in zip(input, [0x88]*len(input))]

#1513719133.8728752
#print(c)
cur_time = str("1513719133.8728752").encode('ASCII')
random.seed(cur_time)
key = [random.randrange(256) for _ in input]
a = [chr(m ^ k) for (m,k ) in zip(input, key)]
text = ''.join(a)
b = text[:len(input) - len(cur_time)]
print(b)
