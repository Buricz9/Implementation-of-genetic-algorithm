# Implementation-of-genetic-algorithm

Funkcjonalności
Optymalizacja funkcji Ackley za pomocą algorytmu genetycznego.

Możliwość konfiguracji:

- liczby zmiennych
- zakresów wartości
- liczby bitów na zmienną
- wielkości populacji
- liczby pokoleń
- prawdopodobieństwa krzyżowania i mutacji
- różne metody selekcji (turniejowa, ruletkowa).
- różne krzyżowania (jednopunktowe, dwupunktowe).
- GUI (Tkinter): pozwala na ustawienie parametrów i wyświetla wykres konwergencji.
- zapisywanie wyników do pliku (results/best_scores.txt) w wariancie z main.py.
- Obsługa statystyk populacji: minimum, średnia, maksimum w każdym pokoleniu (w wersji rozbudowanej).


Instalacja krok po kroku
Sklonuj repozytorium (lub pobierz ZIP i rozpakuj):

git clone https://github.com/<twoj-uzytkownik>/implementation-of-genetic-algorithm.git
cd implementation-of-genetic-algorithm
Utwórz i aktywuj wirtualne środowisko:
py -m venv .venv
.\.venv\Scripts\activate

Zainstaluj wymagane pakiety:
pip install numpy matplotlib

Sposoby uruchomienia
py gui.py
