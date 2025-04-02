import numpy as np

def one_point_crossover(parent1, parent2, p_cross):
    """
    Jednopunktowe krzyżowanie – losowy punkt cięcia.
    """
    if np.random.rand() < p_cross:
        point = np.random.randint(1, len(parent1) - 1)
        child1 = parent1[:point] + parent2[point:]
        child2 = parent2[:point] + parent1[point:]
        return child1, child2
    return parent1, parent2

def two_point_crossover(parent1, parent2, p_cross):
    """
    Dwupunktowe krzyżowanie – wymiana środkowego fragmentu.
    """
    if np.random.rand() < p_cross:
        pt1 = np.random.randint(1, len(parent1) - 2)
        pt2 = np.random.randint(pt1 + 1, len(parent1) - 1)
        child1 = parent1[:pt1] + parent2[pt1:pt2] + parent1[pt2:]
        child2 = parent2[:pt1] + parent1[pt1:pt2] + parent2[pt2:]
        return child1, child2
    return parent1, parent2

def uniform_crossover(parent1, parent2, p_cross):
    """
    Jednorodne krzyżowanie – losowo wybiera bity od p1 lub p2.
    """
    if np.random.rand() < p_cross:
        child1 = ''.join([np.random.choice([a, b]) for a, b in zip(parent1, parent2)])
        child2 = ''.join([np.random.choice([a, b]) for a, b in zip(parent2, parent1)])
        return child1, child2
    return parent1, parent2
