import random
from dataclasses import dataclass
from datetime import datetime
from abc import ABC


@dataclass
class BoundingBox:
    x: float
    y: float
    width: int
    height: int

    @staticmethod
    def random_generator():
        return BoundingBox(random.uniform(0, 100), random.uniform(0, 100),
                           random.randint(0, 100), random.randint(0, 100))


@dataclass
class FrameVector(ABC):
    timestamp: datetime
    frame_id: int
    bounding_box: BoundingBox
