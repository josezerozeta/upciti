from src.Topic import Topic
from src.Manager import Manager
from src.Consumer import Consumer
from src.Producer import Producer
from concurrent.futures import ThreadPoolExecutor

from src.model import MotionVector, DetectionVector


def main():
    manager = Manager()

    motion_vector = Topic('Motion Vector')
    detection_vector = Topic('Detection Vector')

    with ThreadPoolExecutor() as executor:
        executor.submit(create_motion_detector(manager, motion_vector).produce)
        executor.submit(create_single_shot_detector(manager, motion_vector, detection_vector).consume)
        executor.submit(create_logger(manager, motion_vector, detection_vector).consume)


def create_motion_detector(manager: Manager, motion_vector: Topic) -> Producer:
    motion_detector = Producer('Motion Detector', manager)
    manager.register_producer(motion_detector, motion_vector, MotionVector.random_generator)
    return motion_detector


def create_single_shot_detector(manager: Manager, motion_vector: Topic, detection_vector: Topic) -> Consumer:
    single_shot_detector = Consumer('Single Shot Detector', manager)
    manager.register_consumer(
        single_shot_detector,
        motion_vector,
        lambda message: detection_vector.put_message(DetectionVector.random_generator()))
    return single_shot_detector


def create_logger(manager: Manager, motion_vector: Topic, detection_vector: Topic) -> Consumer:
    logger = Consumer('Logger', manager)
    manager.register_consumer(logger, motion_vector, print)
    manager.register_consumer(logger, detection_vector, print)
    return logger


if __name__ == "__main__":
    main()
