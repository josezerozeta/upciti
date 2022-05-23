import threading
import unittest

from src.model import motion_vector
from src.model.frame_vector import FrameVector
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
        test = motion_vector.random_generator()

        def message_generator() -> FrameVector:
            event.set()
            return test

        manager.register_producer(producer, topic, message_generator)

        with ThreadPoolExecutor() as executor:
            executor.submit(producer.produce)
            event.wait()
            producer.stop()

        self.assertEqual(topic.get_message(), test)


if __name__ == '__main__':
    unittest.main()
