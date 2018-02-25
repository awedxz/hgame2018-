from pwn import *
import base64
import string
import hashlib
context.log_level = 'debug'

def cbcByteFlip(iv, pos, plaintext, want):
    iv = list(iv)
    iv[pos] = chr(ord(iv[pos]) ^ ord(plaintext) ^ ord(want))
    return ''.join(iv)

allChar = string.ascii_letters + string.digits

def proof(md5Str, md5Re):
    for a in allChar:
        for b in allChar:
            for c in allChar:
                for d in allChar:
                    if hashlib.md5(a + b + c + d + md5Str).hexdigest() == md5Re:
                        return a + b + c + d

r = remote('123.206.203.108', 6666)
# r = remote('0.0.0.0', 6666)

data = r.recvuntil("XXXX:")
md5Str = data[77:89]
md5Re = data[94:126]
print md5Str, md5Re
r.sendline(str(proof(md5Str, md5Re)))
r.recvuntil('2.login')
r.sendline('1')
r.recvuntil('username: ')
r.sendline('admimaaaaaaaaaa')
token = r.recv()[11:]
# print token
iv = base64.b64decode(token)[:16]
niv = cbcByteFlip(iv, 15, '\x01', 'm')
niv = cbcByteFlip(niv, 4, 'm', 'n')
ntoken = base64.b64encode(niv + base64.b64decode(token)[16:])
# print ntoken
sig = "d41d8cd98f00b204e9800998ecf8427e"

r.recvuntil('2.login')
r.sendline('2')
r.recvuntil('give me your token: ')
r.sendline(ntoken)
r.recvuntil('give me your sig: ')
r.sendline(sig)
r.recvuntil('flag')
