import numpy as np
from ackley import ackley


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


def random_chromosome(n_vars, n_bits):
    return ''.join(np.random.choice(['0', '1']) for _ in range(n_vars * n_bits))


def initial_population(pop_size, n_vars, n_bits):
    return [random_chromosome(n_vars, n_bits) for _ in range(pop_size)]


def evaluate_population(population, n_vars, n_bits, bounds):
    decoded_pop = [decode(chrom, n_vars, n_bits, bounds) for chrom in population]
    scores = [ackley(ind) for ind in decoded_pop]
    return scores, decoded_pop


# -------------------- SELEKCJE --------------------

def selection_tournament(population, scores):
    """Selekcja turniejowa"""
    selected = []
    pop_size = len(population)
    for _ in range(pop_size):
        i, j = np.random.randint(0, pop_size, 2)
        # W przypadku minimalizacji wybieramy mniejsze score
        winner = population[i] if scores[i] < scores[j] else population[j]
        selected.append(winner)
    return selected


def selection_roulette(population, scores):
    """Selekcja ruletkowa (dla minimalizacji)"""
    # Możemy np. zrobić odwrotność dopasowania, aby lepsze (mniejsze) score miały większą szansę
    fitness = np.max(scores) - np.array(scores) + 1e-9  # odwracamy, aby mniejsze score => wyższe fitness
    total_fitness = np.sum(fitness)
    rel_fitness = fitness / total_fitness

    # Tworzymy dystrybuantę
    cum_probs = np.cumsum(rel_fitness)

    selected = []
    pop_size = len(population)
    for _ in range(pop_size):
        r = np.random.rand()
        # Szukamy pierwszego osobnika, dla którego cum_probs >= r
        index = np.searchsorted(cum_probs, r)
        selected.append(population[index])
    return selected


# -------------------- KRZYŻOWANIA --------------------

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
        child1 = (
                parent1[:pt1]
                + parent2[pt1:pt2]
                + parent1[pt2:]
        )
        child2 = (
                parent2[:pt1]
                + parent1[pt1:pt2]
                + parent2[pt2:]
        )
        return child1, child2
    return parent1, parent2


# -------------------- MUTACJA --------------------

def mutate(chromosome, p_mut):
    chromosome_list = list(chromosome)
    for i in range(len(chromosome_list)):
        if np.random.rand() < p_mut:
            chromosome_list[i] = '1' if chromosome_list[i] == '0' else '0'
    return ''.join(chromosome_list)


# -------------------- GŁÓWNA FUNKCJA GA --------------------

def run_ga(
        n_vars=2,
        n_bits=20,
        bounds=(-32.768, 32.768),
        pop_size=50,
        generations=100,
        p_cross=0.7,
        p_mut=0.01,
        selection_type='tournament',
        crossover_type='one_point',
        elitism=True
):
    # Inicjalizacja populacji
    population = initial_population(pop_size, n_vars, n_bits)
    best_scores_history = []
    avg_scores_history = []
    max_scores_history = []

    for gen in range(generations):
        scores, decoded_pop = evaluate_population(population, n_vars, n_bits, bounds)

        # Statystyki
        best_idx = np.argmin(scores)
        best_score = scores[best_idx]
        best_solution = decoded_pop[best_idx]

        avg_score = np.mean(scores)
        max_score = np.max(scores)

        best_scores_history.append(best_score)
        avg_scores_history.append(avg_score)
        max_scores_history.append(max_score)

        print(
            f"Pokolenie {gen}: Najlepszy wynik: {best_score:.6f}, Średni: {avg_score:.6f}, Rozwiązanie: {best_solution}")

        # Selekcja
        if selection_type == 'tournament':
            selected = selection_tournament(population, scores)
        elif selection_type == 'roulette':
            selected = selection_roulette(population, scores)
        else:
            raise ValueError("Nieznana metoda selekcji")

        # Tworzenie nowej populacji przez krzyżowanie i mutację
        children = []
        for i in range(0, pop_size, 2):
            parent1 = selected[i]
            parent2 = selected[(i + 1) % pop_size]

            # Różne rodzaje krzyżowania
            if crossover_type == 'one_point':
                child1, child2 = crossover_one_point(parent1, parent2, p_cross)
            elif crossover_type == 'two_point':
                child1, child2 = crossover_two_point(parent1, parent2, p_cross)
            else:
                raise ValueError("Nieznany typ krzyżowania")

            # Mutacja
            child1 = mutate(child1, p_mut)
            child2 = mutate(child2, p_mut)

            children.append(child1)
            children.append(child2)

        # Elitaryzm – zastąp pierwsze miejsce najlepszym z poprzedniej populacji
        if elitism:
            children[0] = population[best_idx]

        population = children

    # Po ostatniej epoce
    final_scores, final_decoded = evaluate_population(population, n_vars, n_bits, bounds)
    best_idx = np.argmin(final_scores)
    best_score = final_scores[best_idx]
    best_solution = final_decoded[best_idx]

    return best_solution, best_score, best_scores_history, avg_scores_history, max_scores_history
