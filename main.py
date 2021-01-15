from DNAToolkit import *
from classes.DNA import *

dna_seq = generate_dna_sample(20)

print(dna_seq)

dna_obj = DNA(dna_seq)

print(dna_obj.reverse_strand())
print(dna_obj.get_complementary_strand())
print(dna_obj.get_reverse_complementary_dna_strand())