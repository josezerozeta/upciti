import sys
import random
from datetime import datetime
from dataclasses import dataclass

from src.model.FrameVector import FrameVector, BoundingBox


@dataclass
class VelocityVector:
    velocityX: float
    velocityY: float

    @staticmethod
    def random_generator():
        return VelocityVector(random.uniform(-20, 20), random.uniform(-20, 20))


@dataclass(init=True)
class MotionVector(FrameVector):
    velocity: VelocityVector


def random_generator():
    return MotionVector(datetime.now(),
                        random.randint(1, sys.maxsize),
                        BoundingBox.random_generator(),
                        VelocityVector.random_generator())
