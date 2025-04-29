# algorithm_real.py
import numpy as np
from mealpy import FloatVar                             # ← FloatVar do definiowania zakresów :contentReference[oaicite:0]{index=0}
from mealpy.swarm_based.GWO import OriginalGWO           # ← prawidłowa klasa GWO :contentReference[oaicite:1]{index=1}
from ackley import ackley

def run_gwo(
        n_vars: int = 30,
        bounds: tuple = (-32.768, 32.768),
        pop_size: int = 50,
        iterations: int = 200,
        runs: int = 30
):
    lb = [bounds[0]] * n_vars
    ub = [bounds[1]] * n_vars

    # MealPy 3.x: używamy FloatVar zamiast oddzielnego lb/ub
    problem = {
        "obj_func": ackley,
        "bounds": FloatVar(lb=lb, ub=ub),
        "minmax": "min",
        "log_to": None,    # wyciszamy logi
    }

    all_curves = []
    best_positions = []
    best_fits = []

    for _ in range(runs):
        model = OriginalGWO(epoch=iterations, pop_size=pop_size)
        best_agent = model.solve(problem)
        best_positions.append(best_agent.solution)
        best_fits.append(best_agent.target.fitness)
        # historia globalnie najlepszego osobnika w każdej iteracji
        all_curves.append(model.history.list_global_best_fit)

    all_curves  = np.array(all_curves)
    mean_curve  = all_curves.mean(axis=0)
    std_curve   = all_curves.std(axis=0)

    # wybieramy globalnie najlepszy z wszystkich powtórzeń
    idx_best       = int(np.argmin(best_fits))
    global_best_pos = best_positions[idx_best]
    global_best_fit = best_fits[idx_best]

    return global_best_pos, global_best_fit, mean_curve, std_curve
