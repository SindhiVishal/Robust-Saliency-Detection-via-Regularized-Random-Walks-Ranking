from dataclasses import dataclass, field
from typing import List, Tuple

import numpy as np


@dataclass(slots=True)
class Node:
    """
    Represents one superpixel in the graph.
    """

    id: int

    pixel_indices: np.ndarray

    centroid: Tuple[float, float]

    mean_rgb: np.ndarray

    mean_lab: np.ndarray

    area: int

    boundary: bool

    neighbors: List[int] = field(default_factory=list)
