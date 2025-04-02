import numpy as np

def random_chromosome(n_vars, n_bits):
    return ''.join(np.random.choice(['0', '1']) for _ in range(n_vars * n_bits))

def initial_population(pop_size, n_vars, n_bits):
    return [random_chromosome(n_vars, n_bits) for _ in range(pop_size)]
