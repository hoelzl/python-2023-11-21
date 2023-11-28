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

# %%

# %%

# %%

# %%

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Bedingte Auswahl
#
# Sie können ein NumPy-Array mit booleschen Werten als Indexwert verwenden, wenn es die
# gleiche Form hat wie das "Werte-Array". Dadurch werden alle Elemente des
# "value"-Arrays ausgewählt, für die der Index den Wert `True` ergibt.

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Broadcasting bei der Selektion
#
# Beim Indexing mit booleschen Arrays wird Broadcasting verwendet, d.h., man kann z.B.
# Zeilen selektieren:

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

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

# %%

# %%

# %%
