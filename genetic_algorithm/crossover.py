import numpy as np

def crossover_one_point(parent1, parent2, p_cross):
    if np.random.rand() < p_cross:
        point = np.random.randint(1, len(parent1) - 1)
        return parent1[:point] + parent2[point:], parent2[:point] + parent1[point:]
    return parent1, parent2

def crossover_two_point(parent1, parent2, p_cross):
    if np.random.rand() < p_cross:
        pt1 = np.random.randint(1, len(parent1) - 2)
        pt2 = np.random.randint(pt1, len(parent1) - 1)
        return (parent1[:pt1] + parent2[pt1:pt2] + parent1[pt2:], 
                parent2[:pt1] + parent1[pt1:pt2] + parent2[pt2:])
    return parent1, parent2

def crossover_uniform(parent1, parent2, p_cross):
    if np.random.rand() < p_cross:
        child1 = ''.join([parent1[i] if np.random.rand() < 0.5 else parent2[i] for i in range(len(parent1))])
        child2 = ''.join([parent2[i] if np.random.rand() < 0.5 else parent1[i] for i in range(len(parent1))])
        return child1, child2
    return parent1, parent2

def crossover_granular(parent1, parent2, p_cross, grain_size=2):
    if np.random.rand() < p_cross:
        child1 = ''
        child2 = ''
        for i in range(0, len(parent1), grain_size):
            if np.random.rand() < 0.5:
                child1 += parent1[i:i+grain_size]
                child2 += parent2[i:i+grain_size]
            else:
                child1 += parent2[i:i+grain_size]
                child2 += parent1[i:i+grain_size]
        return child1, child2
    return parent1, parent2
