from genetic_algorithm.algorithm import run_ga
import matplotlib.pyplot as plt
import time

if __name__ == "__main__":
    start_time = time.time()
    best_solution, best_score, best_hist, avg_hist, max_hist = run_ga(
        n_vars=2,
        n_bits=10,
        bounds=(-32.768, 32.768),
        pop_size=100,
        generations=100,
        p_cross=0.8,
        p_mut=0.5,
        selection_type='best',
        crossover_type='two_point',
        elitism=True
    )
    end_time = time.time()

    print("\n--- WYNIK KOŃCOWY ---")
    print(f"Najlepsze znalezione rozwiązanie: {best_solution}")
    print(f"Wartość funkcji celu: {best_score:.6f}")
    print(f"Czas wykonania: {end_time - start_time:.4f} s")

    plt.figure()
    plt.plot(best_hist, label="Najlepszy osobnik")
    plt.plot(avg_hist, label="Średnia dla populacji")
    plt.plot(max_hist, label="Najgorszy osobnik")
    plt.title("Konwergencja algorytmu genetycznego")
    plt.xlabel("Pokolenie")
    plt.ylabel("Wartość funkcji (Ackley)")
    plt.legend()
    plt.grid()
    plt.show()
