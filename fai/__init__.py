from fai.read import Read


def add_flankers_to_reads(reads: list[Read], gene_dict: dict) -> list[Read]:
    for read in reads:
        gene_sequence = gene_dict.get(read.gene_id)

        if not gene_sequence:
            raise ValueError(f"Gene ID {read.gene_id} not found in gene_dict.")

        if len(gene_sequence) < read.gene_position + read.size - 1:
            raise ValueError(
                f"Gene position overflow: Gene sequence for {read.gene_id} is too short"
                " for the read position and size."
            )

        leading_flankers_starting_index = read.gene_position - 3
        leading_flankers = [
            gene_sequence[leading_flankers_starting_index + i] for i in range(4)
        ]

        trailing_flankers_starting_index = leading_flankers_starting_index + read.size
        trailing_flankers = [
            gene_sequence[trailing_flankers_starting_index + i] for i in range(4)
        ]

        read.flankers = leading_flankers + trailing_flankers

    return reads
