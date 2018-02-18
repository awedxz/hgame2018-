# a = 7
# b = 19
# m = "sometimes_it_takes_a_bit_of_violence"

flag = "hgame{" + m + "}"

cipher = ''
for i in m:
    if 96 < ord(i) < 123:
        cipher += chr(a * (ord(i) + b - 97) % 26)
    else:
        cipher += i

print cipher.encode('hex')

# https://www.wikiwand.com/en/Affine_cipher flag是一个有意义的句子
# cipher = 1917090506070905195f07065f06031505195f035f0a07065f170c5f1407170205101105