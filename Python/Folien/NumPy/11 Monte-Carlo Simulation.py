# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.15.2
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# <div style="text-align:center; font-size:200%;">
#  <b>Monte-Carlo Simulation</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 11 Monte-Carlo Simulation.py -->
# <!-- python_courses/slides/module_600_numpy/topic_250_a5_np_monte_carlo.py -->

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# # Einfache Monte-Carlo Simulation
#
# Mit der folgenden Monte Carlo Simulation kann eine Approximation von $\pi$ berechnet
# werden.
#
# Die Grundidee ist zu berechnen, welcher Anteil an zufällig gezogenen Paaren aus Zahlen
# $(x, y)$, mit $x, y \sim SV[0, 1)$  (d.h., unabhängig und stetig auf $[0, 1)$
# verteilt) eine $\ell^2$ Norm kleiner als 1 hat. Diese Zahl ist eine Approximation von
# $\pi/4$.
#
# Die folgende naive Implementierung is in (fast) reinem Python geschrieben und
# verwendet NumPy nur zur Berechnung der Zufallszahlen.

# %% tags=["keep"]
import numpy as np
import time


# %%
def show_runtime(fun, args=[], kwargs={}, num_iterations: int = 1, repeat=1):
    print("Starting timer run...", end="")
    result = None
    best_time_in_ms = np.inf
    for _ in range(repeat):
        start_time = time.perf_counter_ns()
        for _ in range(num_iterations):
            tmp_result = fun(*args, **kwargs)
            tmp_time = time.perf_counter_ns() - start_time
            if tmp_time < best_time_in_ms:
                best_time_in_ms = tmp_time / (num_iterations * 1e6)
                result = tmp_result
    print("done.")
    print(
        f"Time per iteration: {best_time_in_ms:.2f}ms "
        # f"({num_iterations} iterations)."
    )
    return result


# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
def mc_pi_1(n):
    num_in_circle = 0
    rng = np.random.default_rng(42)
    for _ in np.arange(n):
        xy = rng.random(2)
        if (xy**2).sum() < 1:
            num_in_circle += 1
    return num_in_circle * 4 / n


# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
def test(mc_pi):
    np.random.seed(64)
    for n in [100, 10_000, 100_000, 1_000_000]:
        result = show_runtime(mc_pi, [n], num_iterations=1)
        print(f"𝜋 ≈ {result} ({n} iterations)")


# %%
test(mc_pi_1)

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Durch Just-in-Time Übersetzung mit Numba kann die Performance teils erheblich
# gesteigert werden. Allerdings wird nicht jede Funktion beschleunigt und oft
# führen kleine Unterschiede zu großen Unterschieden in der Laufzeit.

# %%
import numba

# %%
# mc_pi_1_nb = numba.jit(mc_pi_1)
mc_pi_1_nb = numba.jit(mc_pi_1, forceobj=True)

# %%
test(mc_pi_1_nb)


# %%
@numba.jit()
def mc_pi_1a_nb(n):
    num_in_circle = 0
    for _ in np.arange(n):
        xy = np.random.random(2)
        if (xy**2).sum() < 1:
            num_in_circle += 1
    return num_in_circle * 4 / n


# %%
test(mc_pi_1a_nb)


# %%
# %load_ext cython


# %% language="cython"
# # # language_level = 3
# # import numpy as np
# # def mc_pi_1_cython(n):
# #     num_in_circle = 0
# #     rng = np.random.default_rng(42)
# #     for _ in np.arange(n):
# #         xy = rng.random(2)
# #         if (xy**2).sum() < 1:
# #             num_in_circle += 1
# #     return num_in_circle * 4 / n


# %%
# test(mc_pi_1_cython)


# %% magic_args="-a" language="cython"
# # # language_level = 3
# # import numpy as np
# # import random
# # cimport cython
# # def mc_pi_1a_cython(n):
# #     cdef int num_in_circle = 0
# #     for _ in np.arange(n):
# #         x = cython.declare(double)
# #         y = cython.declare(double)
# #         x = random.random()
# #         y = random.random()
# #         if x**2 + y**2 < 1:
# #             num_in_circle += 1
# #     return num_in_circle * 4 / n


# %%
# test(mc_pi_1a_cython)


# %% [markdown]
# Die folgende Implementierung verwendet die Vektorisierungs-Features von NumPy:

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
def mc_pi_2(n):
    x = np.random.random(n)
    y = np.random.random(n)
    return ((x**2 + y**2) < 1).sum() * 4 / n


# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
test(mc_pi_2)

# %%
# # %time mc_pi_2(100_000_000)

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
#
# Auch bei dieser Version können mit Numba Performance-Steigerungen erzielt
# werden, aber in deutlich geringerem Ausmaß (relativ zum Ausgangswert):

# %%
mc_pi_2_nb = numba.njit(mc_pi_2)

# %%
test(mc_pi_2_nb)

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Mini-Workshop: Roulette
#
#
# Analysieren Sie die Gewinnerwartung eines Spielers in folgender vereinfachter
# Form eines Roulettespiels mittels Monte Carlo Simulation:
#
# - Der Kessel ist in 36 Zahlen unterteilt.
# - Der Spieler wählt eine der Zahlen 1 bis 36 und wettet 1 Euro.
# - Fällt die Kugel auf die gewählte Zahl, so erhält der Spieler seinen Einsatz
#   plus 35 Euro zurück.
# - Andernfalls verliert der Spieler seinen Einsatz.
#
# Schreiben Sie eine Version der Simulation mit `for`-Schleife in Python und
# testen Sie die Performance dieser Version vor und nach Kompilierung mit Numba.
# Schreiben Sie dann eine vektorisierte Version und testen Sie deren Performance
# in beiden Fällen.
#
# *Hinweise:*
# - Die NumPy Bibliothek enthält eine Funktion
#   `np.random.randint(low, high, size=None)`, mit der Sie ein Array mit Shape
#   `size` erzeugen können, das gleichverteilte Zufallszahlen zwischen `low`
#   (inklusive) und `high` (exklusive) enthält.
# - Wird `np.random.randint()` mit nur zwei Argumenten aufgerufen, so gibt es
#   eine einzige Zahl zurück.
# - Die NumPy Bibliothek enthält eine Funktion `np.random.binomial(n, p,
#   size=None)`, mit der Sie binomialverteilte Zufallszahlen erzeugen können.


# %%
# import numpy as np


# %%
def roulette1(n):
    # We can assume that the player always bets on 1
    money_spent = 0
    money_won = 0
    for i in range(n):
        money_spent += 1
        if np.random.randint(1, 37) == 1:
            money_won += 36
    return (money_won - money_spent) / n


# %%
def test_roulette(roulette):
    np.random.seed(123)
    for n in [1000, 100_000, 1_000_000]:
        result = show_runtime(roulette, [n])
        print(f"win/loss ≈ {result} ({n} iterations)")


# %%
test_roulette(roulette1)

# %%
import numba

roulette1_nb = numba.njit(roulette1)

# %%
test_roulette(roulette1_nb)


# %%
def roulette2(n):
    money_spent = np.ones(n)
    money_won = np.random.binomial(1, 1.0 / 36.0, n) * 36
    return (money_won - money_spent).sum() / n


# %%
test_roulette(roulette2)

# %%
roulette2_nb = numba.njit(roulette2)

# %%
test_roulette(roulette2_nb)


# %%
def roulette3(n):
    money_spent = n
    money_won = np.random.binomial(n, 1.0 / 36.0) * 36
    return (money_won - money_spent) / n


# %%
test_roulette(roulette3)

# %%
roulette3_nb = numba.njit(roulette3)

# %%
test_roulette(roulette3_nb)

# %%
roulette3(100_000_000)

# %%
