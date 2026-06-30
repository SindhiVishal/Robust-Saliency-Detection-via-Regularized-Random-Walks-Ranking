from abc import ABC
from abc import abstractmethod

import numpy as np


class SuperpixelGenerator(ABC):

    @abstractmethod
    def generate(
        self,
        image: np.ndarray,
    ) -> np.ndarray:
        pass
