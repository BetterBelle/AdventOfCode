from hashlib import md5
init = 'ckczppom'
for i in range(100000000000):
    h = md5((init + str(i)).encode()).hexdigest()
    if h[:6] == '000000': # if h[:5] == '00000': for part 1
        print(h, i)
        break