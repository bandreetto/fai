from collections import defaultdict
from fai.consts import DELTA_RANGE, START_CODON_OFFSET, STOP_CODON_OFFSET
from fai.contracts import Read


def add_flankers_to_reads(reads: list[Read], gene_dict: dict) -> list[Read]:
    reads_and_genes = [[read, gene_dict.get(read.gene_id)] for read in reads]

    if any(gene is None for _, gene in reads_and_genes):
        raise ValueError(
            "One or more gene IDs in reads do not match any key in gene_dict."
        )

    return [
        Read(
            read.gene_id,
            read.gene_position,
            read.size,
            get_flankers(read.gene_position, read.size, gene_sequence),
        )
        for [read, gene_sequence] in reads_and_genes
    ]


def get_flankers(gene_position: int, read_size: int, gene_sequence: str) -> list[str]:
    if len(gene_sequence) < gene_position + read_size + 2:
        raise ValueError(
            "Gene sequence is shorter than the specified gene position, size and flankers."  # noqa: E501
        )

    leading_flankers = gene_sequence[gene_position - 2 : gene_position + 2]

    read_end_position = gene_position + read_size
    trailing_flankers = gene_sequence[read_end_position - 2 : read_end_position + 2]

    return [nt for nt in leading_flankers + trailing_flankers]


def map_valid_A_site_positions_for_read(read: Read, gene_dict: dict) -> list[bool]:
    read_gene_indexes = [read.gene_position + i for i in range(read.size)]

    cds_size = len(gene_dict[read.gene_id]) - (START_CODON_OFFSET + STOP_CODON_OFFSET)

    gene_cds_indexes = [index - START_CODON_OFFSET for index in read_gene_indexes]

    valid_A_site_positions = [
        index >= 0 and index < cds_size and index % 3 == 0 for index in gene_cds_indexes
    ]

    return valid_A_site_positions


def calculate_delta(reads: list[Read], gene_dict: dict) -> int:
    read_sizes = {read.size for read in reads}
    if len(read_sizes) > 1:
        raise ValueError("All reads must have the same size.")

    valid_A_site_positions = [
        map_valid_A_site_positions_for_read(read, gene_dict) for read in reads
    ]

    deltas_dict = {
        sum(
            [
                valid_A_site_position[delta]
                for valid_A_site_position in valid_A_site_positions
            ]
        ): delta
        for delta in DELTA_RANGE
    }

    max_valid_reads = max(deltas_dict.keys())

    return deltas_dict[max_valid_reads] + 1  # deltas should start on 1 and not 0


def calculate_deltas_by_subset(reads: list[Read], gene_dict: dict) -> dict[str, int]:
    if not all(len(read.flankers) == 8 for read in reads):
        raise ValueError("All reads must have flankers")

    reads_by_subset = defaultdict(list)
    for read in reads:
        for flanker in range(8):
            subset = f"{read.size}:F{flanker}:{read.flankers[flanker]}"
            reads_by_subset[subset].append(read)

    deltas_by_subset = {
        subset: calculate_delta(reads_by_subset[subset], gene_dict)
        for subset in reads_by_subset
    }

    return deltas_by_subset
