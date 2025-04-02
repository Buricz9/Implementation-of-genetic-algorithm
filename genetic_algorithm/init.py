import numpy as np

def random_real_chromosome(n_vars, bounds):
    return list(np.random.uniform(bounds[0], bounds[1], n_vars))

def initial_population(pop_size, n_vars, bounds):
    return [random_real_chromosome(n_vars, bounds) for _ in range(pop_size)]
