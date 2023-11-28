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

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Durch Just-in-Time Übersetzung mit Numba kann die Performance teils erheblich
# gesteigert werden. Allerdings wird nicht jede Funktion beschleunigt und oft
# führen kleine Unterschiede zu großen Unterschieden in der Laufzeit.

# %%

# %%

# %%

# %%

# %%


# %%


# %%


# %%


# %%


# %%


# %% [markdown]
# Die folgende Implementierung verwendet die Vektorisierungs-Features von NumPy:

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
#
# Auch bei dieser Version können mit Numba Performance-Steigerungen erzielt
# werden, aber in deutlich geringerem Ausmaß (relativ zum Ausgangswert):

# %%

# %%

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


# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%
