from Bio import SeqIO
import csv
import operator as op


# Exercise 3


def GenomeAnalyze(fasta_file):
    """
    Calculate genome length, GC content and number of occurences of ATG
    sequence in a fasta sequence and write the results as a csv table
    in a new file ruddi.csv
    """
    for record in SeqIO.parse(fasta_file, "fasta"):
        seq_length = len(record.seq)
        G_count = op.countOf(record.seq, "G")
        C_count = op.countOf(record.seq, "C")
        GC_content = ((G_count + C_count) / seq_length) * 100
        F_ATG_count = record.seq.count("ATG")
        R_ATG_count = record.seq.reverse_complement().count("ATG")
        with open("ruddi.csv", "w") as f:
            csvwriter = csv.writer(f, delimiter=",", quotechar='"')
            csvwriter.writerow(["Length_of_genome", seq_length])
            csvwriter.writerow(["GC_content", GC_content])
            csvwriter.writerow(["ATG_forward", F_ATG_count])
            csvwriter.writerow(["ATG_reverse", R_ATG_count])


GenomeAnalyze("GCA_000287275.1_ASM28727v1_genomic.fna")
