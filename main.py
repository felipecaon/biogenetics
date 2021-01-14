from DNAToolkit import *

dna_seq = generate_dna_sample(20)

print(f'Sequence: {dna_seq}')
print(f'Nucleotide frequency: {nucleotide_frequency(dna_seq)}')

reverse_complementary_dna_strand = get_reverse_complementary_dna_strand(dna_seq)

print(f'Reverse Complement: {reverse_complementary_dna_strand}')

print('Transcripton:', transcript(dna_seq))