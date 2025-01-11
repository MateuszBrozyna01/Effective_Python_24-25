import argparse
import sympy as sp

# Parser argumentów
parser = argparse.ArgumentParser(description="Metoda Newtona do znajdowania miejsc zerowych funkcji (także zespolonych).")
parser.add_argument("funkcja", type=str, help="Funkcja w postaci wyrażenia, np. x**2+x+1")
parser.add_argument("start", type=complex, help="Punkt startowy (może być zespolony) dla metody Newtona")
parser.add_argument("-s", "--step", type=float, default=1e-5, help="Wielkość kroku w pochodnej")
parser.add_argument("-n", "--steps", type=int, default=100, help="Maksymalna liczba kroków")
parser.add_argument("-t", "--tolerance", type=float, default=1e-7, help="Tolerancja dla wyniku")

args = parser.parse_args()

# Zmienna x jako symbol
x = sp.symbols('x')

# Funkcja i jej pochodna (wzór sympy)
f = sp.sympify(args.funkcja)
df = sp.diff(f, x)

# Konwersja funkcji na formę numeryczną
f_func = sp.lambdify(x, f, 'numpy')
df_func = sp.lambdify(x, df, 'numpy')

# Ustawienie punktu początkowego
current_x = args.start

# Iteracja w metodzie Newtona
for step in range(args.steps):
    f_val = f_func(current_x)
    df_val = df_func(current_x)

    # Warunek zakończenia, jeśli funkcja w punkcie jest wystarczająco blisko zera
    if abs(f_val) < args.tolerance:
        print(f"Znaleziono miejsce zerowe: x = {current_x:.10f}, w {step + 1} krokach.")
        break

    # Sprawdzenie, czy pochodna jest zerowa
    if df_val == 0:
        print("Pochodna jest zerowa. Metoda Newtona nie działa.")
        break

    # Aktualizacja punktu
    current_x = current_x - f_val / df_val
else:
    print("Nie znaleziono miejsca zerowego w podanej liczbie kroków.")
