#! /usr/bin/python2.7
from Crypto.Util.number import getPrime

flag = "hgame{sHa2e_i3_dan9erOus_1N_RSA}"
msg = int(flag.encode('hex'), 16)
e = 65537
primes = []

f = open('cipherx.txt', 'w')

for i in range(5):
    primes.append(getPrime(1024))

for p in primes[::-1]:
    primes.pop()
    for q in primes:
        if p != q:
            n = p * q
            f.write(str(pow(msg, e, n)) + '\n')

