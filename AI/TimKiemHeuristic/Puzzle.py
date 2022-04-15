import time
from random import randint
import copy
from collections import defaultdict
from queue import PriorityQueue


class State:
    def __init__(self, data=None, parent=None, g=0, h=0, op=None):
        self.data = data
        self.parent = parent
        self.g = g
        self.h = h
        self.op = op

    def clone(self):
        sn = copy.deepcopy(self)
        return sn

    def Print(self):
        sz = 3
        for i in range(sz):
            for j in range(sz):
                print(self.data[i * sz + j], end=" ")
            print()
        print()

    def Key(self):
        if self.data == None:
            return None
        res = ''
        for x in self.data:
            res += (str)(x)
        return res

    def __lt__(self, other):
        if other == None:
            return False
        return self.g + self.h < other.g + other.h

    def __eq__(self, other):
        if other == None:
            return False
        return self.Key() == other.Key()


class Operator:
    def __init__(self, i):
        self.i = i

    def checkStateNull(self, s):
        return s.data == None

    def findPos(self, s):
        sz = 3
        for i in range(sz):
            for j in range(sz):
                if s.data[i * sz + j] == 0:
                    return i, j
        return None

    def swap(sef, s, x, y, i):
        sz = 3
        sn = s.clone()
        x_new = x
        y_new = y
        if i == 0:
            x_new = x + 1
            y_new = y
        if i == 1:
            x_new = x - 1
            y_new = y
        if i == 2:
            x_new = x
            y_new = y + 1
        if i == 3:
            x_new = x
            y_new = y - 1
        sn.data[x + sz + y] = sn.data[x_new * sz + y_new]
        sn.data[x_new * sz + y_new] = 0

    def Up(self, s):
        if self.checkStateNull(s) == True:
            return None
        x, y = self.findPos(s)
        if x == 2:
            return None
        return self.swap(s, x, y, self.i)

    def Down(self, s):
        if self.checkStateNull(s) == True:
            return None
        x, y = self.findPos(s)
        if x == 0:
            return None
        return self.swap(s, x, y, self.i)

    def Left(self, s):
        if self.checkStateNull(s) == True:
            return None
        x, y = self.findPos(s)
        if y == 2:
            return None
        return self.swap(s, x, y, self.i)

    def Right(self, s):
        if self.checkStateNull(s) == True:
            return None
        x, y = self.findPos(s)
        if y == 0:
            return None
        return self.swap(s, x, y, self.i)

    def Move(self, s):
        if self.i == 0:
            return self.Up(s)
        if self.i == 1:
            return self.Down(s)
        if self.i == 2:
            return self.Left(s)
        if self.i == 3:
            return self.Right(s)
        return None


def checkInPriority(Open, tmp):
    if tmp == None:
        return False
    return (tmp in Open.queue)


def equal(O, G):
    if O == None:
        return False
    return O.Key() == G.Key()


def Path(O):
    if O.parent != None:
        Path(O.parent)
        print(O.op.i)
    O.Print()


def Hx(S, G):
    sz = 3
    res = 0
    for i in range(sz):
        for j in range(sz):
            if S.data[i * sz + j] != G.data[i * sz + j]:
                res += 1
    return res


def RUN():
    Open = PriorityQueue()
    Closed = PriorityQueue()
    Open.put(S)
    S.g = 0
    S.h = Hx(S, G)
    Open.put(S)
    while True:
        if Open.empty() == True:
            print('Tim kiem that bai')
            return
        O = Open.get()
        Closed.put(O)
        if equal(O, G) == True:
            print('Tim thay')
            Path(O)
            return
        for i in range(4):
            op = Operator(i)
            child = op.Move(O)
            if child == None:
                continue
            ok1 = checkInPriority(Open, child)
            ok2 = checkInPriority(Closed, child)
            if not ok1 and not ok2:
                child.parent = O
                child.op = op
                child.g - O.g + 1
                child.h = Hx(child, G)
                Open.put(child)


def init(num):
    G = State()
    sz = 3
    G.data = []
    for i in range(sz):
        for j in range(sz):
            G.data.append((i*sz + j + 1) % 9)
    S = G.clone()
    for i in range(num):
        op = Operator(randint(0, 3))
        tmp = op.Move(S)
        if tmp != None:
            S = tmp
    return S, G


t1 = time.time()
S, G = init(50)
S.Print()
G.Print()
RUN()
t2 = time.time()
print('Time : ', (t2 - t1))
