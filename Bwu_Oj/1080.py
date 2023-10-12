import sys
import time

def Polymonial(origin, polymonial, opt):
    pl = len(polymonial)
    ol = len(origin)
    for i in range(pl):
        t = polymonial[i]
        if opt[i] == '+':
            for j in range(len(t)):
                if t[j][0] != 0:
                    for k in range(ol):
                        if origin[k][1] == t[j][1]:
                            origin[k][0] += t[j][0]
                            break
                    else:
                        origin.append(t[j])
                        ol += 1
        elif opt[i] == '-':
            for j in range(len(t)):
                if t[j][0] != 0:
                    for k in range(ol):
                        if origin[k][1] == t[j][1]:
                            origin[k][0] -= t[j][0]
                            break
                    else:
                        origin.append(t[j])
                        ol += 1
        else:
            for j in range(len(t)):
                if t[j][0] != 0:
                    for k in range(ol):
                        origin[k][1] += t[j][1]
                        origin[k][0] *= t[j][0]
                else:
                    for k in range(ol):
                        origin[k][0] = 0
        for i in range(ol):
            for j in range(ol - i - 1):
                if origin[j][1] > origin[j + 1][1]:
                    origin[j], origin[j + 1] = origin[j + 1], origin[j]
        flag = 1
        for i in range(ol):
            if origin[i][0] != 0:
                print("{}:{}".format(origin[i][0], origin[i][1]), end=' ')
                flag = 0
        else:
            if flag == 1:
                print("{}:{}".format(0, 0), end=' ')
        print()

t_start=time.time()
k = 0
while True:
    polymonial = []
    opt = []
    for line in sys.stdin:
        temp = line.split()
        if temp[0] == '=':
            k += 1
        opt.append(temp[0])
        polymonial.append(temp[1:])
    if not polymonial:
        break
    l = len(polymonial)
    for i in range(l):
        tmp = polymonial[i]
        y = []
        for j in range(len(tmp)):
            x = tmp[j].split(':')
            x[0] = int(x[0])
            x[1] = int(x[1])
            y.append(x)
        polymonial[i] = y
    origin = polymonial[0]
    print("Case {}".format(k))
    Polymonial(origin, polymonial[1:], opt[1:])
t_end=time.time()
print(t_end-t_start)
