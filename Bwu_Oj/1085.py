flag = [0] * 10
for a in range(1, 10):
    for b in range(0, 10):
        for c in range(1, 10):
            num1 = a * 100 + b * 10 + c
            num2 = c * 100 + b * 10 + a
            if num1 + num2 == 1333 and (flag[a] != 1 or flag[c]!=1):
                flag[a] = 1
                flag[c] = 1
                if a > c:
                    print("{}+{}=1333".format(num2, num1))
                    print("{}+{}=1333".format(num1, num2))
                else:
                    print("{}+{}=1333".format(num1, num2))
                    print("{}+{}=1333".format(num2, num1))

