from queue import PriorityQueue
class Color:
    def __init__(self, color, weight = 0):
        self.color = color
        self.weight = weight
    def display(self):
        print(self.color, self.weight)
    def __lt__(self, other):
        return self.weight < other.weight
e = Color(weight = 55, color = "Red")
e.display()
c = Color('Blue', 9)
c.display()
d = Color('Green')
d.display()
d.weight = 22
d.display()
q = PriorityQueue()
c1 = Color('Yellow', 12)
c2 = Color('Red', 10)
c3 = Color('Green', 19)
q.put(c1)
q.put(c2)
q.put(c3)
while not q.empty():
    tmp = q.get()
    tmp.display()