from fai.read import Read
from fai.read_fasta import read_fasta
from pathlib import Path

from fai.read_sam import read_sam


def test_deserialize_fasta():
    project_root = Path(__file__).resolve().parent.parent
    result = read_fasta(str(project_root) + "/tests/fixtures/micro.fasta", "gene_id=")
    expected = {
        "yal001": "ATGCGTACGTTAGCTAGCTAGGCTAGCTAG",
        "yal004": "ATGAGCTAGCTAGGCTAGCTAGCTAGCTAA",
    }

    assert result == expected


def test_deserialize_sam():
    project_root = Path(__file__).resolve().parent.parent
    result = read_sam(str(project_root) + "/tests/fixtures/micro.sam")

    expected = [
        Read("gene1", 5, 30),
        Read("gene2", 10, 33),
        Read("gene3", 15, 28),
    ]

    for i in range(len(result)):
        assert result[i].gene_id == expected[i].gene_id
        assert result[i].gene_position == expected[i].gene_position
        assert result[i].size == expected[i].size
