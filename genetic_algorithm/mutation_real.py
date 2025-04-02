import numpy as np

def mutate_uniform_real(chromosome, p_mut, bounds):
    return [
        gene if np.random.rand() > p_mut else np.random.uniform(bounds[0], bounds[1])
        for gene in chromosome
    ]

def mutate_gaussian(chromosome, p_mut, mean=0, std=1):
    return [
        gene + np.random.normal(mean, std) if np.random.rand() < p_mut else gene
        for gene in chromosome
    ]
