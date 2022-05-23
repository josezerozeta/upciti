from src.topic import Topic


class Manager:
    """Manager class that orchestrate the consumer and producer registered"""

    def __init__(self):
        self.__consumers_strategy = {}
        self.__producers_strategy = {}

    def register_consumer(self, consumer, topic: Topic, process_message):
        """
        Register a consumer with a strategy to process the messages

        :param consumer: the consumer to be registered
        :param topic: the target topic
        :param process_message: the process message strategy
        """
        self.__consumers_strategy.setdefault(consumer, set())
        self.__consumers_strategy[consumer].add((topic, process_message))

    def register_producer(self, producer, topic: Topic, message_generator):
        """
        Register a producer with a strategy to generate messages

        :param producer: the producer to be registered
        :param topic: the tqrget topic
        :param message_generator: the message generator
        """
        self.__producers_strategy.setdefault(producer, set())
        self.__producers_strategy[producer].add((topic, message_generator))

    def consume(self, consumer):
        """
        The consumer target consumes messages from all the topics in which it has been registered
        and applies the process message strategy for each topic

        :param consumer: consumer target
        """
        for (topic, process_message) in self.__consumers_strategy[consumer]:
            message = topic.get_message()
            process_message(message)

    def peek(self, consumer):
        """
        The consumer target peeks messages from all the topics in which it has been registered
        and applies the process message strategy for each topic

        :param consumer: consumer target
        """
        for (topic, process_message) in self.__consumers_strategy[consumer]:
            message = topic.peek_message()
            process_message(message)

    def produce(self, producer):
        """
        The producer target produce messages to all the topics in which it has been registered
        and applies the message generator strategy for each topic

        :param producer: producer target
        """
        for (topic, message_generator) in self.__producers_strategy[producer]:
            topic.put_message(message_generator())
