import queue

from src.PeekQueue import PeekQueue
from src.model.frame_vector import FrameVector


class Topic:
    """Topic where messages are published"""

    def __init__(self, name: str, size=10):
        self.__name = name
        self.__queue = PeekQueue(size)

    def put_message(self, message: FrameVector, block=True):
        """put a message in the topic"""
        try:
            self.__queue.put(message, block, timeout=1)
        except queue.Full:
            pass

    def get_message(self, block=True) -> FrameVector:
        """get a message from the topic"""
        message = None
        while not message:
            try:
                message = self.__queue.get(block, timeout=1)
            except queue.Empty:
                pass

        return message

    def peek_message(self, block=True):
        """peek a message from the topic"""
        message = None
        while not message:
            try:
                message = self.__queue.peek(block, timeout=1)
            except queue.Empty:
                pass

        return message
