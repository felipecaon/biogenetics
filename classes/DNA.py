from structures import *

class DNA:
    def __init__(self, sequence: str):
        self.sequence = sequence

    def is_valid(self) -> str:
        dna = self.sequence.upper()
        for nucleotide in dna:
            if nucleotide not in NUCLETIODES:
                return "No"
        return "Yes"

    def nucleotide_frequency(self) -> dict:
        nucleotide_frequency = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
        for nucleotide in self.sequence:
            nucleotide_frequency[nucleotide] += 1;
        return nucleotide_frequency

    def reverse_strand(self) -> str:
        return self.sequence[::-1]

    def get_complementary_strand(self) -> str:
        return DNA(sequence=''.join([DNA_COMPLEMENT[nuc] for nuc in self.sequence]))

    def transcript(self) -> str:
        """DNA -> RNA. Transforms Tynine to Uracil.""" 
        return self.sequence.replace ("T", "U")

    def get_reverse_complementary_dna_strand(self) -> str:
        return self.get_complementary_strand().reverse_strand()
