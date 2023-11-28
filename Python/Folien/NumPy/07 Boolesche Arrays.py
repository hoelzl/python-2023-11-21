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
#  <b>Boolesche Arrays</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 07 Boolesche Arrays.py -->
# <!-- python_courses/slides/module_600_numpy/topic_150_np_booleans.py -->

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# # Boolesche Arrays
#
# Arrays mit booleschen Werten spielen in NumPy eine wichtige Rolle, weil sie z.B. oft
# zur Auswahl von Elementen verwendet werden.

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Boolesche Operationen auf Arrays

# %% tags=["keep"]
import numpy as np

# %%
bool_vec = np.array([True, False, True, False, True])

# %%
neg_vec = np.logical_not(bool_vec)
neg_vec

# %%
np.logical_and(bool_vec, neg_vec)

# %%
~bool_vec

# %%
bool_vec & neg_vec

# %%
bool_vec | neg_vec

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Bedingte Auswahl
#
# Sie können ein NumPy-Array mit booleschen Werten als Indexwert verwenden, wenn es die
# gleiche Form hat wie das "Werte-Array". Dadurch werden alle Elemente des
# "value"-Arrays ausgewählt, für die der Index den Wert `True` ergibt.

# %%
vec = np.arange(9)
bool_vec = vec % 3 == 0
print(vec)
print(bool_vec)

# %%
vec[bool_vec]

# %%
arr = np.arange(8).reshape(2, 4)
bool_arr = arr % 2 == 0
bool_arr

# %%
arr[bool_arr]

# %%
# Error!
# arr[bool_arr.reshape(-1)]

# %%
vec[vec % 2 > 0]

# %%
arr[arr < 5]

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Broadcasting bei der Selektion
#
# Beim Indexing mit booleschen Arrays wird Broadcasting verwendet, d.h., man kann z.B.
# Zeilen selektieren:

# %%
arr = np.arange(30).reshape(6, 5)
arr

# %%
arr[:, 1]

# %%
arr[:, 1].shape

# %%
arr[:, 1] % 2 == 0

# %%
arr[arr[:, 1] % 2 == 0]

# %%
arr[arr[:, 1] % 2 == 1]

# %%
arr[1] % 2 == 0

# %%
arr[:, arr[1] % 2 == 0]

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# ## Mini-Workshop: Boolesche Selektion
#
# Gegeben sei die folgende Matrix:

# %% tags=["keep"]
mat = np.arange(20).reshape(4, 5)
mat

# %% [markdown] lang="de"
#
# - Selektieren Sie alle durch 4 teilbaren Elemente in der Matrix
# - Selektieren Sie alle Zeilen, deren Wert in der ersten Spalte kleiner als 10 ist
# - Selektieren Sie alle Spalten, in denen in der ersten Zeile eine durch 2 teilbare
#   Zahl steht
# - Selektieren Sie alle Spalten, in denen in der zweiten Zeile eine Zahl steht, die
#   durch 5 teilbar ist oder größer als 7 ist

# %%
mat[mat % 4 == 0]

# %%
mat[mat[:, 0] < 10]

# %%
mat[:, mat[0] % 2 == 0]

# %%
mat[:, (mat[1] % 5 == 0) | (mat[1] > 7)]
