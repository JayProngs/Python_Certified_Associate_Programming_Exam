class QueueError(BaseException):
    pass


class Queue:
    def __init__(self):
        self.queue = []

    def put(self, elem):
        self.queue.append(elem)

    def get(self):
        if len(self.queue) > 0:
            elem = self.queue[0]
            del self.queue[0]
            return elem
        else:
            raise QueueError


class myQueue(Queue):
    def __init__(self):
        Queue.__init__(self)
        self.__flag = False

    def isEmpty(self):
        if len(self.queue) > 0:
            return False
        else:
            return True


que = myQueue()
que.put(1)
que.put("dog")
que.put(False)
try:
    for i in range(5):
        if que.isEmpty():
            print('Queue Empty')
        else:
            print(que.get())
except:
    print("Queue error")