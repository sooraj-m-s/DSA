class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.count = 0
        self.li = [[] for _ in range(self.size)]

    def __get_hashed(self, key):
        index = 0
        for i in str(key):
            index += ord(i)
        return index % self.size
    
    def __rehash(self):
        print("Rehashing...")
        old_data = self.li
        self.size *= 2
        self.li = [[] for _ in range(self.size)]
        for i in old_data:
            for key, val in i:
                self[key] = val

    def __setitem__(self, key, val):
        index = self.__get_hashed(key)
        for i in self.li[index]:
            if i[0] == key:
                i[1] = val
                return
        self.li[index].append([key, val])
        self.count += 1
        if (self.count / self.size) > 0.75:
            self.__rehash()

    def __getitem__(self, key):
        index = self.__get_hashed(key)
        for i in self.li[index]:
            if i[0] == key:
                return i[1]
        raise KeyError(f"{key} not found")

    def __delitem__(self, key):
        index = self.__get_hashed(key)
        for i in self.li[index]:
            if i[0] == key:
                self.li[index].remove(i)
                self.count -= 1
                return
        raise KeyError(f"{key} not found")




if __name__ == '__main__':
    # Clear the console
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

    # Example usage
    h = HashTable()
    h['Name'] = 'Sooraj'
    h['Place'] = 'Pathanamthitta'
    h['Age'] = 20
    del h['Age']
    print(h.li)

