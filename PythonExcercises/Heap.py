class Heap:
    def __init__(self):
        self.heap_list = []
        self.current_size = 0

    def insert(self, val):
        self.heap_list.append(val)
        self.current_size += 1
        self.percUP(self.current_size-1)

    def percUP(self, i):
        while (1+i)//2 > 0:
            if self.heap_list[i] < self.heap_list[i//2]:
                temp = self.heap_list[i]
                self.heap_list[i] = self.heap_list[i//2]
                self.heap_list[i//2] = temp
            i = i//2

    def print_heap(self):
        for i in self.heap_list:
            print(i)

    def find(self, szukana):
        if self.find_helper(szukana) is None:
            return False
        else:
            return self.find_helper(szukana)

    def find_helper(self, szukana):
        for i in self.heap_list:
            if i == szukana:
                return True


kopiec = Heap()
kopiec.insert(5)
kopiec.insert(7)
kopiec.insert(3)
kopiec.insert(12)
kopiec.insert(2)
kopiec.print_heap()
print(kopiec.find(7))
