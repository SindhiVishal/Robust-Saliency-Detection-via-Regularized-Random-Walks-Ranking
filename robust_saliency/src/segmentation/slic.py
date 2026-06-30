from skimage.segmentation import slic

from .base import SuperpixelGenerator


class SLICGenerator(SuperpixelGenerator):

    def __init__(

        self,

        n_segments=300,

        compactness=10,

        sigma=1,

    ):

        self.n_segments = n_segments

        self.compactness = compactness

        self.sigma = sigma

    def generate(self, image):

        return slic(

            image,

            n_segments=self.n_segments,

            compactness=self.compactness,

            sigma=self.sigma,

            start_label=0,

        )
