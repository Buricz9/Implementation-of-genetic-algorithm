import streamlit as st
import matplotlib.pyplot as plt
from real_runner import run_ga_real
from binary_runner import run_ga_binary

st.set_page_config(layout="wide")
st.title("🔬 Porównanie: Algorytm Genetyczny – P3")

# Funkcja celu
def_choice = st.selectbox("Wybierz funkcję celu:", ["Booth", "Ackley"])

# Parametry globalne
generations = st.slider("Liczba epok", 10, 1000, 100)
pop_size = st.slider("Wielkość populacji", 10, 500, 50)

col1, col2 = st.columns(2)

# === Parametry rzeczywiste ===
with col1:
    st.subheader("⚙️ Parametry – Rzeczywiste")
    real_selection_gui = st.selectbox("Selekcja (real)", ["tournament", "rws", "random"])
    real_crossover_gui = st.selectbox("Krzyżowanie (real)", ["single_point", "two_point", "uniform"])
    real_mutation_gui = st.selectbox("Mutacja (real)", ["random", "swap"])
    elitism_real = st.checkbox("Elitaryzm (real)", value=True)

# === Parametry binarne ===
with col2:
    st.subheader("⚙️ Parametry – Binarne")
    binary_selection = st.selectbox("Selekcja (binary)", ["tournament", "rws", "random"])
    binary_crossover = st.selectbox("Krzyżowanie (binary)", ["single_point", "two_point", "uniform"])
    binary_mutation = st.selectbox("Mutacja (binary)", ["classic", "one_point", "two_point"])
    p_cross_binary = st.slider("Prawdopodobieństwo krzyżowania (binary)", 0.0, 1.0, 0.8)
    p_mut_binary = st.slider("Prawdopodobieństwo mutacji (binary)", 0.0, 1.0, 0.01)
    elitism_binary = st.checkbox("Elitaryzm (binary)", value=True)

# === MAPOWANIE nazw do PyGAD ===
selection_map = {
    "tournament": "tournament",
    "rws": "rws",
    "random": "random"
}

crossover_map_real = {
    "single_point": "single_point",
    "two_point": "two_points",
    "uniform": "uniform"
}

mutation_map_real = {
    "random": "random",
    "swap": "swap",
}

# === URUCHOMIENIE ALGORYTMU ===
if st.button("🚀 Uruchom optymalizację"):
    # Rzeczywiste
    result_real = run_ga_real(
        generations=generations,
        population_size=pop_size,
        function_name=def_choice,
        selection_type=selection_map[real_selection_gui],
        crossover_type=crossover_map_real[real_crossover_gui],
        mutation_type=mutation_map_real[real_mutation_gui],
        elitism=elitism_real,
        gene_type=float
    )

    # Binarne
    result_binary = run_ga_binary(
        generations=generations,
        population_size=pop_size,
        function_name=def_choice,
        selection_type=selection_map[binary_selection],
        crossover_type=binary_crossover,
        mutation_type=binary_mutation,
        p_mut=p_mut_binary,
        p_cross=p_cross_binary,
        elitism=elitism_binary,
        gene_type=int
    )

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📊 Wyniki – Rzeczywiste")
        st.write(f"Najlepsze rozwiązanie: {result_real['solution']}")
        st.write(f"Fitness: {result_real['fitness']:.6f}")
        st.write(f"Czas wykonania: {result_real['execution_time']:.4f} s")

        fig1, ax1 = plt.subplots()
        ax1.plot(result_real["best_scores"], label="Najlepszy")
        if result_real["avg_scores"]:
            ax1.plot(result_real["avg_scores"], label="Średni")
        if result_real["worst_scores"]:
            ax1.plot(result_real["worst_scores"], label="Najgorszy")
        ax1.set_title("Konwergencja – rzeczywista")
        ax1.set_xlabel("Epoka")
        ax1.set_ylabel("Wartość funkcji")
        ax1.legend()
        st.pyplot(fig1)

    with col2:
        st.subheader("📊 Wyniki – Binarne")
        st.write(f"Najlepsze rozwiązanie: {result_binary['solution']}")
        st.write(f"Fitness: {result_binary['fitness']:.6f}")
        st.write(f"Czas wykonania: {result_binary['execution_time']:.4f} s")

        fig2, ax2 = plt.subplots()
        ax2.plot(result_binary["best_scores"], label="Najlepszy")
        if result_binary["avg_scores"]:
            ax2.plot(result_binary["avg_scores"], label="Średni")
        if result_binary["worst_scores"]:
            ax2.plot(result_binary["worst_scores"], label="Najgorszy")
        ax2.set_title("Konwergencja – binarna")
        ax2.set_xlabel("Epoka")
        ax2.set_ylabel("Wartość funkcji")
        ax2.legend()
        st.pyplot(fig2)
