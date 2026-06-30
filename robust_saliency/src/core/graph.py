from dataclasses import dataclass, field

import scipy.sparse as sp

from .edge import Edge
from .node import Node


@dataclass(slots=True)
class Graph:

    nodes: list[Node] = field(default_factory=list)

    edges: list[Edge] = field(default_factory=list)

    affinity: sp.csr_matrix | None = None

    degree: sp.csr_matrix | None = None

    laplacian: sp.csr_matrix | None = None
