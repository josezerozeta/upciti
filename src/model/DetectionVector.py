import sys
import random
from datetime import datetime
from dataclasses import dataclass

from src.model.FrameVector import FrameVector, BoundingBox


@dataclass
class PredictionVector:
    target: str
    accuracy: float

    @staticmethod
    def random_generator():
        return PredictionVector("str", random.uniform(0, 100))


@dataclass(init=True)
class DetectionVector(FrameVector):
    predictionVector: PredictionVector


def random_generator():
    return DetectionVector(datetime.now(),
                           random.randint(1, sys.maxsize),
                           BoundingBox.random_generator(),
                           PredictionVector.random_generator())
