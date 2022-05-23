import queue

from src.PeekQueue import PeekQueue
from src.model.frame_vector import FrameVector


class Topic:
    """Topic where messages are published"""

    def __init__(self, name: str, size=10):
        self.__name = name
        self.__queue = PeekQueue(size)

    def put_message(self, message: FrameVector, block=True, timeout=1):
        """put a message in the topic

        If optional args 'block' is true and 'timeout' is None, block if
        necessary until a free slot is available. If 'timeout' is a
        non-negative number (the default), it blocks at most 'timeout'
        seconds and retries till success. Otherwise ('block' is false),
        put the message on the topic if a free slot is immediately available,
        else the message is lost (not recommended)
        """
        try:
            self.__queue.put(message, block, timeout)
        except queue.Full:
            pass

    def get_message(self, block=True, timeout=1) -> FrameVector:
        """get a message from the topic

        If optional args 'block' is true and 'timeout' is None, block if
        necessary until a message is available. If 'timeout' is a non-negative
        number (the default), it blocks at most 'timeout' seconds and retries
        till success. Otherwise ('block' is false), return a message if one
        is immediately available, else return None.
        """
        message = None
        while not message:
            try:
                message = self.__queue.get(block, timeout)
            except queue.Empty:
                pass

        return message

    def peek_message(self, block=True):
        """peek a message from the topic

        If optional args 'block' is true and 'timeout' is None, block if
        necessary until a message is available. If 'timeout' is a non-negative
        number (the default), it blocks at most 'timeout' seconds and retries
        till success. Otherwise ('block' is false), return a message if one
        is immediately available, else return None.
        """
        message = None
        while not message:
            try:
                message = self.__queue.peek(block, timeout=1)
            except queue.Empty:
                pass

        return message
