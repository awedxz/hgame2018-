# -*- coding:utf-8 -*-
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

flag = "hgame{OAEP_i3_safer%$#}"

with open('pubkey.pem', 'r') as f:
    key = RSA.importKey(f)
    N = key.n
    e = key.e

with open('private.pem', 'r') as f:
    private = RSA.importKey(f)
    oaep = PKCS1_OAEP.new(private)

with open('flag.enc', 'w') as f:
    f.write(oaep.encrypt(flag))
    f.close()

with open('flag.enc', 'r') as f:
    print oaep.decrypt(f.read())

# 还有一种 openssl rsautl -decrypt -oeap -in flag.enc -inkey private.pem