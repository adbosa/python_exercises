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


### Test ###
if __name__ == "__main__":
    que = Queue()
    que.put(1)
    que.put("dog")
    que.put(False)
    try:
        for i in range(4):
            print(que.get())
    except:
        print("Queue error")

