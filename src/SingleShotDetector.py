from src.Topic import Topic
from src.model import DetectionVector


class SingleShotDetector:

    def __init__(self, topic_to_consume: Topic, topic_to_produce: Topic):
        self.topic_to_consume = topic_to_consume
        self.topic_to_produce = topic_to_produce

    def consume(self):
        while True:
            self.topic_to_consume.get_message()
            self.produce()

    def produce(self):
        self.topic_to_produce.put_message(DetectionVector.random_generator())
