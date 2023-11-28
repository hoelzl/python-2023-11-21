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
#  <b>Motivation für NumPy</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 01 Motivation für NumPy.py -->
# <!-- python_courses/slides/module_600_numpy/topic_110_a3_np_motivation.py -->

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# # Vektoren und Matrizen als Python Listen

# %% tags=["keep"]
vector1 = [3, 2, 4]
vector2 = [8, 9, 7]

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Berechnungen mit Python Listen
#
# Wir können für Berechnungen keine mathematischen Operatoren verwenden, da
# diese entweder nicht definiert sind, oder die falsche Bedeutung haben:

# %%


# %%

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Statt Operatoren zu verwenden, können wir Funktionen definieren:

# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
def vector_add(v1, v2):
    assert len(v1) == len(v2)
    result = [0] * len(v1)
    for i in range(len(v1)):
        result[i] = v1[i] + v2[i]
    return result

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Matrizen können als verschachtelte Listen repräsentiert werden:
#
# $$
# M_1 = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{pmatrix}
# \qquad
# M_2 = \begin{pmatrix} 10 & 11 & 12 \\ 13 & 14 & 15 \\ 16 & 17 & 18 \end{pmatrix}
# $$


# %% tags=["keep"]
matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[10, 11, 12], [13, 14, 15], [16, 17, 18]]


# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
def matrix_add(m1, m2):
    # Can only add matrices with the same number of rows
    assert len(m1) == len(m2)
    result = []
    for row1, row2 in zip(m1, m2):
        result.append(vector_add(row1, row2))
    return result


# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Zugriff auf Elemente

# %% tags=["keep"]
vector1 = [3, 2, 4]

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Bei Matrizen kann mit mehreren Indexing-Operationen auf Elemente zugegriffen werden:

# %% tags=["keep"]
matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# %%

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Performance

# %% tags=["keep"]
from random import random


# %% tags=["keep"]
def make_random_vector(num_elts: int):
    return [round(random() * 100, 1) for _ in range(num_elts)]


# %%

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
def make_random_matrix(num_rows: int, num_cols: int):
    result = []
    for _ in range(num_rows):
        result.append(make_random_vector(num_cols))
    return result


# %% tags=["keep"]
make_random_matrix(5, 3)

# %% tags=["keep"]
m1 = make_random_matrix(20, 5)
m2 = make_random_matrix(20, 5)

# %%

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
from timeit import Timer


# %% tags=["keep"]
def compute_runtime_in_ms(code: str, num_iterations: int, repeat=1):
    timer = Timer(code, globals=globals())
    print("Starting timer run...", end="")
    time_in_ms = (
        min(timer.repeat(number=num_iterations, repeat=repeat)) / num_iterations * 1000
    )
    print("done.")
    print(f"Time per iteration: {time_in_ms:.2f}ms ({num_iterations} iterations).")
    return time_in_ms


# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
m1 = make_random_matrix(10_000, 10)
m2 = make_random_matrix(10_000, 10)

# %% tags=["keep"]
time_python = compute_runtime_in_ms("matrix_add(m1, m2)", 100, 4)

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
import numpy as np

# %% tags=["keep"]
a1 = np.array(m1)
a2 = np.array(m2)

# %% tags=["keep"]
a1

# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
a1 + a2

# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
np.all(matrix_add(m1, m2) == a1 + a2)

# %% tags=["keep"]
time_numpy = compute_runtime_in_ms("a1 + a2", 10_000, 4)

# %% tags=["keep"]
print(f"Ratio python/numpy: {time_python/time_numpy:.1f}")

# %%
