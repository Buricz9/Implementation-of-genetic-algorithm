import time
import pygad
import numpy as np
from fitness import booth_function, ackley_function

def run_ga_real(
    generations=100,
    population_size=50,
    function_name="Booth",
    selection_type="tournament",
    crossover_type="single_point",
    mutation_type="random",
    elitism=True,
    gene_type=float,
    num_genes=2
):
    if function_name == "Ackley":
        init_range = (-32.768, 32.768)
    else:
        init_range = (0, 2)

    def fitness_function(ga_instance, solution, solution_idx):
        if function_name == "Ackley":
            return -ackley_function(solution)
        else:
            return -booth_function(solution)

    best_scores = []
    avg_scores = []
    worst_scores = []

# usuniecie munusow 
    def on_generation(ga_instance):
        fitnesses = ga_instance.last_generation_fitness
        objective_values = [-f for f in fitnesses]  # odwracamy z powrotem

        best_scores.append(min(objective_values))    # najmniejsze = najlepsze
        avg_scores.append(np.mean(objective_values)) # średnie
        worst_scores.append(max(objective_values))   # największe = najgorsze


    start_time = time.time()

    ga_instance = pygad.GA(
        num_generations=generations,
        num_parents_mating=population_size // 2,
        fitness_func=fitness_function,
        sol_per_pop=population_size,
        num_genes=num_genes,
        init_range_low=init_range[0],
        init_range_high=init_range[1],
        parent_selection_type=selection_type,
        crossover_type=crossover_type,
        mutation_type=mutation_type,
        keep_parents=1 if elitism else 0,
        gene_type=gene_type,
        on_generation=on_generation
    )

    ga_instance.run()
    end_time = time.time()

    best_solution, best_fitness, _ = ga_instance.best_solution()

    return {
        "solution": best_solution,
        "fitness": -best_fitness,
        "best_scores": best_scores,
        "avg_scores": avg_scores,         
        "worst_scores": worst_scores,     
        "execution_time": end_time - start_time
    }
