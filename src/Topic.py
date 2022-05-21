import queue


class Topic:

    def __init__(self, size=10):
        self.queue = queue.Queue(size)

    def put_message(self, message: str):
        self.queue.put(message)

    def get_message(self) -> str:
        return self.queue.get(True)
