'''
Design your implementation of the circular queue. The circular queue is a linear data structure in which the operations are performed based on FIFO (First In First Out) principle and the last position is connected back to the first position to make a circle. It is also called "Ring Buffer".

One of the benefits of the circular queue is that we can make use of the spaces in front of the queue. In a normal queue, once the queue becomes full, we cannot insert the next element even if there is a space in front of the queue. But using the circular queue, we can use the space to store new values.

Implementation the MyCircularQueue class:

MyCircularQueue(k) Initializes the object with the size of the queue to be k.
int Front() Gets the front item from the queue. If the queue is empty, return -1.
int Rear() Gets the last item from the queue. If the queue is empty, return -1.
boolean enQueue(int value) Inserts an element into the circular queue. Return true if the operation is successful.
boolean deQueue() Deletes an element from the circular queue. Return true if the operation is successful.
boolean isEmpty() Checks whether the circular queue is empty or not.
boolean isFull() Checks whether the circular queue is full or not.
You must solve the problem without using the built-in queue data structure in your programming language. 
'''

class MyCircularQueue:

    def __init__(self, k: int):
        self.size = k
        self.FRONT = 0
        self.REAR = -1
        self.queue = []
        

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.queue.append(value)
        self.REAR += 1
        return True
        

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.FRONT += 1
        return True
        

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.FRONT]
        

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.REAR]
        

    def isEmpty(self) -> bool:
        if self.FRONT > self.REAR or self.REAR == -1:
            return True
        return False
        

    def isFull(self) -> bool:
        if self.isEmpty():
            return False
        if self.REAR - self.FRONT + 1 >= self.size:
            return True
        return False
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
