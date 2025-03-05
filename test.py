from queue import PriorityQueue

a = PriorityQueue()
a.put(1)
a.put(2)
a.put(3)
a.put(4)
a.put(5)
print(a.qsize())

a.get()
a.get()
print(a.qsize())