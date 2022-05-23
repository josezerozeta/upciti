import threading

from src.manager import Manager


class Consumer:
    """Class implementing a consumer task

    Consume messages from a topic, the consumer need to be registered
    in a Manager with the target topic and a strategy to process the messages
    """

    def __init__(self, name: str, manager: Manager):
        self.__name = name
        self.__manager = manager
        self.__stopped = threading.Event()

    def consume(self):
        """start to consume messages"""
        while not self.__stopped.is_set():
            self.__manager.consume(self)

        print(f'Stopping consumer {self.__name}')

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


class Peeker(Consumer):

    def consume(self):
        """start to peek messages"""
        while not self.is_stopped():
            self.get_manager().peek(self)
