class MinHeap:
    def __init__(self):
        self.li = []

    def insert(self, val):
        self.li.append(val)
        self._heapify_up(len(self.li) - 1)

    def _heapify_up(self, index):
        parent = (index - 1) // 2
        if index > 0 and self.li[index] < self.li[parent]:
            self.li[index], self.li[parent] = self.li[parent], self.li[index]
            self._heapify_up(parent)
    
    def remove(self):
        if not self.li:
            return None
        if len(self.li) == 1:
            return self.li.pop()
        self.li[0] = self.li.pop()
        self._heapify_down(len(self.li))

    def _heapify_down(self, l, index=0):
        smallest, left, right = index, (2*index) + 1, (2*index) + 2
        if left < l and self.li[left] < self.li[smallest]:
            smallest = left
        if right < l and self.li[right] < self.li[smallest]:
            smallest = right
        if smallest != index:
            self.li[index], self.li[smallest] = self.li[smallest], self.li[index]
            self._heapify_down(l, smallest)
    
    def heap_sort(self):
        for i in range(len(self.li)-1, 0, -1):
            self.li[i], self.li[0] = self.li[0], self.li[i]
            self._heapify_down(i)
        self.li.reverse()
        return self.li




if __name__ == "__main__":
    # Clear the console
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

    # Example usage of MinHeap
    li = [10, 5, 40, 15, 20, 2]
    min_heap = MinHeap()
    for i in li:
        min_heap.insert(i)

    print(min_heap.li)
    print(min_heap.heap_sort())
    # min_heap.remove()

