import threading

from src.manager import Manager


class Producer:
    """Class implementing a producer task

    Produce messages to a target, the producer need to be registered
    in a Manager with the target topic and a strategy to generate messages
    """

    def __init__(self, name: str, manager: Manager):
        self.__name = name
        self.__manager = manager
        self.__stopped = threading.Event()

    def produce(self):
        """start producing messages"""
        while not self.__stopped.is_set():
            self.__manager.produce(self)

        print(f'Stopping producer {self.__name}')

    def stop(self):
        """stop method to kill the task"""
        self.__stopped.set()

    def is_stopped(self) -> bool:
        """
        :return: true is the producer stopped
        """
        return self.__stopped.is_set()

    def get_manager(self):
        """return the manager"""
        return self.__manager
