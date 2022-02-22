import heapq
heap = [4, 2, 6, 76, 34, 3, 0, 1, 5, 43]
l1 = [3,2,1,5,7,2]

print(heapq.heappush(heap, 100))

print(heapq.heappop(heap))

print(heapq.heappushpop(heap, -1))

print(heapq.heapreplace(heap, -1))

print(heapq.heapify(heap))

print(heapq.nsmallest(2, heap))
print(heapq.nlargest(3, heap))

print(list(heapq.merge(heap, l1)))


