import numpy as np

def inversion(chromosome, p_inversion):
    if np.random.rand() < p_inversion:
        start = np.random.randint(0, len(chromosome) - 1)
        end = np.random.randint(start + 1, len(chromosome))
        return chromosome[:start] + chromosome[start:end][::-1] + chromosome[end:]
    return chromosome
