#! /bin/python3


class QueueError(IndexError):
    pass


class Queue:
    def __init__(self) -> None:
        self._queue = []

    def put(self, val):
        self._queue.append(val)

    def get(self):
        if len(self._queue) > 0:
            val = self._queue[0]
            del self._queue[0]
            return val
        else:
            raise QueueError


class QueueExtended(Queue):
    def is_empty(self):
        return not self._queue

    def get_size(self):
        return len(self._queue)


society = "superficial people"
my_queue = QueueExtended()
my_queue.put("f*")
my_queue.put(society)

for i in range(5):
    my_queue.put(i)

while not my_queue.is_empty():
    try:
        print(f"Processing: {my_queue.get()}")
    except QueueError as e:
        print(f"Queue Error: {e}")
