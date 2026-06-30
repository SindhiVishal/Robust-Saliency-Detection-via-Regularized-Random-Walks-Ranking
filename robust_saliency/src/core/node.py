from dataclasses import dataclass, field

import numpy as np


@dataclass(slots=True)
class Node:

    id: int

    centroid: tuple[float, float]

    mean_rgb: np.ndarray

    mean_lab: np.ndarray

    area: int

    boundary: bool

    neighbors: list[int] = field(default_factory=list)
