import sys


def convert(s):
    s=list(s)
    for i in range(len(s)):
        if 'a' <= s[i] <= 'z':
            s[i] = chr(ord(s[i]) - 32)
        elif 'A' <= s[i] <= 'Z':
            s[i] = chr(ord(s[i]) + 32)
        else:
            s[i] = '*'
    print("".join(s))


for line in sys.stdin:
    arr = line[:-1]
res = convert(arr)
