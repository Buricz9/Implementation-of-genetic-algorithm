import numpy as np
from ackley import ackley
from genetic_algorithm.encoding import decode
from genetic_algorithm.init import initial_population
from genetic_algorithm.selection import selection_tournament, selection_roulette, selection_best
from genetic_algorithm.crossover import crossover_one_point, crossover_two_point, crossover_uniform, crossover_granular
from genetic_algorithm.mutation import mutate, mutate_boundary, mutate_one_point, mutate_two_point
from genetic_algorithm.inversion import inversion

def evaluate_population(population, n_vars, n_bits, bounds):
    decoded_pop = [decode(chrom, n_vars, n_bits, bounds) for chrom in population]
    scores = [ackley(ind) for ind in decoded_pop]
    return scores, decoded_pop

def save_results(filename, best_solution, best_score, best_scores_history, avg_scores_history, max_scores_history):
    with open(filename, 'w') as f:
        f.write(f"Najlepsze rozwiązanie: {best_solution}\n")
        f.write(f"Najlepszy wynik (wartość funkcji): {best_score:.6f}\n\n")
        f.write("Pokolenie;Najlepszy;Średni;Maksymalny\n")
        for i in range(len(best_scores_history)):
            f.write(f"{i};{best_scores_history[i]:.6f};{avg_scores_history[i]:.6f};{max_scores_history[i]:.6f}\n")

def run_ga(
        n_vars=2,
        n_bits=10,
        bounds=(-32.768, 32.768),
        pop_size=100,
        generations=100,
        p_cross=0.8,
        p_mut=0.5,
        p_inversion=0.3,
        selection_type='best',
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

        if selection_type == 'tournament':
            selected = selection_tournament(population, scores)
        elif selection_type == 'roulette':
            selected = selection_roulette(population, scores)
        elif selection_type == 'best':
            selected = selection_best(population, scores)
        else:
            raise ValueError("Nieznana metoda selekcji")

        children = []
        for i in range(0, pop_size, 2):
            parent1 = selected[i]
            parent2 = selected[(i + 1) % pop_size]

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
