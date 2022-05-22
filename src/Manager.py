import Topic


class Manager:

    def __init__(self):
        self.__consumers_strategy = {}
        self.__producers_strategy = {}

    def register_consumer(self, consumer, topic: Topic, process_message):
        self.__consumers_strategy.setdefault(consumer, set())
        self.__consumers_strategy[consumer].add((topic, process_message))

    def register_producer(self, producer, topic: Topic, message_generator):
        self.__producers_strategy.setdefault(producer, set())
        self.__producers_strategy[producer].add((topic, message_generator))

    def consume(self, consumer):
        for (topic, process_message) in self.__consumers_strategy[consumer]:
            process_message(topic.get_message())

    def produce(self, producer):
        for (topic, message_generator) in self.__producers_strategy[producer]:
            topic.put_message(message_generator())
