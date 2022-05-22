import random
from dataclasses import dataclass

from src.model.frame_vector import FrameVector


@dataclass
class PredictionVector:
    target: str
    accuracy: float

    @staticmethod
    def random_generator():
        return PredictionVector(["car", "person", "bicycle"][random.randint(0, 2)], random.uniform(0, 100))


@dataclass(init=True)
class DetectionVector(FrameVector):
    prediction_vector: PredictionVector


def random_generator(frame_vector: FrameVector) -> FrameVector:
    return DetectionVector(frame_vector.timestamp,
                           frame_vector.frame_id,
                           frame_vector.bounding_box,
                           PredictionVector.random_generator())
