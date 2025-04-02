import numpy as np
import time
from decode import decode
from fitness import booth_function, ackley_function
from selection.selection_methods import tournament_selection, roulette_selection, random_selection
from crossover.crossover_binary import one_point_crossover, two_point_crossover, uniform_crossover
from mutation import mutation_binary as mut

# Mapowanie funkcji
mutation_map_binary = {
    "classic": mut.bit_mutation,
    "one_point": mut.one_point_mutation,
    "two_point": mut.two_point_mutation
}

crossover_map_binary = {
    "single_point": one_point_crossover,
    "two_point": two_point_crossover,
    "uniform": uniform_crossover
}

selection_map = {
    "tournament": tournament_selection,
    "rws": roulette_selection,
    "random": random_selection
}


def run_ga_binary(
    generations,
    population_size,
    function_name,
    selection_type,
    crossover_type,
    mutation_type,
    p_mut=0.01,
    p_cross=0.8,
    elitism=True,
    gene_type=int
):
    start_time = time.time()

    n_bits = 10
    n_vars = 2
    total_bits = n_bits * n_vars
    bounds = (-32.768, 32.768) if function_name == "Ackley" else (0, 10)
    fitness_func = ackley_function if function_name == "Ackley" else booth_function

    def random_chromosome():
        return ''.join(np.random.choice(['0', '1']) for _ in range(total_bits))

    population = [random_chromosome() for _ in range(population_size)]
    best_scores, avg_scores, worst_scores = [], [], []

    for gen in range(generations):
        decoded = [decode(ch, n_vars, n_bits, bounds) for ch in population]
        scores = [fitness_func(d) for d in decoded]

        best_idx = np.argmin(scores)
        best_solution = decoded[best_idx]
        best_score = scores[best_idx]

        best_scores.append(best_score)
        avg_scores.append(np.mean(scores))
        worst_scores.append(np.max(scores))

        selected = selection_map[selection_type](population, scores)
        children = []

        for i in range(0, population_size, 2):
            p1, p2 = selected[i], selected[(i + 1) % population_size]
            
            if np.random.rand() < p_cross:
                c1, c2 = crossover_map_binary[crossover_type](p1, p2, p_cross)
            else:
                c1, c2 = p1, p2
        
            c1 = mutation_map_binary[mutation_type](c1, p_mut)
            c2 = mutation_map_binary[mutation_type](c2, p_mut)
            children.extend([c1, c2])

        if elitism:
            children[0] = population[best_idx]

        population = children

    final_decoded = [decode(ch, n_vars, n_bits, bounds) for ch in population]
    final_scores = [fitness_func(d) for d in final_decoded]
    best_idx = np.argmin(final_scores)
    end_time = time.time()

    return {
        "solution": final_decoded[best_idx],
        "fitness": final_scores[best_idx],
        "best_scores": best_scores,
        "avg_scores": avg_scores,
        "worst_scores": worst_scores,
        "execution_time": end_time - start_time  # ✅ Poprawione!
    }
