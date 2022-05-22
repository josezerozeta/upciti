import threading

from src.manager import Manager


class Consumer:

    def __init__(self, name: str, manager: Manager):
        self.__name = name
        self.__manager = manager
        self.__stopped = threading.Event()

    def consume(self):
        while not self.__stopped.is_set():
            self.__manager.consume(self)

    def stop(self):
        self.__stopped.set()
