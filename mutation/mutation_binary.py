import numpy as np

def bit_mutation(chromosome, p_mut):
    mutated = list(chromosome)
    for i in range(len(mutated)):
        if np.random.rand() < p_mut:
            mutated[i] = '1' if mutated[i] == '0' else '0'
    return ''.join(mutated)

def one_point_mutation(chromosome, p_mut):
    if np.random.rand() < p_mut:
        index = np.random.randint(0, len(chromosome))
        mutated = list(chromosome)
        mutated[index] = '1' if mutated[index] == '0' else '0'
        return ''.join(mutated)
    return chromosome

def two_point_mutation(chromosome, p_mut):
    if np.random.rand() < p_mut:
        idx1, idx2 = np.random.choice(len(chromosome), size=2, replace=False)
        mutated = list(chromosome)
        mutated[idx1] = '1' if mutated[idx1] == '0' else '0'
        mutated[idx2] = '1' if mutated[idx2] == '0' else '0'
        return ''.join(mutated)
    return chromosome
