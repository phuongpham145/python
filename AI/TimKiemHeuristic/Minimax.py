import copy


class State:
    def __init__(self, data=None, N=3):
        self.data = data
        self.N = N

    def clone(self):
        sn = copy.deepcopy(self)
        return sn

    def Print(self):
        sz = self.N
        for i in range(sz):
            for j in range(sz):
                tmp = self.data[i*sz+j]
                if tmp == 0:
                    print('_', end='')
                elif tmp == 1:
                    print('o', end='')
                else:
                    print('x', end='')
            print()
        print('================================')


class Operate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def Move(self, s):
        x = self.x
        y = self.y
        sz = s.N
        if x < 0 or x >= sz:
            return None
        if y < 0 or y >= sz:
            return None
        if s.data[x * sz + y] != 0:
            return None
        res = 0
        for value in s.data:
            if value != 0:
                res += 1
        sn = s.clone()
        if res % 2 == 0:
            sn.data[x * sz + y] = 1
        else:
            sn.data[x * sz + y] = 2
        return sn


def isEndNode(s):
    sz = s.N
    data = s.data
    for i in range(sz):
        if data[i * sz + 0] != 0 and data[i * sz + 0] == data[i * sz + 1] and data[i * sz + 0] == data[i * sz + 2]:
            return True
        if data[0*sz + i] != 0 and data[0 * sz + i] == data[1 * sz + i] and data[0 * sz + i] == data[2*sz + i]:
            return True
    if data[0*sz + 0] != 0 and data[0 * sz + 0] == data[1 * sz + 1] and data[0 * sz + 0] == data[2 * sz + 2]:
        return True
    if data[0*sz + 2] != 0 and data[0 * sz + 2] == data[1 * sz + 1] and data[0 * sz + 2] == data[2 * sz + 0]:
        return True
    for value in data:
        if value == 0:
            return False
    return True


def Win(s):
    if s.data == None:
        return False
    sz = s.N
    data = s.data
    for i in range(sz):
        if data[i * sz + 0] != 0 and data[i * sz + 0] == data[i * sz + 1] and data[i * sz + 0] == data[i * sz + 2]:
            return True
        if data[0*sz + i] != 0 and data[0 * sz + i] == data[1 * sz + i] and data[0 * sz + i] == data[2*sz + i]:
            return True
    if data[0*sz + 0] != 0 and data[0 * sz + 0] == data[1 * sz + 1] and data[0 * sz + 0] == data[2 * sz + 2]:
        return True
    if data[0*sz + 2] != 0 and data[0 * sz + 2] == data[1 * sz + 1] and data[0 * sz + 0] == data[2 * sz + 0]:
        return True
    for value in data:
        if value == 0:
            return False
    return True


def checkMyTurn(s):
    res = 0
    for x in s.data:
        if x == 0:
            res += 1
    if res % 2 == 0:
        return True
    return False


def Value(s):
    if Win(s):
        if checkMyTurn(s):
            return 1
        return -1
    return 0


def AlphaBeta(s, d, a, b, mp):
    if isEndNode(s) or d == 0:
        return Value(s)
    sz = s.N
    if mp == True:
        for i in range(sz):
            for j in range(sz):
                child = Operate(i, j).Move(s)
                if child == None:
                    continue
                tmp = AlphaBeta(child, d - 1, a, b, False)
                a = max(a, tmp)
                if a >= b:
                    break
        return a
    else:
        for i in range(sz):
            for j in range(sz):
                child = Operate(i, j).Move(s)
                if child == None:
                    continue
                tmp = AlphaBeta(child, d - 1, a, b, True)
                b = min(b, tmp)
                if a >= b:
                    break
        return b


def Minimax(s, d, mp):
    return AlphaBeta(s, d, -2, 2, mp)


def RUN():
    player = 1
    turn = 0
    s = State(data=[0, 0, 0, 0, 0, 0, 0, 0, 0])
    s.Print()
    while True:
        if turn % 2 + 1 == player:
            child = None
            while child == None:
                print('Please input coordinate')
                x = (int)(input())
                y = (int)(input())
                child = Operate(x, y).Move(s)
            s = child
            if Win(s):
                print('Player wins')
                break
            else:
                mn = 2
                minChild = None
                sz = s.N
                for i in range(sz):
                    for j in range(sz):
                        child = Operate(i, j).Move(s)
                        if child == None:
                            continue
                        tmp = Minimax(child, 1, True)
                        print(i, j, tmp)
                        if mn > tmp:
                            mn = tmp
                            minChild = child
                s = minChild
                s.Print()
                if Win(s):
                    s.Print()
                    print('AI won')
                    break
            s.Print()
            if isEndNode(s):
                print('Draw')
                break
            turn += 1


RUN()
