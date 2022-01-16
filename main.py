# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import time
from random import randint

mxlen = 20


class Point(object):
    # 1 - life. 2 - die
    def __init__(self, type):
        self.type = type


class All(object):
    global mxlen

    def __init__(self):
        self.matrix = []
        for i in range(mxlen):
            self.matrix.append([])
        for i in range(mxlen):
            for j in range(mxlen):
                self.matrix[i].append(Point(randint(0, 1) % 2))

    def next(self):
        matrix = []
        x = [0, 1, 1, 1, 0, -1, -1, -1]
        y = [-1, -1, 0, 1, 1, 1, 0, -1]
        for i in range(mxlen):
            matrix.append([])
        for i in range(mxlen):
            for j in range(mxlen):
                cnt = 0
                matrix[i].append(0)
                for k in range(8):
                    cnt += self.matrix[(i + x[k] + mxlen) % mxlen][(j + y[k] + mxlen) % mxlen].type
                if self.matrix[i][j].type == 1:
                    if 2 <= cnt and 3 >= cnt:
                        matrix[i][j] = 1
                else:
                    if cnt == 3:
                        matrix[i][j] = 1
        for i in range(mxlen):
            for j in range(mxlen):
                self.matrix[i][j].type = matrix[i][j]

    def pr(self):
        for i in range(mxlen):
            for j in range(mxlen):
                print(self.matrix[i][j].type, end='')
            print()


all = All()
while True:
    all.pr()
    all.next()
    time.sleep(1)
    print('\n' * 30)
