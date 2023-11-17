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
#  <b>Properties</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 09 Properties.py -->
# <!-- python_courses/slides/module_200_object_orientation/topic_150_a2_properties.py -->

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
# ## Properties
#
# Wie können wir es ermöglichen auf einen Punkt sowohl mittels der `x` und
# `y`-Koordinaten zuzugreifen, als auch mittels Radius und Winkel?

# %% tk

# %% tk

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %% tags=["keep"]
assert p.x == 0.0
assert p.y == 0.0
assert p.get_radius() == 0.0
assert p.get_angle() == 0.0

# %%

# %% tags=["keep"]
assert p.x == 1.0
assert p.y == 0.0
assert p.get_radius() == 1.0
assert p.get_angle() == 0.0

# %%

# %% tags=["keep"]
from math import isclose, pi

assert p.x == 0.0
assert p.y == 2.0
assert p.get_radius() == 2.0
assert isclose(p.get_angle(), pi / 2)


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Es ist unschön, dass bei der Verwendung von `GeoPointV0` die Attribute `x` und `y`
# anders behandelt werden müssen als `radius` und `angle`:

# %%

# %% tags=["subslide", "start"] slideshow={"slide_type": "subslide"}
class GeoPointV1:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def get_radius(self):
        return math.hypot(self.x, self.y)

    def get_angle(self):
        return math.atan2(self.y, self.x)

    def __repr__(self):
        return (
            f"GeoPointV0({self.x:.1f}, {self.y:.1f}, "
            f"r={self.get_radius():.2f}, θ={self.get_angle():.2f})"
        )


# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %% tags=["keep"]
assert p.x == 0.0
assert p.y == 0.0
assert p.radius == 0.0
assert p.angle == 0.0

# %%

# %% tags=["keep"]
assert p.x == 1.0
assert p.y == 0.0
assert p.radius == 1.0
assert p.angle == 0.0

# %%

# %% tags=["keep"]
from math import isclose, pi

assert p.x == 0.0
assert p.y == 2.0
assert p.radius == 2.0
assert isclose(p.angle, pi / 2)


# %%

# %%

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Setter für Properties:
#
# Properties können auch modifiziert werden:

# %% tags=["subslide", "start"] slideshow={"slide_type": "subslide"}
class GeoPointV2:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    @property
    def radius(self):
        return (self.x**2 + self.y**2) ** 0.5

    @property
    def angle(self):
        return math.atan2(self.y, self.x)

    def __repr__(self):
        return (
            f"GeoPointV2({self.x:.1f}, {self.y:.1f}, "
            f"r={self.radius:.2f}, θ={self.angle:.2f})"
        )


# %%

# %% tags=["keep"]
assert p.radius == 10.0
