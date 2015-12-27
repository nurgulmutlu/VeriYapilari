class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

n = Stack()

def hanoi(n,kaynak,ara,hedef):
    if n > 0:
        hanoi(n-1, kaynak,ara,hedef)
        if kaynak:
            hedef.append(kaynak.pop())
        hanoi(n-1, ara, kaynak ,hedef)

kaynak = [15,14,13,12,12,11,10,9,8,7,6,5,4,3,2,1]
hedef= []
ara= []

hanoi (len(kaynak),kaynak, ara, hedef)

print(kaynak, ara, hedef)

