import heapq

h = [1,-2,3,4]

heapq.heapify(h)
print(h)

h2 = list(map(lambda x: x * (-1), h))
heapq.heapify(h2)
print(h2)