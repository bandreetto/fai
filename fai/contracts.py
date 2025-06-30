from typing import Literal


Nucleotide = Literal["A", "C", "G", "T"]
FlankerPosition = Literal[0, 1, 2, 3, 4, 5, 6, 7]


class Read:
    gene_id: str
    gene_position: int
    size: int
    flankers: list[str]

    def __init__(
        self, gene_id: str, gene_position: int, size: int, flankers: list[str] = []
    ) -> None:
        self.gene_id = gene_id
        self.gene_position = gene_position
        self.size = size
        self.flankers = flankers
