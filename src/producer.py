from src.manager import Manager


class Producer:

    def __init__(self, name: str, manager: Manager):
        self.__name = name
        self.__manager = manager

    def produce(self):
        while True:
            self.__manager.produce(self)

    def __str__(self) -> str:
        return 'name: ' + self.__name + ', manager: ' + str(self.__manager)
