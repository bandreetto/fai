from csv import reader

from fai.read import Read


def read_sam(sam_file_path: str) -> list[Read]:
    """Deserialize the reads in a SAM file.

    The SAM format can be extremely large.  To avoid holding two copies of the
    data we now stream the CSV reader and build the resulting list of ``Read``
    instances in a single pass.
    """

    with open(sam_file_path, "r", encoding="utf-8") as file:
        sam_table = reader(file, delimiter="\t")

        return [
            Read(row[2], int(row[3]), len(row[9]))
            for row in sam_table
            if row and not row[0].startswith("@")
        ]
