def read_fasta(file_name, delimiter):
    """fasta_file:object, from open() function
    delimiter:str, modifier that designates any type of information in
    the fasta definition line.
    suggested delimiters: "gene_id=", "transcript_id=", "protein_name="
    """
    stop_codons = ("TAA", "TAG", "TGA")
    fasta_file = open(file_name, "r")
    fasta_list = fasta_file.read().split("\n")
    fasta_dict = {}
    first_line = True
    gene_code = ""
    gene_symbol = ""
    for line in fasta_list:
        if len(line) == 0:
            continue
        if line[0] == ">":
            if first_line:
                first_line = False
            else:
                if (
                    (len(gene_code) % 3 == 0)
                    and (gene_code[0:3] == "ATG")
                    and (gene_code[-3:0] not in stop_codons)
                ):
                    # input in dict only if its len is multiple of 3 (codon length)
                    # input in dict only if code starts in ATG
                    # input in dict only if code ends in a stop codon

                    if gene_symbol not in fasta_dict:
                        fasta_dict[gene_symbol] = gene_code
                    # input in dict only if there is no code for current gene
                    elif len(fasta_dict[gene_symbol]) < len(gene_code):
                        fasta_dict[gene_symbol] = gene_code
                    # or replace it if current code is longer than code in the dict.

            try:
                gene_symbol = line.split(delimiter)[1]
                gene_symbol = gene_symbol.split(" ")[0]
            except IndexError:
                gene_symbol = "none"

            gene_code = ""

        else:
            gene_code += line

    fasta_dict[gene_symbol] = gene_code
    return fasta_dict
