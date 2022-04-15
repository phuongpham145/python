from collections import defaultdict
from queue import PriorityQueue
data = defaultdict(list)
data['A'] = ['B', 'C', 'D', 6]
data['B'] = ['E', 'F', 3]
data['C'] = ['G', 'H', 4]
data['D'] = ['I', 'J', 5]
data['F'] = ['K', 'L', 'M', 1]
data['H'] = ['N', 'O', 2]
data['E'] = [3]
data['G'] = [6]
data['I'] = [5]
data['J'] = [4]
data['K'] = [2]
data['L'] = [0]
data['M'] = [4]
data['N'] = [0]
data['O'] = [4]


class Node:
    def __init__(self, name, parent=None, h=0):
        self.name = name
        self.parent = parent
        self.h = h

    def display(self):
        print(self.name, self.h)

    def __lt__(self, other):
        if other == None:
            return False
        return self.h < other.h

    def __eq__(self, other):
        if other == None:
            return False
        return self.name == other.name


def equal(O, G):
    if O.name == G.name:
        return True
    return False


def checkInPriority(tmp, c):
    if tmp == None:
        return False
    return(tmp in c.queue)


def getPath(O, distance):
    print(O.name)
    distance += O.h
    if O.parent != None:
        getPath(O.parent, distance)
    else:
        print('Distance: ', distance)
        return


def BestFirstSearch(S=Node('A'), G=Node('N')):
    Open = PriorityQueue()
    Closed = PriorityQueue()
    S.h = data[S.name][-1]
    Open.put(S)
    while True:
        if Open.empty() == True:
            print('Tim kiem that bai')
            return
        O = Open.get()
        Closed.put(O)
        print('Duyet : ', O.name, O.h)
        if equal(O, G) == True:
            print('Tim kiem thanh cong')
            distance = 0
            getPath(O, distance)
            return
        i = 0
        while i < len(data[O.name]) - 1:
            name = data[O.name][i]
            h = data[name][-1]
            tmp = Node(name=name, h=h)
            tmp.parent = O
            ok1 = checkInPriority(tmp, Open)
            ok2 = checkInPriority(tmp, Closed)
            if not ok1 and not ok2:
                Open.put(tmp)
            i += 1


BestFirstSearch()
