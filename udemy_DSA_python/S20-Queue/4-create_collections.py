from collections import deque
customQueue=deque(maxlen=3) # maxlen é opcional
print(customQueue)
customQueue.append(1)
customQueue.append(2)
customQueue.append(3)
print(customQueue)
customQueue.append(4) # substitui o primeiro elemento, já que a capacidade maxima é 3
print(customQueue)
print(customQueue.popleft()) # dequeue
print(customQueue)
print(customQueue.clear())
print(customQueue)