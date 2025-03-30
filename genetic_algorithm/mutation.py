import numpy as np

def mutate(chromosome, p_mut):
    return ''.join('1' if gene == '0' else '0' if np.random.rand() < p_mut else gene for gene in chromosome)

def mutate_boundary(chromosome, p_mut):
    return ''.join(np.random.choice(['0', '1']) if np.random.rand() < p_mut else gene for gene in chromosome)

def mutate_one_point(chromosome, p_mut):
    if np.random.rand() < p_mut:
        point = np.random.randint(len(chromosome))
        chromosome_list = list(chromosome)
        chromosome_list[point] = '1' if chromosome_list[point] == '0' else '0'
        return ''.join(chromosome_list)
    return chromosome

def mutate_two_point(chromosome, p_mut):
    if np.random.rand() < p_mut:
        points = np.random.choice(len(chromosome), 2, replace=False)
        chromosome = list(chromosome)
        for point in points:
            chromosome[point] = '1' if chromosome[point] == '0' else '0'
        return ''.join(chromosome)
    return chromosome
