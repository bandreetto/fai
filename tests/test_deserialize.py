from fai.read_fasta import read_fasta
from pathlib import Path


def test_deserialize_fasta():
    project_root = Path(__file__).resolve().parent.parent
    result = read_fasta(str(project_root) + "/tests/fixtures/micro.fasta", "gene_id=")
    expected = {
        "yal001": "ATGCGTACGTTAGCTAGCTAGGCTAGCTAG",
        "yal004": "ATGAGCTAGCTAGGCTAGCTAGCTAGCTAA",
    }

    print(result)
    print(expected)
    assert result == expected
