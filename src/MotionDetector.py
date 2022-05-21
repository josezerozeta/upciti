from src.Topic import Topic
from src.model import MotionVector


class MotionDetector:

    def __init__(self, topic_to_produce: Topic):
        self.topic_to_produce = topic_to_produce

    def produce(self):
        while True:
            self.topic_to_produce.put_message(MotionVector.random_generator())
