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
int_vector.shape

# %%
small_float_vector.shape

# %%
int_matrix.shape

# %%
tensor.shape

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Das Attribut `size` gibt die Anzahl der Elemente zurück.
#
# Die `len()`-Funktion gibt nur bei 1-dimensionalen Arrays die Anzahl der
# Elemente zurück, sonst die Anzahl der Zeilen!

# %%
len(int_vector)

# %%
int_vector.size

# %%
float_vector.size

# %%
small_float_vector.size

# %%
len(int_matrix)

# %%
int_matrix.size

# %%
len(tensor)

# %%
tensor.size

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Mit dem Attribut `itemsize` kann man den Speicherplatz bestimmen, der von einem
# Element belegt wird.

# %%
int_vector.itemsize

# %%
float_vector.itemsize

# %%
small_float_vector.itemsize

# %%
int_matrix.itemsize

# %%
tensor.itemsize

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Die `np.info()`-Funktion gibt die interessantesten Informationen über Arrays aus.

# %%
np.info(int_vector)

# %%
np.info(float_vector)

# %%
np.info(small_float_vector)

# %%
np.info(int_matrix)

# %%
np.info(tensor)

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Ändern von Shape und Größe
#
# ### Ändern des Shapes

# %%
float_vector.shape

# %%
float_matrix = float_vector.reshape((6, 6))

# %%
float_matrix

# %%
float_matrix.shape

# %%
float_vector

# %%
np.info(float_matrix)

# %%
float_matrix.reshape(3, 12)

# %%
# float_vector.reshape(20, 20)

# %%
m1 = float_vector.reshape(3, 12)
m1

# %%
np.info(m1)

# %%
m2 = float_vector.reshape(3, 12, order="F")
m2

# %%
np.info(m2)

# %%
v = np.arange(3)
v

# %%
v.shape

# %%
v.reshape(3, 1)

# %%
v.reshape(-1, 1)

# %%
float_vector.shape

# %%
float_vector.reshape(2, 6, 3)

# %%
float_vector.reshape(2, -1, 3)

# %%
float_vector.reshape(2, 6, -1)

# %%
# float_vector.reshape(2, -1, -1)

# %%
v.reshape(3, 1)

# %%
v.reshape(1, 3)

# %%
v.reshape(1, 3, 1)

# %%
vt = v.reshape(1, 3, 1, 1)
vt

# %%
vt.squeeze()

# %%
vt.squeeze().shape

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
# float_vector.resize(10, 10)

# %%
int_vector.resize(10, 10)

# %%
int_vector

# %%
np.info(int_vector)

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# `np.resize()` ist ähnlich zur `resize()` Methode, aber:
#
# - das ursprüngliche Array wird nicht verändert
# - die Werte werden zyklisch kopiert, wenn das Array vergrößert wird

# %%
np.resize(float_vector, (10, 10))

# %%
float_vector

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Mit der `np.pad()`-Funktion kann ein Array in ein größeres Array eingebettet
# werden:

# %%
v = np.array([1, 2, 3])

# %%
np.pad(v, (2, 3), "constant", constant_values=(0, 4))

# %%
v

# %%
a = np.array([[10, 20], [30, 40], [50, 60]])
a

# %%
np.pad(
    a,
    [[1, 2], [3, 4]],
    "constant",  # type: ignore #
    constant_values=((11, 22), (33, 44)),
)


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Transponieren von Matrizen

# %%
float_matrix

# %%
float_matrix.T

# %%
int_matrix

# %%
int_matrix.T

# %%
tensor

# %%
np.set_printoptions(precision=2)

# %%
tensor

# %%
tensor.T

# %%
tensor.shape, tensor.T.shape

# %%
tensor[1, 2, 3], tensor.T[3, 2, 1]

# %%
tensor

# %%
tensor2 = tensor.transpose((1, 2, 0))
tensor2

# %%
tensor2.shape

# %%
tensor[1, 2, 3], tensor2[2, 3, 1]

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Mini-Workshop: Reshaping Arrays
#
# Gegeben seien die folgenden Arrays:


# %%
vec = np.arange(9)
mat = np.arange(16).reshape((2, 8))

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
tensor = vec.reshape((3, 1, 3, 1))
tensor

# %%
tensor.squeeze()

# %%
np.resize(vec, (2, 9))

# %%
mat_square = mat.reshape((4, 4))
mat_square

# %%
mat_square_fortran = mat.reshape(-1).reshape((4, 4), order="F")
mat_square_fortran

# %%
assert (mat_square_fortran == mat_square.T).all()
