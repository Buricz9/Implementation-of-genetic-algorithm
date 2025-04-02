import numpy as np

def crossover_arithmetic(p1, p2, alpha=0.5):
    c1 = [alpha * x + (1 - alpha) * y for x, y in zip(p1, p2)]
    c2 = [(1 - alpha) * x + alpha * y for x, y in zip(p1, p2)]
    return c1, c2

def crossover_linear(p1, p2):
    c1 = [(x + y) / 2 for x, y in zip(p1, p2)]
    c2 = [2 * x - y for x, y in zip(p1, p2)]
    return c1, c2

def crossover_blend_alpha(p1, p2, alpha=0.5):
    c1, c2 = [], []
    for x, y in zip(p1, p2):
        d = abs(x - y)
        min_val = min(x, y) - alpha * d
        max_val = max(x, y) + alpha * d
        c1.append(np.random.uniform(min_val, max_val))
        c2.append(np.random.uniform(min_val, max_val))
    return c1, c2

def crossover_alpha_beta(p1, p2, alpha=0.4, beta=0.6):
    c1, c2 = [], []
    for x, y in zip(p1, p2):
        d = abs(x - y)
        min_val = min(x, y) - alpha * d
        max_val = max(x, y) + beta * d
        c1.append(np.random.uniform(min_val, max_val))
        c2.append(np.random.uniform(min_val, max_val))
    return c1, c2

def crossover_average(p1, p2):
    avg = [(x + y) / 2 for x, y in zip(p1, p2)]
    return avg, avg
