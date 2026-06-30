from dataclasses import dataclass

import numpy as np


@dataclass(slots=True)
class Image:
    """
    Container for one image.
    """

    rgb: np.ndarray

    lab: np.ndarray

    segments: np.ndarray | None = None

    path: str | None = None
