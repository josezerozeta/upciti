from src.topic import Topic


class Manager:
    """Manager class that orchestrate the consumer and producer registered"""

    def __init__(self):
        self.__consumers_strategy = {}
        self.__producers_strategy = {}

    def register_consumer(self, consumer, topic: Topic, process_message):
        """register a consumer with a strategy to process the messages"""
        self.__consumers_strategy.setdefault(consumer, set())
        self.__consumers_strategy[consumer].add((topic, process_message))

    def register_producer(self, producer, topic: Topic, message_generator):
        """register a producer with a strategy to generate messages"""
        self.__producers_strategy.setdefault(producer, set())
        self.__producers_strategy[producer].add((topic, message_generator))

    def consume(self, consumer):
        """the consumer consumes messages to all the topics that has been registered"""
        for (topic, process_message) in self.__consumers_strategy[consumer]:
            message = topic.get_message()
            process_message(message)

    def produce(self, producer):
        """the producer produces messages to all the topics that has been registered"""
        for (topic, message_generator) in self.__producers_strategy[producer]:
            topic.put_message(message_generator())
