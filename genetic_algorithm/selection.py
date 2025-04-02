import numpy as np

def selection_tournament(population, scores):
    selected = []
    for _ in range(len(population)):
        i, j = np.random.randint(0, len(population), 2)
        winner = population[i] if scores[i] < scores[j] else population[j]
        selected.append(winner)
    return selected

def selection_roulette(population, scores):
    fitness = np.max(scores) - np.array(scores) + 1e-9
    total_fitness = np.sum(fitness)
    rel_fitness = fitness / total_fitness
    cum_probs = np.cumsum(rel_fitness)
    selected = []
    for _ in range(len(population)):
        r = np.random.rand()
        index = np.searchsorted(cum_probs, r)
        selected.append(population[index])
    return selected

def selection_best(population, scores, n_best=None):
    if n_best is None:
        n_best = len(population)
    best_indices = np.argsort(scores)[:n_best]
    return [population[i] for i in best_indices]
