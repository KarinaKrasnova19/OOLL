#Вариант №2 (оценка 4)
#Создать базовый класс «список» на основе обычного массива с  функциями вставки и удаления элементов.
#Реализовать на базе списка производные классы стека и очереди.

class MyList:
    def __init__(self):
        self.data = []

    def insert(self, index, value):
        if index < 0 or index > len(self.data):
            raise IndexError("Индекс вне диапазона")
        self.data.insert(index, value)

    def remove(self, value):
        self.data.remove(value)

    def __str__(self):
        return str(self.data)

    def __len__(self):
        return len(self.data)

class Stack(MyList):
    def push(self, value):
        self.insert(len(self.data), value)

    def pop(self):
        if len(self.data) == 0:
            raise IndexError("Стек пуст")
        return self.data.pop()

    def peek(self):
        if len(self.data) == 0:
            raise IndexError("Стек пуст")
        return self.data[-1]

class Queue(MyList):
    def enqueue(self, value):
        self.insert(len(self.data), value)

    def dequeue(self):
        if len(self.data) == 0:
            raise IndexError("Очередь пуста")
        return self.data.pop(0)

    def peek(self):
        if len(self.data) == 0:
            raise IndexError("Очередь пуста")
        return self.data[0]

if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print("Состояние стека:", stack)
    print("Верх стек:", stack.peek())
    print("Выталкиваем элемент:", stack.pop())
    print("Состояние стека после вытаскивания элемента:", stack)

    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print("Состояние очереди:", queue)
    print("Элемент на начале очереди:", queue.peek())
    print("Удаляем элемент из очереди:", queue.dequeue())
    print("Состояние очереди после удаления элемента:", queue)
