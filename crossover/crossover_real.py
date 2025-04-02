import numpy as np

def arithmetic_crossover(parent1, parent2):
    child = [(g1 + g2) / 2 for g1, g2 in zip(parent1, parent2)]
    return child, child

def blend_crossover(parent1, parent2, alpha=0.5):
    child1 = []
    child2 = []
    for g1, g2 in zip(parent1, parent2):
        d = abs(g1 - g2)
        low = min(g1, g2) - alpha * d
        high = max(g1, g2) + alpha * d
        child1.append(np.random.uniform(low, high))
        child2.append(np.random.uniform(low, high))
    return child1, child2
