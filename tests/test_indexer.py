import numpy as np

from rsr.segmentation.indexer import SegmentIndexer


def test_segment_indexer():

    segments = np.array(
        [
            [0, 0, 1],
            [0, 2, 2],
            [3, 3, 2],
        ]
    )

    indexer = SegmentIndexer()

    indices = indexer.build(segments)

    assert len(indices) == 4

    assert indices[0].area == 3

    assert indices[1].area == 1

    assert indices[2].area == 3

    assert indices[3].area == 2
