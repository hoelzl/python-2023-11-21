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
#  <b>Ranges</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 13 Ranges.py -->
# <!-- python_courses/slides/module_150_collections/topic_125_b3_ranges.py -->

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
# ## Simulation der klassischen `for`-Schleife
#
# Iteration mit einer `for`-Schleife ist auch über andere Datenstrukturen als Listen
# möglich.
#
# In Python stellt der Typ `range` eine Folge von ganzen Zahlen dar:
#
# - `range(n)` erzeugt das ganzzahlige Interval von $0$ bis $n-1$
# - `range(m, n)` erzeugt das ganzzahlige Interval von $m$ bis $n-1$
# - `range(m, n, k)` erzeugt die ganzzahlige Sequenz $m, m+k, m+2k, ..., p$, wobei $p$
#    die größte Zahl der Form $m + jk$ mit $j \geq 0$ und $p < n$ ist

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
range(1, 4)

# %%
list(range(1, 4))

# %%
range(4)

# %%
list(range(4))

# %%
list(range(1, 9, 2))

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
for i in range(3):
    print(i, end=", ")

# %%
for i in range(1, 6, 2):
    print(i, end=", ")


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
# ### Mini-Workshop
#
# Schreiben Sie eine Funktion `print_squares(n: int)`, die die Quadrate der
# Zahlen von 1 bis n ausgibt, jeweils ein Element pro Zeile:
#
# ```python
# >>> print_squares(3)
# 1**2 = 1
# 2**2 = 4
# 3**2 = 9
# >>>
# ```


# %%
def print_squares(n: int):
    for i in range(1, n + 1):
        print(i, "**2 = ", i * i, sep="")


# %%
print_squares(3)


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
# ### Mini-Workshop: Summe der ersten n Quadratzahlen
#
# Schreiben Sie eine Funktion `sum_squares(n: int) -> int`, die die Summe der
# ersten $n$ Quadratzahlen zurückgibt:
#
# ```python
# >>> sum_squares(3)
# 14
# >>> sum_squares(10)
# 385
# ```
#

# %%
def sum_squares(n: int) -> int:
    sum = 0
    for i in range(1, n + 1):
        sum += i * i
    return sum


# %% tags=["keep"]
assert sum_squares(3) == 14
assert sum_squares(10) == 385

# %% [markdown] tags=["subslide"] slideshow={"slide_type": "subslide"}
# **Hinweis:** Idee dieser Aufgabe war es, es über eine for-Schleife zu lösen aber
# die Summe der ersten $n$ Quadratzahlen kann auch per Formel ausgerechnet werden:
# $$ \sum_{i=1}^n i^2 = \frac{n(n+1)(2n+1)}{6} $$  
