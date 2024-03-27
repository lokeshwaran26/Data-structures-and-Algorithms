class Hashmap:
    def __init__(self):
        self.Max = 10
        self.arr = [[] for i in range(self.Max)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.Max

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        # self.arr[h] = value
        # print(self.arr)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key, value)
                found = True
                break
        if not found:
            self.arr[h].append((key,value))

    def __getitem__(self, key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]

    def __delitem__(self, key):
        h = self.get_hash(key)
        for idx, element in enumerate(self.arr[h]):
            if  element[0] == key:
                del self.arr[h][idx] 
                break


t = Hashmap()
t['march 6'] = 120
t['march 6'] = 78
t['march 9'] = 4
t['march 17'] = 440 
del t['march 17']

print(t.arr)


