import heapq

items = []

heapq.heappush(items, (1, "hello sam"))
heapq.heappush(items, (3, "hello tim"))
heapq.heappush(items, (13, "hello scab"))
heapq.heappush(items, (5, "hello lars"))
heapq.heappush(items, (2, "hello s"))

# for i in items:
#     print(i)

while items:
    a = heapq.heappop(items)
    print(a)
