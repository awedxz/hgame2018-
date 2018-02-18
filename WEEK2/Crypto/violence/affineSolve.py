import gmpy2

a = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]
c = '1917090506070905195f07065f06031505195f035f0a07065f170c5f1407170205101105'.decode('hex')
c = list(c)

def dec(a, b, c):
    m = ''
    for k in c:
        if 96 < ord(k) + 97 < 123:
            m += chr((a * (ord(k) - b) % 26) + 97)
        else:
            m += k
    m = m.split('_')
    if m[3] == 'a' or m[3] == 'i':
        print m

for i in a:
    for j in range(1, 27):
       dec(int(gmpy2.invert(i, 26)), j, c)



