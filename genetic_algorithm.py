import numpy as np
from ackley import ackley

# ================== DEKODOWANIE ==================
def binary_to_real(binary, bounds, n_bits):
    value = int(binary, 2)
    min_bound, max_bound = bounds
    return min_bound + (value / (2 ** n_bits - 1)) * (max_bound - min_bound)

def decode(chromosome, n_vars, n_bits, bounds):
    decoded = []
    for i in range(n_vars):
        start = i * n_bits
        end = (i + 1) * n_bits
        binary_value = chromosome[start:end]
        real_value = binary_to_real(binary_value, bounds, n_bits)
        decoded.append(real_value)
    return decoded

# ================== INICJALIZACJA ==================
def random_chromosome(n_vars, n_bits):
    return ''.join(np.random.choice(['0', '1']) for _ in range(n_vars * n_bits))

def initial_population(pop_size, n_vars, n_bits):
    return [random_chromosome(n_vars, n_bits) for _ in range(pop_size)]

# ================== OCENA ==================
def evaluate_population(population, n_vars, n_bits, bounds):
    decoded_pop = [decode(chrom, n_vars, n_bits, bounds) for chrom in population]
    scores = [ackley(ind) for ind in decoded_pop]
    return scores, decoded_pop

# ================== SELEKCJA ==================
def selection_tournament(population, scores):
    selected = []
    pop_size = len(population)
    for _ in range(pop_size):
        i, j = np.random.randint(0, pop_size, 2)
        winner = population[i] if scores[i] < scores[j] else population[j]
        selected.append(winner)
    return selected

def selection_roulette(population, scores):
    fitness = np.max(scores) - np.array(scores) + 1e-9
    total_fitness = np.sum(fitness)
    rel_fitness = fitness / total_fitness
    cum_probs = np.cumsum(rel_fitness)
    selected = []
    pop_size = len(population)
    for _ in range(pop_size):
        r = np.random.rand()
        index = np.searchsorted(cum_probs, r)
        selected.append(population[index])
    return selected

def selection_best(population, scores, n_best=None):
    if n_best is None:
        n_best = len(population)
    sorted_indices = np.argsort(scores)
    best_indices = sorted_indices[:n_best]
    return [population[i] for i in best_indices]

# ================== KRZYŻOWANIE ==================
def crossover_one_point(parent1, parent2, p_cross):
    if np.random.rand() < p_cross:
        point = np.random.randint(1, len(parent1) - 1)
        child1 = parent1[:point] + parent2[point:]
        child2 = parent2[:point] + parent1[point:]
        return child1, child2
    return parent1, parent2

def crossover_two_point(parent1, parent2, p_cross):
    if np.random.rand() < p_cross:
        pt1 = np.random.randint(1, len(parent1) - 2)
        pt2 = np.random.randint(pt1, len(parent1) - 1)
        child1 = parent1[:pt1] + parent2[pt1:pt2] + parent1[pt2:]
        child2 = parent2[:pt1] + parent1[pt1:pt2] + parent2[pt2:]
        return child1, child2
    return parent1, parent2

def crossover_uniform(parent1, parent2, p_cross):
    if np.random.rand() < p_cross:
        child1 = ''.join([parent1[i] if np.random.rand() < 0.5 else parent2[i] for i in range(len(parent1))])
        child2 = ''.join([parent2[i] if np.random.rand() < 0.5 else parent1[i] for i in range(len(parent2))])
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

# ================== MUTACJA ==================
def mutate(chromosome, p_mut):
    chromosome_list = list(chromosome)
    for i in range(len(chromosome_list)):
        if np.random.rand() < p_mut:
            chromosome_list[i] = '1' if chromosome_list[i] == '0' else '0'
    return ''.join(chromosome_list)

def mutate_boundary(chromosome, p_mut):
    chromosome_list = list(chromosome)
    for i in range(len(chromosome_list)):
        if np.random.rand() < p_mut:
            chromosome_list[i] = np.random.choice(['0', '1'])
    return ''.join(chromosome_list)

def mutate_one_point(chromosome, p_mut):
    if np.random.rand() < p_mut:
        point = np.random.randint(len(chromosome))
        chromosome_list = list(chromosome)
        chromosome_list[point] = '1' if chromosome_list[point] == '0' else '0'
        return ''.join(chromosome_list)
    return chromosome

def mutate_two_point(chromosome, p_mut):
    chromosome_list = list(chromosome)
    if np.random.rand() < p_mut:
        points = np.random.choice(range(len(chromosome)), 2, replace=False)
        for point in points:
            chromosome_list[point] = '1' if chromosome_list[point] == '0' else '0'
    return ''.join(chromosome_list)

# ================== INWERSJA ==================
def inversion(chromosome, p_inversion):
    if np.random.rand() < p_inversion:
        start = np.random.randint(0, len(chromosome) - 1)
        end = np.random.randint(start + 1, len(chromosome))
        inverted = chromosome[start:end][::-1]
        return chromosome[:start] + inverted + chromosome[end:]
    return chromosome

# ================== ZAPIS WYNIKÓW ==================
def save_results(filename, best_solution, best_score, best_scores_history, avg_scores_history, max_scores_history):
    with open(filename, 'w') as f:
        f.write(f"Najlepsze rozwiązanie: {best_solution}\n")
        f.write(f"Najlepszy wynik (wartość funkcji): {best_score:.6f}\n\n")
        f.write("Pokolenie;Najlepszy;Średni;Maksymalny\n")
        for i in range(len(best_scores_history)):
            f.write(f"{i};{best_scores_history[i]:.6f};{avg_scores_history[i]:.6f};{max_scores_history[i]:.6f}\n")

# ================== ALGORYTM GŁÓWNY ==================
def run_ga(
        n_vars=2,
        n_bits=20,
        bounds=(-32.768, 32.768),
        pop_size=50,
        generations=100,
        p_cross=0.7,
        p_mut=0.01,
        p_inversion=0.05,
        selection_type='tournament',
        crossover_type='one_point',
        mutation_type='classic',
        elitism=True
):
    population = initial_population(pop_size, n_vars, n_bits)
    best_scores_history = []
    avg_scores_history = []
    max_scores_history = []

    for gen in range(generations):
        scores, decoded_pop = evaluate_population(population, n_vars, n_bits, bounds)
        best_idx = np.argmin(scores)
        best_score = scores[best_idx]
        best_solution = decoded_pop[best_idx]

        avg_score = np.mean(scores)
        max_score = np.max(scores)

        best_scores_history.append(best_score)
        avg_scores_history.append(avg_score)
        max_scores_history.append(max_score)

        print(f"Pokolenie {gen}: Najlepszy wynik: {best_score:.6f}, Średni: {avg_score:.6f}, Rozwiązanie: {best_solution}")

        # Selekcja
        if selection_type == 'tournament':
            selected = selection_tournament(population, scores)
        elif selection_type == 'roulette':
            selected = selection_roulette(population, scores)
        elif selection_type == 'best':
            selected = selection_best(population, scores)
        else:
            raise ValueError("Nieznana metoda selekcji")

        # Tworzenie nowej populacji
        children = []
        for i in range(0, pop_size, 2):
            parent1 = selected[i]
            parent2 = selected[(i + 1) % pop_size]

            # Krzyżowanie
            if crossover_type == 'one_point':
                child1, child2 = crossover_one_point(parent1, parent2, p_cross)
            elif crossover_type == 'two_point':
                child1, child2 = crossover_two_point(parent1, parent2, p_cross)
            elif crossover_type == 'uniform':
                child1, child2 = crossover_uniform(parent1, parent2, p_cross)
            elif crossover_type == 'granular':
                child1, child2 = crossover_granular(parent1, parent2, p_cross)
            else:
                raise ValueError("Nieznany typ krzyżowania")

            # Mutacja
            if mutation_type == 'classic':
                child1 = mutate(child1, p_mut)
                child2 = mutate(child2, p_mut)
            elif mutation_type == 'boundary':
                child1 = mutate_boundary(child1, p_mut)
                child2 = mutate_boundary(child2, p_mut)
            elif mutation_type == 'one_point':
                child1 = mutate_one_point(child1, p_mut)
                child2 = mutate_one_point(child2, p_mut)
            elif mutation_type == 'two_point':
                child1 = mutate_two_point(child1, p_mut)
                child2 = mutate_two_point(child2, p_mut)
            else:
                raise ValueError("Nieznany typ mutacji")

            # Inwersja
            child1 = inversion(child1, p_inversion)
            child2 = inversion(child2, p_inversion)

            children.append(child1)
            children.append(child2)

        if elitism:
            children[0] = population[best_idx]

        population = children

    final_scores, final_decoded = evaluate_population(population, n_vars, n_bits, bounds)
    best_idx = np.argmin(final_scores)
    best_score = final_scores[best_idx]
    best_solution = final_decoded[best_idx]

    return best_solution, best_score, best_scores_history, avg_scores_history, max_scores_history
