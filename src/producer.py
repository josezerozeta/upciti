import threading

from src.manager import Manager


class Producer:

    def __init__(self, name: str, manager: Manager):
        self.__name = name
        self.__manager = manager
        self.__stopped = threading.Event()

    def produce(self):
        while not self.__stopped.is_set():
            self.__manager.produce(self)

    def stop(self):
        self.__stopped.set()
