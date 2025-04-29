# gui.py

import streamlit as st
import matplotlib.pyplot as plt
from algorithm_real import run_gwo

st.title("Eksperyment GWO na funkcji Ackleya")

# ——————————————————————————
# Panel parametrów
n_vars     = st.number_input("Liczba zmiennych", min_value=1, max_value=100, value=30)
pop_size   = st.slider("Rozmiar populacji", 10, 500, 50, step=10)
iterations = st.slider("Liczba iteracji", 10, 2000, 200, step=10)
runs       = st.slider("Liczba powtórzeń", 1, 100, 30, step=1)

if st.button("Uruchom eksperyment"):
    with st.spinner("Optymalizacja w toku..."):
        best_sol, best_val, mean_curve, std_curve = run_gwo(
            n_vars=n_vars,
            bounds=(-32.768, 32.768),
            pop_size=pop_size,
            iterations=iterations,
            runs=runs
        )
    st.success(f"**Najlepsze rozwiązanie:** {best_sol}")
    st.info(f"**Wartość funkcji Ackleya:** {best_val:.6f}")

    fig, ax = plt.subplots()
    ax.plot(mean_curve, label="Średnia konwergencja")
    ax.fill_between(
        range(len(mean_curve)),
        mean_curve - std_curve,
        mean_curve + std_curve,
        alpha=0.3,
        label="±1 odchylenie standardowe"
    )
    ax.set_xlabel("Iteracja")
    ax.set_ylabel("Ackley(x)")
    ax.set_title("Krzywa konwergencji GWO")
    ax.legend()
    ax.grid()
    st.pyplot(fig)
