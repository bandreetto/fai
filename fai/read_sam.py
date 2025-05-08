from fai.read import Read
from csv import reader


def read_sam(sam_file_path: str) -> list[Read]:
    file = open(sam_file_path, "r")

    sam_table = reader(file, delimiter="\t")

    headerless_list = [row for row in sam_table if not row[0].startswith("@")]

    filtered_list = [Read(row[2], int(row[3]), len(row[9])) for row in headerless_list]

    return filtered_list
