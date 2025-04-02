import numpy as np
from ackley import ackley
from genetic_algorithm.init import initial_population
from genetic_algorithm.selection import selection_tournament, selection_roulette, selection_best
from genetic_algorithm.crossover_real import (
    crossover_arithmetic, crossover_linear,
    crossover_blend_alpha, crossover_alpha_beta,
    crossover_average
)
from genetic_algorithm.mutation_real import mutate_uniform_real, mutate_gaussian

def evaluate_population(population):
    scores = [ackley(ind) for ind in population]
    return scores, population

def run_ga(
        n_vars=2,
        bounds=(-32.768, 32.768),
        pop_size=100,
        generations=100,
        p_cross=0.8,
        p_mut=0.5,
        selection_type='best',
        crossover_type='arithmetic',
        mutation_type='uniform',
        elitism=True
):
    population = initial_population(pop_size, n_vars, bounds)
    best_scores_history = []
    avg_scores_history = []
    max_scores_history = []

    for gen in range(generations):
        scores, population = evaluate_population(population)
        best_idx = np.argmin(scores)
        best_score = scores[best_idx]
        best_solution = population[best_idx]

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

        # Tworzenie dzieci
        children = []
        for i in range(0, pop_size, 2):
            parent1 = selected[i]
            parent2 = selected[(i + 1) % pop_size]

            # Krzyżowanie
            if np.random.rand() < p_cross:
                if crossover_type == 'arithmetic':
                    child1, child2 = crossover_arithmetic(parent1, parent2)
                elif crossover_type == 'linear':
                    child1, child2 = crossover_linear(parent1, parent2)
                elif crossover_type == 'blend_alpha':
                    child1, child2 = crossover_blend_alpha(parent1, parent2)
                elif crossover_type == 'alpha_beta':
                    child1, child2 = crossover_alpha_beta(parent1, parent2)
                elif crossover_type == 'average':
                    child1, child2 = crossover_average(parent1, parent2)
                else:
                    raise ValueError("Nieznany typ krzyżowania")
            else:
                child1, child2 = parent1[:], parent2[:]

            # Mutacja
            if mutation_type == 'uniform':
                child1 = mutate_uniform_real(child1, p_mut, bounds)
                child2 = mutate_uniform_real(child2, p_mut, bounds)
            elif mutation_type == 'gaussian':
                child1 = mutate_gaussian(child1, p_mut)
                child2 = mutate_gaussian(child2, p_mut)
            else:
                raise ValueError("Nieznany typ mutacji")

            children.append(child1)
            children.append(child2)

        if elitism:
            children[0] = best_solution

        population = children

    # Finalna ocena
    final_scores, population = evaluate_population(population)
    best_idx = np.argmin(final_scores)
    best_score = final_scores[best_idx]
    best_solution = population[best_idx]

    return best_solution, best_score, best_scores_history, avg_scores_history, max_scores_history
