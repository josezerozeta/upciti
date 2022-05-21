from typing import List
from src.Topic import Topic


class Logger:

    def __init__(self, topics_to_consume: List[Topic]):
        self.topics_to_consume = topics_to_consume

    def consume(self):
        while True:
            for topic in self.topics_to_consume:
                print(topic.get_message())
