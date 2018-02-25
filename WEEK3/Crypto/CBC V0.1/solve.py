# -*- coding:utf-8 -*-
import requests
import re


def xor(a, b):
    return ''.join([chr(ord(x[0]) ^ ord(x[1])) for x in zip(a, b)])


def addIV(iv, pos):
    iv = list(iv.decode('hex'))
    iv[pos] = chr(ord(iv[pos]) + 1)
    return ''.join(iv).encode('hex')


def newMid(iv, pos, mid):
    mid = mid.decode('hex')
    iv = list(iv.decode('hex'))
    mid = chr(ord(iv[pos]) ^ (16 - pos)) + mid
    return mid.encode('hex')


def newIV(mid, pos):
    mid = list(mid.decode('hex'))
    iv = '0' * pos * 2
    tmp = 17 - pos
    for i in mid:
        iv = iv + chr(ord(i) ^ tmp).encode('hex')
    return iv


iv = '0' * 32
mid = ''
l = 15
c = "0" * 32

url = "http://123.206.203.108:10001/padding/index.php?token="
while l > 0:
    res = requests.get(url + iv + c)
    if "decrypt error" not in res.content:
        mid = newMid(iv, l, mid)
        iv = newIV(mid, l)
        l = l - 1
        print iv, mid
        continue
    iv = addIV(iv, l)

# 15 0078a470af26f9f02edd44a5ce7f4ce6 68b460bf36e9e03ecd54b5de6f5cf6

plaintext = 'admin\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b'
for i in range(256):
    niv = xor(plaintext, (chr(i).encode('hex') + mid).decode('hex')).encode('hex')
    res = requests.get(url + niv + c)
    if "hgame" in res.content:
        print "token:", niv + c
        print res.content
        break


