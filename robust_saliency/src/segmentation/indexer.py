"""
segmenter/indexer.py

Efficient utilities for indexing SLIC superpixels.

Author:
    Your Name

"""

from __future__ import annotations

from dataclasses import dataclass
import numpy as np


@dataclass(slots=True)
class SegmentIndex:
    """
    Stores all pixel coordinates belonging to one superpixel.

    Parameters
    ----------
    label:
        Superpixel label.

    rows:
        Row indices.

    cols:
        Column indices.
    """

    label: int

    rows: np.ndarray

    cols: np.ndarray

    @property
    def area(self) -> int:
        """Number of pixels inside the superpixel."""
        return len(self.rows)


class SegmentIndexer:
    """
    Builds an index of every superpixel.

    Example
    -------
    >>> indexer = SegmentIndexer()
    >>> indices = indexer.build(segments)
    >>> indices[12].rows
    >>> indices[12].cols
    """

    def build(
        self,
        segments: np.ndarray,
    ) -> list[SegmentIndex]:

        if segments.ndim != 2:
            raise ValueError("segments must be a 2D array.")

        num_segments = int(segments.max()) + 1

        indices: list[SegmentIndex] = []

        for label in range(num_segments):

            rows, cols = np.where(segments == label)

            indices.append(
                SegmentIndex(
                    label=label,
                    rows=rows,
                    cols=cols,
                )
            )

        return indices
