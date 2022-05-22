from manager import Manager


class Consumer:

    def __init__(self, name: str, manager: Manager):
        self.__name = name
        self.__manager = manager

    def consume(self):
        while True:
            self.__manager.consume(self)

    def __str__(self) -> str:
        return 'name: ' + self.__name + ', manager: ' + str(self.__manager)