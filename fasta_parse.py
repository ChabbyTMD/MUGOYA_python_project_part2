# Import Libraries

from Bio import SeqIO
import csv
import operator as op

# Exercise 2


def proteinInfo(protein_list):
    """
    # A function that takes as input a list of protein fasta files and produces a protein_info.csv file with the following columns:
    # ID,First_10_AA,Length,Number_Cs
    """
    file_columns = ["ID", "First_10_AA", "Length", "Number_Cs"]
    with open("protein_info.csv", "w") as f:
        csvwriter = csv.writer(f, delimiter=",", quotechar='"')
        csvwriter.writerow(file_columns)
        for file in protein_list:
            for record in SeqIO.parse(file + ".fasta", "fasta"):
                csvwriter.writerow(
                    [
                        record.id,
                        record.seq[:10],
                        len(record.seq),
                        op.countOf(record.seq, "C"),
                    ]
                )


prot_list = ["WVS05366.1", "AGJ87295.1", "WVV45440.1", "AGI40145.1"]
proteinInfo(prot_list)
