from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
from gmpy2 import invert

with open('pubkey.pem') as f:
    key = RSA.importKey(f)
    N = key.n
    e = key.e

print N
print e

# factordb.com
p = 275127860351348928173285174381581152299
q = 319576316814478949870590164193048041239
# git clone https://github.com/ius/rsatool.git
# python rsatools.py -f PEM -o private.pem -p 275127860351348928173285174381581152299 -q 319576316814478949870590164193048041239
# openssl rsautl -decrypt -inkey private.pem -in flag.enc -out flag
