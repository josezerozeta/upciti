import threading
import unittest

from src.topic import Topic
from src.manager import Manager
from src.producer import Producer
from concurrent.futures import ThreadPoolExecutor


class TestProducer(unittest.TestCase):

    def test_produce_message(self):
        manager = Manager()
        topic = Topic('topic')
        producer = Producer('producer', manager)
        event = threading.Event()

        def message_generator() -> str:
            event.set()
            return 'test'

        manager.register_producer(producer, topic, message_generator)

        with ThreadPoolExecutor() as executor:
            executor.submit(producer.produce)
            event.wait()
            producer.stop()

        self.assertEqual(topic.get_message(), 'test')


if __name__ == '__main__':
    unittest.main()
