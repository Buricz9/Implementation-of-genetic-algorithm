import streamlit as st
import matplotlib.pyplot as plt
import time

from genetic_algorithm.algorithm import run_ga

st.title("Algorytm Genetyczny – Funkcja Ackley")

# Konfiguracja parametrów
n_vars = st.number_input("Liczba zmiennych", min_value=1, max_value=50, value=2)
n_bits = st.number_input("Liczba bitów", min_value=1, max_value=64, value=20)
pop_size = st.slider("Wielkość populacji", 10, 500, 50)
generations = st.slider("Liczba pokoleń", 10, 1000, 100)
p_cross = st.slider("Prawdopodobieństwo krzyżowania", 0.0, 1.0, 0.7)
p_mut = st.slider("Prawdopodobieństwo mutacji", 0.0, 1.0, 0.01)

if st.button("Uruchom algorytm genetyczny"):
    start = time.time()
    best_solution, best_score, best_hist, avg_hist, max_hist = run_ga(
        n_vars=n_vars,
        n_bits=n_bits,
        pop_size=pop_size,
        generations=generations,
        p_cross=p_cross,
        p_mut=p_mut
    )
    end = time.time()

    st.success(f"Najlepsze rozwiązanie: {best_solution}")
    st.info(f"Wartość funkcji celu: {best_score:.6f}")
    st.write(f"Czas wykonania: {end - start:.4f} s")

    # Wykres
    fig, ax = plt.subplots()
    ax.plot(best_hist, label="Najlepszy")
    ax.plot(avg_hist, label="Średni")
    ax.plot(max_hist, label="Maksymalny")
    ax.set_xlabel("Pokolenie")
    ax.set_ylabel("Wartość funkcji (Ackley)")
    ax.set_title("Konwergencja algorytmu genetycznego")
    ax.legend()
    ax.grid()
    st.pyplot(fig)