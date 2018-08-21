import hashlib
import time


def get_as_cp(now):
    zz ={}
    # now = round(time.time())
    # print now
    e = hex(int(now)).upper()[2:]
    # print e
    i = hashlib.md5(str(int(now)).encode('utf-8')).hexdigest().upper()
    if len(e) != 8:
        zz = {'as': "479BB4B7254C150",
            'cp': "7E0AC8874BB0985"}
        return zz
    n = i[:5]
    a = i[-5:]
    r = ""
    s = ""
    for i in range(5):
        s = s+n[i]+e[i]
    for j in range(5):
        r = r+e[j+3]+a[j]
    zz = {
            'as': "A1" + s + e[-3:],
            'cp': e[0:3] + r + "E1"
        }
    # print zz

    return zz


if __name__ == "__main__":
    get_as_cp(time.time())
