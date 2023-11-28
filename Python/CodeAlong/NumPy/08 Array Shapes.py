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
#  <b>Array Shapes</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 08 Array Shapes.py -->
# <!-- python_courses/slides/module_600_numpy/topic_160_a5_np_reshaping.py -->

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# # Array Shapes
#
# NumPy bietet viele Möglichkeiten, die Form und Größe von Arrays zu modifizieren.

# %% tags=["keep"]
import numpy as np

# %% tags=["keep"]
int_vector = np.arange(36)
float_vector = np.arange(36.0)
small_float_vector = np.arange(36.0, dtype=np.float16)

rng = np.random.default_rng(42)
int_matrix = rng.integers(low=0, high=10, size=(3, 5))
tensor = rng.random(size=(3, 4, 5))

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Eigenschaften von Arrays
#
# NumPy bietet viele Möglichkeiten, Information über Arrays zu bekommen.
#
# Mit `shape` kann man die Form eines Arrays bestimmen, also seinen Rang und die
# Anzahl der Elemente pro Rang:

# %%

# %%

# %%

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Das Attribut `size` gibt die Anzahl der Elemente zurück.
#
# Die `len()`-Funktion gibt nur bei 1-dimensionalen Arrays die Anzahl der
# Elemente zurück, sonst die Anzahl der Zeilen!

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Mit dem Attribut `itemsize` kann man den Speicherplatz bestimmen, der von einem
# Element belegt wird.

# %%

# %%

# %%

# %%

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Die `np.info()`-Funktion gibt die interessantesten Informationen über Arrays aus.

# %%

# %%

# %%

# %%

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Ändern von Shape und Größe
#
# ### Ändern des Shapes

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

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### Ändern der Größe
#
# NumPy kann die Größe von Arrays ändern, allerdings nur dann, wenn es nur eine
# Referenz auf das Array gibt.
#
# Im Gegensatz zu `reshape()` muss bei `resize()` der Inhalt des Arrays kopiert
# werden.

# %%

# %%

# %%

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# `np.resize()` ist ähnlich zur `resize()` Methode, aber:
#
# - das ursprüngliche Array wird nicht verändert
# - die Werte werden zyklisch kopiert, wenn das Array vergrößert wird

# %%

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Mit der `np.pad()`-Funktion kann ein Array in ein größeres Array eingebettet
# werden:

# %%

# %%

# %%

# %%

# %%


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Transponieren von Matrizen

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

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Mini-Workshop: Reshaping Arrays
#
# Gegeben seien die folgenden Arrays:


# %%

# %% [markdown] lang="de"
#
# - Erzeugen Sie einen Tensor mit Shape `(3, 1, 3, 1)` aus `vec`
# - Entfernen Sie die Dimensionen mit nur einem Element aus diesem Vektor
# - Erzeugen Sie eine Matrix mit Shape `(2, 9)`, in der jede Zeile die gleichen
#   Werte enthält wie `vec`
# - Erzeugen Sie ein quadratisches Array `mat_square`, das die gleichen Elemente
#   enthält, wie `mat`
# - Können Sie `mat_square.T` nur mit (potentiell mehreren)
#   `reshape()`-Operationen aus `mat` erzeugen?

# %%

# %%

# %%

# %%

# %%

# %%
