from dataclasses import dataclass, field
from typing import Dict

import scipy.sparse as sp

from .node import Node
from .edge import Edge


@dataclass(slots=True)
class Graph:

    nodes: Dict[int, Node] = field(default_factory=dict)

    edges: list[Edge] = field(default_factory=list)

    W: sp.csr_matrix | None = None

    D: sp.csr_matrix | None = None

    L: sp.csr_matrix | None = None
