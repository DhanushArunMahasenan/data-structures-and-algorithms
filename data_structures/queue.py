class Queue:

    def __init__(self):
        self.queue = []

    #enqueue
    def enqueue(self, element):
        self.queue.append(element)

    #dequeue
    def dequeue(self):
        if len(self.queue) > 0:
            return self.queue.pop(0)
        
        else:
            return "Under flow"

    #peek
    def peek(self):
        return self.queue[0]

    #display
    def display(self):
        return self.queue


testQueue = Queue()

testQueue.enqueue(5)
testQueue.enqueue(10)
testQueue.enqueue(4)

testQueue.dequeue()
print(testQueue.peek())

print(testQueue.display())