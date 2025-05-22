from fai.fai import add_flankers_to_read
from fai.fai.read import Read


def test_add_flankers_to_read():
    reads = [
        Read("gene1", 5, 30),
        Read("gene2", 10, 33),
        Read("gene3", 15, 28),
    ]
    fasta_dict = {
        "gene1": "CCTCAGCCTCACCCTTACTCCTTGCCCCAGTTCATCGCCCCCGATGGGTCTAGTCACCAATCAGCCACGCGTCAGGTCAT",  # noqa: E501
        "gene2": "GCTCACTCATACTACACGAAGCAGTCGGCCGAATCCTCCGCACCCTGGGGGTCTCTCAACTCCGTGTGAAAAGTTCCTAT",  # noqa: E501
        "gene3": "CACCGCTTCCCCCTGCGAGCGGTGTCGCCAGGTTGAGCGTATGATGTCAGGTCTTTCAATATCATCCTGGAATGTATATT",  # noqa: E501
    }
    reads_with_flankers = add_flankers_to_read(reads, fasta_dict)

    expected_flankers = {
        "gene1": ["T", "C", "A", "G", "C", "A", "T", "C"],
        "gene2": ["C", "A", "T", "A", "C", "A", "C", "C"],
        "gene3": ["C", "T", "G", "C", "A", "T", "G", "A"],
    }

    for read in reads_with_flankers:
        flankers = expected_flankers[read.gene_id]
        assert read.flankers == flankers
