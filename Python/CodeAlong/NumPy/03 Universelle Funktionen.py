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
#  <b>Universelle Funktionen</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 03 Universelle Funktionen.py -->
# <!-- python_courses/slides/module_600_numpy/topic_125_a5_np_universal_functions.py -->

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# # Aggregat- und Universelle Funktionen
#
# Aggregatfunktionen berechnen einen skalaren Wert aus einem Vektor.
#
# [Universelle Funktionen](https://numpy.org/doc/stable/reference/ufuncs.html)
# sind Funktionen, die sowohl auf Numpy-Arrays als auch auf anderen Datentypen
# wie Listen oder Skalaren ausgeführt werden können und die elementweise auf
# ihren Argumenten operieren.

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Aggregat-Methoden und Statistik
#

# %% tags=["keep"]
import numpy as np

# %% tags=["keep"]
v1 = np.array([2.0, 3.0, 4.0])
v2 = np.array([0.0, 1.0, 8.0])

# %%

# %%

# %%

# %%

# %%

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Universelle Funktionen
#
# "Universelle Funktion" ("ufunc"):
# - Funktion, die elementweise auf Arrays arbeitet
# - Stellt schnelle vektorisierte Operationen bereit
# - Kann auf Arrays jeder Dimension angewendet werden
# - Beispiele für ufuncs: `sin()`, `cos()`, `add()`, `subtract()`, `multiply()`
# - Viele Methoden von Vektoren stehen auch als ufuncs zur Verfügung.
# - Zusätzlich gibt es viele weitere universelle Funktionen, die nicht als
#   Methoden implementiert sind.

# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
v1 = np.array([2.0, 3.0, 4.0])
v2 = np.array([0.0, 1.0, 8.0])

# %%

# %%

# %%

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Viele universelle Funktionen sind nicht als Methoden verfügbar:

# %%

# %%

# %%

# %%

# %%

# %%

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# ## Mini-Workshop: Aggregat- und Universelle Funktionen
#
# Gegeben sei der folgende Vektor:

# %% tags=["keep"]
vec = np.array([1, 3, 3, 8, 2, 9, 3, 8, 1, 7])

# %% [markdown] lang="de"
#
# Berechnen Sie für diesen Vektor die folgenden Größen:
#
# - Summe
# - Produkt
# - Mittelwert
# - Standardabweichung
# - Median

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %%

# %%

# %%

# %%
