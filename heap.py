class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, val):
        self.heap.append(val)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        parent = (index - 1) // 2
        if index > 0 and self.heap[index] < self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self._heapify_up(parent)
    
    def remove(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)

    def _heapify_down(self, index):
        smallest = index
        left = 2 * index + 1
        right = 2 * index + 2
        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)
    
    def print_sort(self):
        temp = []
        while len(self.heap) > 0:
            temp.append(self.remove())
        print(temp)


min_heap = MinHeap()
min_heap.insert(10)
min_heap.insert(5)
min_heap.insert(20)
min_heap.insert(2)

print(min_heap.heap)
# min_heap.remove()
# print(min_heap.heap)
# min_heap.print_sort()


def heapify(arr, l, index):
    smallest = index
    left = 2 * index + 1
    right = 2 * index + 2
    if left < l and arr[left] < arr[smallest]:
        smallest = left
    if right < l and arr[right] < arr[smallest]:
        smallest = right
    if smallest != index:
        arr[index], arr[smallest] = arr[smallest], arr[index]
        heapify(arr, l, smallest)

def heap_sort(arr):
    l = len(arr)
    for i in range(l//2-1, -1, -1):
        heapify(arr, l, i)
    for i in range(l-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


arr = [4, 10, 3, 5, 1]
heap_sort(arr)
print(arr)
