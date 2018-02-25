#-*- coding:utf-8 -*-
import SocketServer
from Crypto.Cipher import AES
from Crypto import Random
import base64
import hashlib
import string
import random
import time

salt = "qwertyuiokmnbvcxzaqsdfghjk"
flag = "hgame{Congr@tv1atIons_0n_havin9_d*ne_!t}"
BS = AES.block_size
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s : s[0:-ord(s[-1])]


class AEScoder():
    def __init__(self):
        self.key = "1qazxsw23edcvfr4"

    def encrypt(self, plaintext):
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        ciphertext = cipher.encrypt(plaintext)
        return base64.b64encode(iv + ciphertext)

    def decrypt(self, ciphertext):
        ciphertext = base64.b64decode(ciphertext)
        iv = ciphertext[0:AES.block_size]
        ciphertext = ciphertext[AES.block_size:len(ciphertext)]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        plaintext = cipher.decrypt(ciphertext)
        return plaintext


class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    pass


class MyTCPHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        self.request.sendall("Welcome to flag getting system\n")
        while 1:
            proof = ''.join([random.choice(string.ascii_letters + string.digits) for i in range(16)])
            hProof = hashlib.md5(proof).hexdigest()
            self.request.sendall("Now prove to me that you want flag\nMD5(XXXX + {}) == {}\nXXXX: ".format(proof[4:], hProof))
            x = self.request.recv(1024).strip()    
            if len(x) != 4 or hashlib.md5(x + proof[4:]).hexdigest() != hProof:
                self.request.sendall("It seems that you are not ready to get the flag\n\n")
            else:
                break
        A = AEScoder()
        while 1:
            self.request.sendall("tell me what do you want to do:\n1.register\n2.login\n")
            choose = self.request.recv(1024).strip()
            if choose == '1':
                self.request.sendall("what's your username: ")
                plaintext = self.request.recv(1024).strip()
                if 'admin' in plaintext:
                    self.request.sendall("you are hacker!!!\n\n")
                    continue
                self.request.sendall("your token: " + A.encrypt(pad(plaintext)) + '\n')
                self.request.sendall("your sig: " + hashlib.md5(salt + plaintext).hexdigest() + '\n\n')
            elif choose == '2':
                self.request.sendall("give me your token: ")
                token = self.request.recv(1024).strip()
                self.request.sendall("give me your sig: ")
                sig = self.request.recv(1024).strip()
                # f = open('access.log', 'a+')
                # f.write("time: {}, ip: {}, token: {}, sig: {} \n".format(time.asctime(time.localtime(time.time())), self.client_address, token, sig))
                # f.close()
                plaintext = A.decrypt(token)
                # self.request.sendall(plaintext.encode('hex') + '\n\n')
                if sig == hashlib.md5(unpad(salt + plaintext)).hexdigest():
                    if 'admin' in plaintext:
                        self.request.sendall("hello admin, here is flag: " + flag + '\n\n')
                    else:
                        self.request.sendall("you are not admin, you cant get flag\n\n")
                else:
                    self.request.sendall("I dont think you are yourself\n\n")
            else:
                continue


if __name__ == "__main__":
    HOST, PORT = "0.0.0.0", 6666
    server = ThreadedTCPServer((HOST, PORT), MyTCPHandler)
    server.serve_forever()
