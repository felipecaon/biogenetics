import random
from structures import *

def generate_dna_sample(size: int = 10) -> list:
    return ''.join(random.choice(NUCLETIODES) for _ in range(size))
