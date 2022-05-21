from src.Topic import Topic
from src.Logger import Logger
from src.MotionDetector import MotionDetector
from src.SingleShotDetector import SingleShotDetector
from concurrent.futures import ThreadPoolExecutor


def main():
    motion_vector = Topic()
    detection_vector = Topic()

    with ThreadPoolExecutor() as executor:
        executor.submit(create_motion_detector(motion_vector).produce)
        executor.submit(create_single_shot_detector(motion_vector, detection_vector).consume)
        executor.submit(create_logger(motion_vector, detection_vector).consume)


def create_motion_detector(motion_vector: Topic) -> MotionDetector:
    return MotionDetector(motion_vector)


def create_single_shot_detector(motion_vector: Topic, detection_vector: Topic) -> SingleShotDetector:
    return SingleShotDetector(motion_vector, detection_vector)


def create_logger(motion_vector: Topic, detection_vector: Topic):
    return Logger([motion_vector, detection_vector])


if __name__ == "__main__":
    main()
