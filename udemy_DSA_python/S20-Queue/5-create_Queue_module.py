import queue as q

customQueue=q.Queue(maxsize=3) #parametro opcional
print(customQueue.empty())
customQueue.put(1)
customQueue.put(2)
customQueue.put(3)
print(customQueue.qsize())
print(customQueue.full())
print(customQueue.get())
print(customQueue.qsize())