import SocketServer

def xor(a, b):
    return ''.join([chr(ord(x[0]) ^ ord(x[1])) for x in zip(a, b)])

def add(a, b):
    return ''.join([chr((ord(x[0]) + ord(x[1])) % 256) for x in zip(a, b)])

def padding(msg, length):
    if len(msg)%length == 0:
        return msg
    padding_size = length - (len(msg)%length)
    return msg + '\x01' * padding_size

def str2hex(s):
    return s.encode('hex')

def encrypt_block(key, msg):
    v = 0x20
    for i in range(v):
        msg = xor(key, msg)
        msg = add(key, msg)
        msg = msg[1:] + msg[:1]
    return msg

def encrypt(key, msg):
    result = ""
    msg = padding(msg, 0x20)
    for i in range(len(msg) / 0x20):
        result += encrypt_block(key, msg[0x20*i:0x20*(i+1)])
    return result

flag = "hgame{*************************}"

class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    pass

class MyTCPHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        self.request.sendall("Welcome to xasr(XOR ADD SHIFT repeat) encrypt system\n")
        while 1:
            self.request.sendall("give me you text: ")
            plaintext = self.request.recv(1024).strip()
            cipher = str2hex(encrypt(flag, plaintext))
            self.request.sendall("result: " + cipher + '\n')

if __name__ == "__main__":
    HOST, PORT = "0.0.0.0", 23555
    server = ThreadedTCPServer((HOST, PORT), MyTCPHandler)
    server.serve_forever()