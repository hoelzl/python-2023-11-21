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
#  <b>Lineare Algebra</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 10 Lineare Algebra.py -->
# <!-- python_courses/slides/module_600_numpy/topic_240_a5_np_linalg.py -->

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# # Lineare Algebra
#
# ## Lösen von Gleichungssystemen
#
# Wie können wir das folgende Gleichungssystem mit NumPy darstellen und lösen:
#
# $$
# 2x_0 + x_1 + x_2 = 4\\
# x_0 + 3x_1 + 2x_2 = 5\\
# x_0 = 6
# $$

# %% tags=["keep"]
import numpy as np

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
a = np.array(
    [
        [2.0, 1.0, 1.0],
        [1.0, 3.0, 2.0],
        [1.0, 0.0, 0.0],
    ]
)

# %%
b = np.array([4.0, 5.0, 6.0])

# %%
x = np.linalg.solve(a, b)
x

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
# Test:
a @ x, b

# %% [markdown]
#
# SciPy bietet spezielle Lösungsverfahren wie LU-Faktorisierung,
# Cholesky-Faktorisierung, etc. an.

# %% slideshow={"slide_type": "-"}
import scipy.linalg as linalg

lu = linalg.lu_factor(a)

# %%
lu

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
x = linalg.lu_solve(lu, b)

# %%
x

# %%
a @ x

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
# Hermite'sche Matrix, positiv definit
a = np.array(
    [
        [10.0, -1.0, 2.0, 0.0],
        [-1.0, 11.0, -1.0, 3.0],
        [2.0, -1.0, 10.0, -1.0],
        [0.0, 3.0, -1.0, 8.0],
    ]
)

# %% tags=["keep"]
b = np.array([6.0, 25.0, -11.0, 15.0])

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
cholesky = linalg.cholesky(a)

# %%
cholesky

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
cholesky.T.conj() @ cholesky

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
y = np.linalg.solve(cholesky.T.conj(), b)

# %%
x = np.linalg.solve(cholesky, y)

# %%
x

# %%
a @ x

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# ## Mini-Workshop: Lösen von Gleichungssystemen
#
# Lösen Sie folgendes Gleichungssystem:
#
# $x_1 - x_2 + 2x_3 = 6$
#
# $2x_1 + 3x_2 + 2x_3 = 8$
#
# $3x_1 + 2x_2 + x_3 = 8$

# %%
a = np.array(
    [
        [1.0, -1.0, 2.0],
        [2.0, 3.0, 2.0],
        [3.0, 2.0, 1.0],
    ]
)

# %%
b = np.array([6.0, 8.0, 8.0])

# %%
import scipy.linalg

# %%
lu = scipy.linalg.lu_factor(a)

# %%
x = scipy.linalg.lu_solve(lu, b)

# %%
x

# %%
a.dot(x)

# %% [markdown]
# Einfacher:

# %%
np.linalg.solve(a, b)
