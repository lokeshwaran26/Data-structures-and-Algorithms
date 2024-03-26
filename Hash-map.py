class Hashmap:
    def __init__(self):
        self.Max = 100
        self.arr = [None for i in range(self.Max)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.Max

    def add(self, key, value):  # ------------> __setitem__
        h = self.get_hash(key)
        self.arr[h] = value
        print(self.arr)

    def get(self, key):  # --------->__getitem__
        h = self.get_hash(key)
        print(self.arr[h])

    def delete(self, key): #-------> __delitem__
        h = self.get_hash(key)
        self.arr[h] = None

    def delete2(self, key): #-------> __delitem__
        h = self.get_hash(key)
        self.arr[h] = None


t = Hashmap()
t.add('march 6', 240) #------> t['march 6'] = 240
t.get('march 6')
