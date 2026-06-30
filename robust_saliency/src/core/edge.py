from dataclasses import dataclass


@dataclass(slots=True)
class Edge:

    source: int

    target: int

    weight: float
