from fai.read import Read


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


def get_flankers(gene_position: int, gene_size: int, gene_sequence: str) -> list[str]:
    leading_flankers_starting_index = gene_position - 3
    leading_flankers = [
        gene_sequence[leading_flankers_starting_index + i] for i in range(4)
    ]

    trailing_flankers_starting_index = leading_flankers_starting_index + gene_size
    trailing_flankers = [
        gene_sequence[trailing_flankers_starting_index + i] for i in range(4)
    ]

    return leading_flankers + trailing_flankers
