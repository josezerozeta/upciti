import time

from src.model.frame_vector import FrameVector
from src.topic import Topic
from src.manager import Manager
from src.consumer import Consumer, Peeker
from src.producer import Producer
from concurrent.futures import ThreadPoolExecutor

from src.model import motion_vector, detection_vector


def main():
    manager = Manager()

    motion_vector_topic = Topic('Motion Vector')
    detection_vector_topic = Topic('Detection Vector')

    with ThreadPoolExecutor() as executor:
        executor.submit(create_motion_detector(manager, motion_vector_topic).produce)
        executor.submit(create_single_shot_detector(manager, motion_vector_topic, detection_vector_topic).consume)
        executor.submit(create_logger(manager, motion_vector_topic, detection_vector_topic).consume)


def create_motion_detector(manager: Manager, motion_vector_topic: Topic) -> Producer:
    motion_detector = Producer('Motion Detector', manager)

    def message_generator():
        # simulate some work time
        time.sleep(0.001)
        return motion_vector.random_generator()

    manager.register_producer(motion_detector, motion_vector_topic, message_generator)
    return motion_detector


def create_single_shot_detector(manager: Manager, motion_vector_topic: Topic, detection_vector_topic: Topic) -> Peeker:
    single_shot_detector = Peeker('Single Shot Detector', manager)

    def process_message(message: FrameVector):
        # simulate some work time
        time.sleep(0.001)
        detection_vector_topic.put_message(detection_vector.random_generator(message))

    manager.register_consumer(single_shot_detector, motion_vector_topic, process_message)
    return single_shot_detector


def create_logger(manager: Manager, motion_vector_topic: Topic, detection_vector_topic: Topic) -> Consumer:
    logger = Consumer('Logger', manager)
    manager.register_consumer(logger, motion_vector_topic, print)
    manager.register_consumer(logger, detection_vector_topic, print)
    return logger


if __name__ == '__main__':
    main()
