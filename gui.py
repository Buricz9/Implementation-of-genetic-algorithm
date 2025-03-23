import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import time

from genetic_algorithm import run_ga

def run_ga_from_gui():
    """
    Funkcja wywoływana po wciśnięciu przycisku "Start GA".
    Pobiera parametry z pól tekstowych, uruchamia GA i wyświetla wyniki.
    """
    try:
        # Pobieramy wartości z pól tekstowych
        n_vars = int(entry_n_vars.get())
        n_bits = int(entry_n_bits.get())
        pop_size = int(entry_pop_size.get())
        generations = int(entry_generations.get())
        p_cross = float(entry_p_cross.get())
        p_mut = float(entry_p_mut.get())

        start_time = time.time()
        best_solution, best_score, best_scores_history, avg_scores_history, max_scores_history = run_ga(
            n_vars=n_vars,
            n_bits=n_bits,
            pop_size=pop_size,
            generations=generations,
            p_cross=p_cross,
            p_mut=p_mut,
            # Możesz dać tu parametry np. selection_type, crossover_type,
            # bounds=(-32.768, 32.768), elitism=True, itp.
        )
        end_time = time.time()

        # Wyświetlamy wynik w Label i oknie dialogowym
        result_str = (
            f"Najlepsze rozwiązanie: {best_solution}\n"
            f"Wartość funkcji: {best_score:.6f}\n"
            f"Czas wykonania: {end_time - start_time:.4f} s"
        )

        label_result.config(text=result_str)
        messagebox.showinfo("Wynik algorytmu genetycznego", result_str)

        # Rysowanie wykresu z konwergencją – np. przebieg najlepszego wyniku
        plt.figure()
        plt.plot(best_scores_history, label="Najlepszy")
        plt.plot(avg_scores_history, label="Średni")
        plt.plot(max_scores_history, label="Maksymalny")
        plt.title("Konwergencja algorytmu genetycznego")
        plt.xlabel("Pokolenie")
        plt.ylabel("Wartość funkcji (Ackley)")
        plt.legend()
        plt.grid()
        plt.show()

    except ValueError:
        messagebox.showerror("Błąd danych", "Upewnij się, że wszystkie pola wypełniono liczbami.")

# === GŁÓWNE OKNO APLIKACJI ===

root = tk.Tk()
root.title("Algorytm Genetyczny - Ackley")

# Frame (kontener) na wszystkie pola i przyciski
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

# Pola do wprowadzania parametrów
label_n_vars = tk.Label(frame, text="Liczba zmiennych (n_vars):")
label_n_vars.grid(row=0, column=0, sticky="e")
entry_n_vars = tk.Entry(frame)
entry_n_vars.insert(0, "2")  # wartość domyślna
entry_n_vars.grid(row=0, column=1)

label_n_bits = tk.Label(frame, text="Liczba bitów (n_bits):")
label_n_bits.grid(row=1, column=0, sticky="e")
entry_n_bits = tk.Entry(frame)
entry_n_bits.insert(0, "20")
entry_n_bits.grid(row=1, column=1)

label_pop_size = tk.Label(frame, text="Wielkość populacji (pop_size):")
label_pop_size.grid(row=2, column=0, sticky="e")
entry_pop_size = tk.Entry(frame)
entry_pop_size.insert(0, "50")
entry_pop_size.grid(row=2, column=1)

label_generations = tk.Label(frame, text="Liczba pokoleń (generations):")
label_generations.grid(row=3, column=0, sticky="e")
entry_generations = tk.Entry(frame)
entry_generations.insert(0, "100")
entry_generations.grid(row=3, column=1)

label_p_cross = tk.Label(frame, text="Prawdopodobieństwo krzyżowania (p_cross):")
label_p_cross.grid(row=4, column=0, sticky="e")
entry_p_cross = tk.Entry(frame)
entry_p_cross.insert(0, "0.7")
entry_p_cross.grid(row=4, column=1)

label_p_mut = tk.Label(frame, text="Prawdopodobieństwo mutacji (p_mut):")
label_p_mut.grid(row=5, column=0, sticky="e")
entry_p_mut = tk.Entry(frame)
entry_p_mut.insert(0, "0.01")
entry_p_mut.grid(row=5, column=1)

# Przycisk start
btn_start = tk.Button(frame, text="Start GA", command=run_ga_from_gui)
btn_start.grid(row=6, column=0, columnspan=2, pady=10)

# Etykieta, w której wyświetlimy wynik
label_result = tk.Label(frame, text="", fg="blue", justify="left")
label_result.grid(row=7, column=0, columnspan=2)

# Uruchamiamy pętlę obsługującą zdarzenia GUI
root.mainloop()
