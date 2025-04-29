# main.py
import argparse
from algorithm_real import run_gwo

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--n_vars",    type=int,   default=30)
    parser.add_argument("--pop_size",  type=int,   default=50)
    parser.add_argument("--iters",     type=int,   default=200)
    parser.add_argument("--runs",      type=int,   default=30)
    args = parser.parse_args()

    best_pos, best_fit, mean_curve, std_curve = run_gwo(
        n_vars=args.n_vars,
        pop_size=args.pop_size,
        iterations=args.iters,
        runs=args.runs
    )
    print("Best pos:", best_pos)
    print("Best fit:", best_fit)
