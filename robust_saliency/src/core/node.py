from dataclasses import dataclass, field

import numpy as np


@dataclass(slots=True)
class Node:
    """
    Represents one superpixel.

    Parameters
    ----------
    id
        Superpixel label.

    rows
        Pixel row indices.

    cols
        Pixel column indices.

    centroid
        (row, col)

    mean_rgb
        Mean RGB value.

    mean_lab
        Mean LAB value.

    area
        Number of pixels.

    boundary
        True if touches image border.

    neighbors
        Adjacent superpixel ids.
    """

    id: int

    rows: np.ndarray

    cols: np.ndarray

    centroid: tuple[float, float]

    mean_rgb: np.ndarray

    mean_lab: np.ndarray

    area: int

    boundary: bool

    neighbors: list[int] = field(default_factory=list)
