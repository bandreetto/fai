def read_fasta(file_name, delimiter):
    """Read a FASTA file returning the longest valid coding sequence per gene.

    The original implementation loaded the whole file into memory which is
    prohibitive for multi-gigabyte datasets.  We now stream the file line by
    line which keeps the memory footprint small regardless of the file size.
    """

    def _maybe_store_sequence(symbol: str, sequence: str, storage: dict) -> None:
        if not sequence:
            return

        if (
            len(sequence) % 3 == 0
            and sequence.startswith("ATG")
            and sequence[-3:] in stop_codons
        ):
            if symbol not in storage or len(storage[symbol]) < len(sequence):
                storage[symbol] = sequence

    stop_codons = {"TAA", "TAG", "TGA"}
    fasta_dict: dict[str, str] = {}
    gene_symbol: str | None = None
    gene_code_parts: list[str] = []

    with open(file_name, "r", encoding="utf-8") as fasta_file:
        for raw_line in fasta_file:
            line = raw_line.strip()
            if not line:
                continue

            if line.startswith(">"):
                if gene_symbol is not None:
                    gene_code = "".join(gene_code_parts)
                    _maybe_store_sequence(gene_symbol, gene_code, fasta_dict)

                gene_code_parts = []
                try:
                    gene_symbol = line.split(delimiter, 1)[1].split(" ", 1)[0]
                except IndexError:
                    gene_symbol = "none"
            else:
                gene_code_parts.append(line)

    if gene_symbol is not None:
        gene_code = "".join(gene_code_parts)
        _maybe_store_sequence(gene_symbol, gene_code, fasta_dict)

    return fasta_dict
