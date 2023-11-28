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
#  <b>Erzeugen von Numpy Arrays</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 05 Erzeugen von Numpy Arrays.py -->
# <!-- python_courses/slides/module_600_numpy/topic_130_a5_np_creating_arrays.py -->

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# # Erzeugen von Numpy Arrays

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Erzeugen von Arrays aus Listen

# %% tags=["keep"]
import numpy as np

# %%
vec = np.array([1, 2, 3, 4])

# %%
vec

# %%
vec.shape

# %% tags=["keep"]
mat = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

# %%
mat

# %%
mat.shape

# %% tags=["keep"]
tensor = np.array(
    [
        [[1, 2, 3, 5], [2, 3, 4, 5], [3, 4, 5, 6]],
        [[4, 5, 6, 7], [5, 6, 7, 8], [6, 7, 8, 9]],
    ]
)

# %%
tensor

# %%
tensor.shape

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Ranges und Lineare Räume

# %% tags=["keep"]
list(range(10))

# %%
np.array(range(10))

# %%
np.arange(10)

# %%
np.arange(10.0)

# %%
np.arange(0.0, 2.5, 0.5)

# %% [markdown] lang="de"
#
# 10 Werte, zwischen 0.0 und 1.0 gleichverteilt:

# %%
np.arange(0.0, 1.1, 1 / 9)

# %%
np.linspace(0.0, 1.0, 10)

# %%
np.linspace(0.0, 1.0, 11)

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Konstante Werte

# %%
zs = np.zeros(3)
zs

# %%
zs.shape

# %%
np.zeros((3,))

# %%
np.zeros((2, 3))

# %%
np.zeros((2, 3, 4))

# %%
np.ones((2, 3))

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Uninitialisierte Arrays
#
# - Werden angelegt, ohne dass der Speicher mit einem bestimmten Wert belegt
#   wird
# - Jedes Element *muss* vor dem ersten Zugriff geschrieben werden

# %%
np.empty((2, 4))

# %%
from timeit import repeat

# %%
min(repeat("np.empty((100, 100))", repeat=20, globals=globals()))

# %%
min(repeat("np.zeros((100, 100))", repeat=20, globals=globals()))

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Einheitsmatrizen

# %%
np.eye(3)

# %%
np.identity(3)

# %%
np.eye(2, 3)

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Mini-Workshop: Erzeugen von Arrays
#
# Erzeugen Sie folgende NumPy Arrays:


# %% [markdown]
# ```python
# array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# ```

# %%
np.arange(10)

# %% [markdown]
# ```python
# array([1. , 1.5, 2. , 2.5, 3. , 3.5, 4. , 4.5])
# ```

# %%
np.arange(1.0, 5.0, 0.5)

# %% [markdown]
# ```python
# array([0.  , 1.25, 2.5 , 3.75, 5.  ])
# ```

# %%
np.linspace(0, 5, 5)


# %% [markdown]
# ```python
# array([[[0., 0.],
#         [0., 0.]],
#
#        [[0., 0.],
#         [0., 0.]],
#
#        [[0., 0.],
#         [0., 0.]]])
# ```

# %%
np.zeros((3, 2, 2))

# %% [markdown]
# ```python
# array([[2., 2., 2.],
#        [2., 2., 2.]])
# ```

# %%
np.ones((2, 3)) * 2.0


# %% [markdown]
# ```python
# array([[2., 1., 1.],
#        [1., 2., 1.],
#        [1., 1., 2.]])
# ```

# %%
np.ones([3, 3]) + np.identity(3)


# %% [markdown]
# ```python
# array([[0., 1., 1., 1.],
#        [1., 0., 1., 1.]])
# ```

# %%
np.ones((2, 4)) - np.eye(2, 4)
