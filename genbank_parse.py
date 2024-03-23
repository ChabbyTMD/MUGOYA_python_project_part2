# Importing Biopython and pandas libraries.
from Bio import SeqIO
from Bio import Entrez
import pandas as pd
import csv

# Exercise 1.


def GenbankInfo(genbank_file_list):
	"""
	A function to parse a list of genbank files. Each genbank file is a record in a new csv file. Each record contains:
	Accession,Family,Genus,Species,Num_Features and source
	"""
	csv_column_names = [
		"Accession",
		"Family",
		"Genus",
		"Species",
		"Num_Features",
		"Source",
	]
	with open("genbank_parse.csv", "w") as f:
		csvwriter = csv.writer(f, delimiter=",", quotechar='"')
		csvwriter.writerow(csv_column_names)
		for file in genbank_file_list:
			record = SeqIO.read(file, "genbank")
			csvwriter.writerow(
				[
					record.id,
					record.annotations["taxonomy"][
						2
					],  # TODO Get reliable way to extract family info
					record.annotations["organism"].split(" ")[0],
					record.annotations["organism"].split(" ")[-1],
					len(record.features),
					record.annotations["source"],
				]
			)


GenbankFiles = [
	"NZ_CALPCP010000001.1.gbk",
	"NZ_CALPCY010000130.1.gbk",
	"NZ_BHVZ01000001.1.gbk",
	"NZ_SRYA01000017.1.gbk",
	"NZ_CAJTFZ010000019.1.gbk",
]

GenbankInfo(GenbankFiles)
