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
#  <b>NumPy: Matrizen</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 04 NumPy Matrizen.py -->
# <!-- python_courses/slides/module_600_numpy/topic_128_a5_np_matrices.py -->

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Matrizen
#
# Matrizen können mit `np.array()` aus geschachtelten Listen erzeugt werden:

# %% tags=["keep"]
import numpy as np

# %% tags=["keep"]
m1 = np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
m1

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Form von Matrizen und Transposition

# %%
m1.ndim

# %%
m1.shape

# %%
m1

# %%
m1.T

# %%
m1.T.shape

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Reshaping

# %% tags=["keep"]
my_array = np.array([1, 2, 3, 4, 5, 6, 7, 8])
my_array

# %%
my_array.reshape((2, 4))

# %%
my_array.reshape(4, 2)

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Indizieren von Matrizen
#
# Numpy bietet die Möglichkeit mit eindimensionalen Indizes Zeilen aus einer
# Matrix zu extrahieren oder mit mehrdimensionalen Indizes direkt zu
# selektieren:

# %% tags=["keep"]
m1 = np.array(
    [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16],
    ]
)

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
m1

# %%
m1[1]

# %%
m1[1][1]

# %%
m1[1, 1]

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Slicing wird für ein- und mehrdimensionale Indizes unterstützt:

# %%
m1

# %%
m1[1:]

# %%
m1[1:, :2]

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
m1

# %%
m1[:, 0]

# %%
m1[1::2, ::3]

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### Rechnen mit Matrizen

# %% tags=["keep"]
m1 = np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
m1

# %% tags=["keep"]
m2 = np.array([[1.0, 0.0], [0.0, 1.0], [2.0, 3.0]])
m2

# %%
m1 + m1

# %%
m2 + m2

# %%
# m1 + m2

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
m1.T + m2

# %%
m1 + m2.T

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
# m1 * m2

# %%
m1.T * m2

# %%
m1.dot(m2)

# %%
m1 @ m2

# %%
m2 @ m1

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
m1

# %%
m1.sum()

# %%
m1.sum(axis=0)

# %%
m1.sum(axis=1)

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# ## Mini-Workshop: Rechnen mit Matrizen
#
# Erzeugen Sie die folgenden Matrizen:
#
# $$m_1 =
# \left(
# \begin{matrix}
#   1.0 & 2.0 & 3.0 & 4.0 \\
#   5.0 & 6.0 & 7.0 & 8.0
# \end{matrix}
# \right)
# \qquad
# m_2 =
# \left(
# \begin{matrix}
#   1 & 2 & 3 \\
#   4 & 5 & 6 \\
#   7 & 8 & 9
# \end{matrix}
# \right)
# $$

# %%
m1 = np.array([[1.0, 2.0, 3.0, 4.0], [5.0, 6.0, 7.0, 8.0]])

# %%
m2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# - Was sind Rang (Anzahl der Dimensionen), Shape und Elementtyp der beiden Matrizen?
# - Berechnen Sie $m_1 + m_1$ und $m_2 + m_2$
# - Berechnen Sie die elementweisen Produkte $m_1 * m_1$ und $m_2 * m_2$
# - Berechnen Sie die Produkte $m_1^T \cdot m_1$, $m_1 \cdot m_1^T$ und $m_2 \cdot m_2$


# %%
m1.ndim

# %%
m2.ndim

# %%
m1.shape

# %%
m2.shape

# %%
m1.dtype

# %%
m2.dtype

# %%
m1 * m1

# %%
m2 * m2

# %%
m1.T @ m1

# %%
m1 @ m1.T

# %%
m2 @ m2
