import matplotlib.pyplot as plt

def plot_scores(best, avg=None, worst=None, title="Wykres konwergencji", save_path=None):
    plt.figure()
    plt.plot(best, label="Najlepszy")
    if avg: plt.plot(avg, label="Średni")
    if worst: plt.plot(worst, label="Najgorszy")
    plt.xlabel("Pokolenie")
    plt.ylabel("Wartość funkcji")
    plt.title(title)
    plt.legend()
    plt.grid()
    if save_path:
        plt.savefig(save_path)
    plt.show()
