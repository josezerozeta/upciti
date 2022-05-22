import random
from dataclasses import dataclass
from datetime import datetime
from abc import ABC


@dataclass
class BoundingBox:
    __x: float
    __y: float
    __width: int
    __height: int

    @staticmethod
    def random_generator():
        return BoundingBox(random.uniform(0, 100), random.uniform(0, 100),
                           random.randint(0, 100), random.randint(0, 100))


@dataclass
class FrameVector(ABC):
    __timestamp: datetime
    __frame_id: int
    __bounding_box: BoundingBox
