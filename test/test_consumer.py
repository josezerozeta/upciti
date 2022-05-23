import threading
import unittest

from src.model import motion_vector
from src.topic import Topic
from src.manager import Manager
from src.consumer import Consumer, Peeker
from concurrent.futures import ThreadPoolExecutor


class TestConsumer(unittest.TestCase):

    def test_consume_message(self):
        manager = Manager()
        topic = Topic('topic')
        consumer = Consumer('consumer', manager)

        test = motion_vector.random_generator()
        event = threading.Event()
        topic.put_message(test)

        def process_message(message: str):
            event.wait()
            self.assertEqual(message, test)

        manager.register_consumer(consumer, topic, process_message)

        with ThreadPoolExecutor() as executor:
            executor.submit(consumer.consume)
            event.set()
            consumer.stop()

    def test_peek_message(self):
        manager = Manager()
        topic = Topic('topic')
        consumer = Peeker('peeker', manager)

        test = motion_vector.random_generator()
        event = threading.Event()
        topic.put_message(test)

        def process_message(message: str):
            event.wait()
            self.assertEqual(message, test)

        manager.register_consumer(consumer, topic, process_message)

        with ThreadPoolExecutor() as executor:
            executor.submit(consumer.consume)
            event.set()
            consumer.stop()

        self.assertEqual(topic.get_message(), test)


if __name__ == '__main__':
    unittest.main()
