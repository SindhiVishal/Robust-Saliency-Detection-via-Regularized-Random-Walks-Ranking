from dataclasses import dataclass

import numpy as np


@dataclass(slots=True)
class ImageData:

    rgb: np.ndarray

    lab: np.ndarray

    segments: np.ndarray | None = None
