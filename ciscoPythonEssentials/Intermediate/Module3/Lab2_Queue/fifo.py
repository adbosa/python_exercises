class QueueError(IndexError):
    def __init__(self):
        print("Empty queue")

class Queue:
    def __init__(self):
        self.__list = []

    def put(self, elem):
        self.__list.append(elem)

    def get(self):
        try:
            elem = self.__list.pop(0)
            return elem
        except IndexError:
            raise QueueError

    def isEmpty(self):
        if len(self.__list) != 0:
            return False
        else:
            return True
        


### Test ###
if __name__ == "__main__":
    que = Queue()
    que.put(1)
    que.put("dog")
    que.put(False)
    for i in range(4):
        if not que.isEmpty():
            print(que.get())
        else:
            print("Queue empty")
