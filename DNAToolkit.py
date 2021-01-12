nucleotides = ['A', 'C', 'G', 'T']

def validate(dna: str):
    dna = dna.upper()
    for nucleotide in dna:
        if nucleotide not in nucleotides:
            return "Not a valid DNA sequence"
    return dna

def count_nucleotide_frequency(dna: str):
    nucleotide_frequency = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for nucleotide in dna:
        nucleotide_frequency[nucleotide] += 1;
    return nucleotide_frequency
