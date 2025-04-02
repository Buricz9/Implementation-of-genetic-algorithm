import numpy as np

def tournament_selection(population, scores, tournament_size=3):
    selected = []
    pop_size = len(population)
    for _ in range(pop_size):
        i, j = np.random.randint(0, pop_size, 2)
        winner = population[i] if scores[i] < scores[j] else population[j]
        selected.append(winner)
    return selected

def roulette_selection(population, scores):
    fitness = 1 / (np.array(scores) + 1e-6)
    probs = fitness / np.sum(fitness)
    indices = np.random.choice(len(population), size=len(population), p=probs)
    return [population[i] for i in indices]

def random_selection(population, scores=None):
    return list(np.random.choice(population, size=len(population), replace=True))
