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
min_heap.print_sort()
