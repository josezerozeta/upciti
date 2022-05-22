import queue


class Topic:

    def __init__(self, name: str, size=10):
        self.__name = name
        self.__queue = queue.Queue(size)

    def put_message(self, message: str):
        self.__queue.put(message)

    def get_message(self) -> str:
        return self.__queue.get(True)

    def __str__(self) -> str:
        return 'name: ' + self.__name + ', queue: ' + str(self.__queue)
