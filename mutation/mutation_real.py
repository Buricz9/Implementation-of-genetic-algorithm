import numpy as np

def gaussian_mutation(solution, p_mut, mu=0, sigma=0.1):
    mutated = []
    for gene in solution:
        if np.random.rand() < p_mut:
            gene += np.random.normal(mu, sigma)
        mutated.append(gene)
    return mutated

def uniform_mutation(solution, p_mut, low=-1, high=1):
    mutated = []
    for gene in solution:
        if np.random.rand() < p_mut:
            gene = np.random.uniform(low, high)
        mutated.append(gene)
    return mutated
