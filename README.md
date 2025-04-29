# Implementation-of-genetic-algorithm

Funkcjonalności
Eksperyment GWO na funkcji Ackleya

Instalacja krok po kroku
Sklonuj repozytorium (lub pobierz ZIP i rozpakuj):
```powershell
git clone https://github.com/<twoj-uzytkownik>/implementation-of-genetic-algorithm.git
git checkout P4
```

```powershell
cd implementation-of-genetic-algorithm
```
Utwórz i aktywuj wirtualne środowisko:
```powershell
py -m venv .venv
```
```powershell
.\.venv\Scripts\activate
```
Zainstaluj wymagane pakiety:
```powershell
 pip install mealpy streamlit numpy matplotlib
```
Sposoby uruchomienia
```powershell
streamlit run gui.py
```

Alternatywny skrypt w main.py, który uruchamia GWO i wypisuje wynik w konsoli:
```powershell
python main.py --n_vars 30 --pop_size 50 --iters 200 --runs 30
```

Dostępne argumenty:
--n_vars — liczba wymiarów wektora (domyślnie 30)
--pop_size — rozmiar stada wilków (domyślnie 50)
--iters — liczba iteracji GWO (domyślnie 200)
--runs — ile razy powtórzyć optymalizację, by zebrać statystyki (domyślnie 30)

Szczegóły:

ackley.py
Definicja funkcji Ackleya w dowolnej liczbie wymiarów.

algorithm_real.py
Funkcja run_gwo(...):

buduje problem w formacie MealPy (FloatVar z bounds),

wywołuje OriginalGWO.solve(),

zbiera najlepsze rozwiązenia i krzywe konwergencji,

zwraca globalnie najlepszy wektor, jego wartość oraz średnią i odchylenie krzywej.

gui.py
Interfejs Streamlit:

suwaki do parametrów,

przycisk uruchomienia,

wykres średniej konwergencji ± odchylenie.

main.py
CLI-owy entry-point (argparse → run_gwo) — opcjonalny.
