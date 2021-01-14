import random

NUCLETIODES = ['A', 'C', 'G', 'T']
DNA_COMPLEMENT = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}

def validate(dna_seq: str) -> str:
    dna = dna_seq.upper()
    for nucleotide in dna:
        if nucleotide not in NUCLETIODES:
            return "Not a valid DNA sequence"
    return dna

def nucleotide_frequency(dna_seq: str) -> dict:
    nucleotide_frequency = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for nucleotide in dna_seq:
        nucleotide_frequency[nucleotide] += 1;
    return nucleotide_frequency

def generate_dna_sample(size: int = 10) -> list:
    return ''.join(random.choice(NUCLETIODES) for _ in range(size))

def get_complementary_dna_strand(dna_seq: str) -> str:
    return ''.join([DNA_COMPLEMENT[nuc] for nuc in dna_seq])

def reverse_dna_strand(dna_seq: str) -> str:
    return dna_seq[::-1]

def get_reverse_complementary_dna_strand(dna_seq: str) -> str:
    return reverse_dna_strand(get_complementary_dna_strand(dna_seq))


def transcript(dna_seq: str) -> str:
    """DNA -> RNA. Transforms Tynine to Uracil.""" 
    return dna_seq.replace ("T", "U")