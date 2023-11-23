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
#  <b>Datenmodell: Vector</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 06 Datenmodell Vector.py -->
# <!-- python_courses/slides/module_200_object_orientation/topic_135_data_model_vector.py -->

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# # Datenmodell: Vector

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Beispiel: `Vektor`-Klasse
#
# Wir demonstrieren einige Dunder-Methoden, indem wir eine Klasse für 2D-Vektoren
# definieren:

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
import math


# %%
class Vector2D:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vector2D({self.x!r}, {self.y!r})"

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Vector2D):
            return self.x == other.x and self.y == other.y
        return False

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if isinstance(other, Vector2D):
            return Vector2D(self.x * other.x, self.y * other.y)
        return Vector2D(other * self.x, other * self.y)

    def __rmul__(self, other):
        """Called when the left operand of * is not a Vector2D instance.
        Python calls __rmul__ only if the left operand does not have a __mul__ method, 
        or that method does not know how to multiply with a Vector2D on the right."""
        return Vector2D(other * self.x, other * self.y)

    def __matmul__(self, other):
        return self.x * other.x + self.y * other.y

    def move(self, dx=0, dy=0):
        self.x += dx
        self.y += dy


# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
v1 = Vector2D(1, 2)
v2 = Vector2D(3, 4)
v3 = Vector2D(3, 4)

# %%
v1 == v2

# %%
v2 == v3

# %%
abs(v2)

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
v1 + v2

# %%
v1 - v2

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
v1, v2

# %%
# works only if __rmul__ is defined
3 * v1

# %%
v1 * 3

# %%
v1 * v2

# %%
v1 @ v2

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
v2

# %%
v2 += v1

# %%
v2
