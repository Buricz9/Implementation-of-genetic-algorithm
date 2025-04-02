import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import time
import io

from genetic_algorithm.algorithm_real import run_ga

st.title("Algorytm Genetyczny – Chromosomy Rzeczywiste – Funkcja Ackley")

n_vars = st.number_input("Liczba zmiennych", min_value=1, max_value=50, value=2)
pop_size = st.slider("Wielkość populacji", 10, 500, 100)
generations = st.slider("Liczba pokoleń (epok)", 10, 1000, 100)
p_cross = st.slider("Prawdopodobieństwo krzyżowania", 0.0, 1.0, 0.8)
p_mut = st.slider("Prawdopodobieństwo mutacji", 0.0, 1.0, 0.5)

selection_type = st.selectbox("Typ selekcji", ["tournament", "roulette", "best"])
crossover_type = st.selectbox("Typ krzyżowania", ["arithmetic", "linear", "blend_alpha", "alpha_beta", "average"])
mutation_type = st.selectbox("Typ mutacji", ["uniform", "gaussian"])
elitism = st.checkbox("Włącz elitaryzm", value=True)

if st.button("Uruchom Algorytm"):
    start_time = time.time()
    best_solution, best_score, best_hist, avg_hist, max_hist = run_ga(
        n_vars=n_vars,
        bounds=(-32.768, 32.768),
        pop_size=pop_size,
        generations=generations,
        p_cross=p_cross,
        p_mut=p_mut,
        selection_type=selection_type,
        crossover_type=crossover_type,
        mutation_type=mutation_type,
        elitism=elitism
    )
    end_time = time.time()

    st.success(f"Najlepsze rozwiązanie: {best_solution}")
    st.info(f"Wartość funkcji celu: {best_score:.6f}")
    st.write(f"Czas wykonania: {end_time - start_time:.4f} s")

    fig, ax = plt.subplots()
    ax.plot(best_hist, label="Najlepszy osobnik")
    ax.plot(avg_hist, label="Średnia dla populacji")
    ax.plot(max_hist, label="Najgorszy osobnik")
    ax.set_xlabel("Pokolenie")
    ax.set_ylabel("Wartość funkcji (Ackley)")
    ax.set_title("Konwergencja algorytmu genetycznego")
    ax.legend()
    ax.grid()
    st.pyplot(fig)

    buf = io.BytesIO()
    fig.savefig(buf, format="png")
    st.download_button(
        label="Pobierz wykres",
        data=buf.getvalue(),
        file_name="konwergencja.png",
        mime="image/png"
    )
