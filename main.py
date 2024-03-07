# Simple examples of using biopython

from Bio import SeqIO

# Read a sequence from a file
dna_seq = SeqIO.read("sequence.fasta", "fasta").seq

# Print the sequence
print("Sequence:", dna_seq)

# Print the length of the sequence
print("Length:", len(dna_seq))

# Print nucleotide composition
print("A:", dna_seq.count("A"))
print("C:", dna_seq.count("C"))
print("G:", dna_seq.count("G"))
print("T:", dna_seq.count("T"))

# Transcribe the DNA sequence into mRNA
mRNA_seq = dna_seq.transcribe()
print("mRNA Sequence:", mRNA_seq)

# Translate the mRNA sequence into an amino acid sequence
protein_seq = mRNA_seq.translate()
print("Protein Sequence:", protein_seq)