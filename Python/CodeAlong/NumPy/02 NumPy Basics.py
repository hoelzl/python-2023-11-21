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
#  <b>NumPy Basics</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 02 NumPy Basics.py -->
# <!-- python_courses/slides/module_600_numpy/topic_120_a5_np_basics.py -->

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# # Grundkonzepte von NumPy

# %% tags=["keep"]
import numpy as np

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Vektoren

# %% tags=["keep"]
v1 = np.array([3.0, 4.0, 5.0])
v2 = np.array([8.0, 7.0, 6.0])

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# - Vektoren sind vom Typ `numpy.ndarray`
# - Sie sind auf einen spezifischen Elementtyp spezialisiert
# - Ihre Anzahl von "Dimensionen" (ihr Rang) ist 1
# - Sie haben daher ein 1-Tupel als "Shape"

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %%

# %%

# %%

# %%

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Rechnen mit Vektoren
#
# ### Grundlegende Operationen
#
# - Numpy unterstützt die grundlegenden mathematischen Operationen auf Vektoren
#   gleicher Dimension
# - Sie werden **elementweise** ausgeführt

# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
v1 = np.array([3.0, 4.0, 5.0])
v2 = np.array([8.0, 7.0, 6.0])

# %%

# %%

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Mathematische Operationen können auch auf NumPy Arrays und Skalare angewendet
# werden:

# %% tags=["keep"]
v1

# %%

# %%


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### Skalarprodukt
#
# Das Skalarprodukt wird mit der `dot()` Methode oder mit dem `@`-Operator
# gebildet

# %%

# %%

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# ## Mini-Workshop: Rechnen mit Vektoren
#
# Erzeugen Sie die folgenden Vektoren:
#
# $$
# \mathit{vec}_1 = \left(\begin{matrix}
#                    3.0\\ 1.5\\ 2.0\\ 4.5\end{matrix}\right)
# \qquad
# \mathit{vec}_2 = \left(\begin{matrix} 0.0\\ 0.1\\ 0.2\end{matrix}\right)
# \qquad
# \mathit{vec}_3 = \left(\begin{matrix} 6\\ 2\\ 3\\ 1\end{matrix}\right)
# \qquad
# \mathit{vec}_4 = \left(\begin{matrix} 3.0\\ 2.0\\ 1.0\end{matrix}\right)
# $$

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# - Welche dieser Vektoren können Sie elementweise miteinander addieren und
#   multiplizieren?
# - Berechnen Sie für diese Vektoren $\mathit{vec}_i * \mathit{vec}_j +
#   \mathit{vec}_i$ (für $i \neq j$)
# - Was passiert, wenn Sie versuchen mit anderen Kombinationen von Vektoren
#   rechnen?

# %% [markdown] lang="de" tags=["subslide", "answer"] slideshow={"slide_type": "subslide"}
# *Antwort:* 

# %%

# %%

# %% [markdown] lang="de" tags=["answer", "subslide"] slideshow={"slide_type": "subslide"}
# *Antwort:* 

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# (Ende des Workshops.)

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Gleichheit von Vektoren
#
# Auch der Vergleich von Vektoren mit `==` wird elementweise durchgeführt!


# %% tags=["keep"]
vec1 = np.array([0, 1, 2, 3])
vec2 = np.array([1, 1, 3, 3])


# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Das gilt auch für Vergleiche von Vektoren und Listen:

# %% tags=["keep"]
vec1 == [1, 1, 3, 3]

# %% tags=["keep"]
vec2 == [1, 1, 3, 3]


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Mit den `all()` (und `any()`) Methoden kann man überprüfen, ob alle Elemente
# truthy sind (bzw. ob mindestens ein Element truthy ist):

# %%

# %%


# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %%

# %%


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### Extrema und ihre Position
#
# - Maximum und minimum können mit den `max()` und `min()`-Methoden berechnet
#   werden
# - Ihre Position erhält man mit den `argmax()` und `argmin()`-Methoden

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %%

# %%

# %%

# %%

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# ## Mini-Workshop: Extrema
#
# Gegeben sei der folgende Vektor:


# %% tags=["keep"]
vec = np.array([1, 0, 8, 5, 2, 8, 3, 0, 1])

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# - Was sind Länge, Anzahl der Dimensionen, Shape und Elementtyp von `vec`?
# - Was sind kleinstes und größtes Element von `vec`?
# - An welcher Position kommen diese Elemente vor?
# - Erzeugen Sie einen Vektor `vec_max` der die gleiche Länge hat, wie `vec` und
#   für den gilt
#   - `vec_max[i]` = `True`, wenn `vec[i]` = `min(vec)`
#   - `vec_max[i]` = `False`, sonst

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %%

# %%

# %%

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %%

# %%

# %%

# %%

# %%

# %% [markdown] lang="de"
#
# (Ende des Workshops.)

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# `argmin()` und `argmax()` geben nur den ersten Index zurück. Um alle Indizes
# des minimalen Elements zu bekommen muss man anders vorgehen. Hier ein
# Ausblick; wir werden die verwendeten Techniken später genauer besprechen.
#
# Ein boolesches Array (oder eine boolesche Liste) kann verwendet werden, um
# Elemente aus einem Vektor zu selektieren:

# %% tags=["keep"]
my_vec = np.array([1, 2, 3, 4])

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Idee für die Selektion aller Indizes des minimalen Elements:
# - Erzeuge ein boolesches Array
#   - `True` an allen Positionen, an denen das minimale Element steht
#   - `False` sonst
# - Erzeuge ein Array mit den Indizes: `[0, 1, 2, ..., len(vec) - 1]`
# - Selektiere die minimal Indizes mit dem booleschen Array

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %%

# %%

# %%

# %%

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %% [markdown] lang="de"
#
# (Das kann man mit `np.arange()` kürzer ausdrücken.)

# %%

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %%
