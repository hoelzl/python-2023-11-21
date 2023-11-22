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
#  <b>Vererbung: Motivation</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 10 Vererbung Motivation.py -->
# <!-- python_courses/slides/module_200_object_orientation/topic_190_inheritance_intro.py -->

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
#  ## Motivation für Vererbung
#
# Wir haben folgende Klasse implementiert:

# %% tags=["keep"]
import random


# %% tags=["keep"]
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x:.1f}, {self.y:.1f})"

    def move(self, dx=0, dy=0):
        self.x += dx
        self.y += dy

    def randomize(self):
        self.x = random.gauss(2, 0.5)
        self.y = random.gauss(3, 0.5)


# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
p = Point(1, 1)
p

# %% tags=["keep"]
p.move(2, 3)
p

# %% tags=["keep"]
p.randomize()
p


# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
def build_rectangle(left_lower: Point, right_upper: Point):
    return [left_lower, right_upper]


# %% tags=["keep"]
build_rectangle(Point(0, 0), Point(1, 1))


# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# Wie können wir farbige Punkte einführen?

# %% tags=["alt"]
class ColorPoint:
    def __init__(self, x=0, y=0, color="black"):
        self.x = x
        self.y = y
        self.color = color

    def __repr__(self):
        return f"ColorPoint({self.x:.1f}, {self.y:.1f}, {self.color!r})"

    def move(self, dx=0, dy=0):
        self.x += dx
        self.y += dy

    def randomize(self):
        self.x = random.gauss(2, 0.5)
        self.y = random.gauss(3, 0.5)


# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
cp = ColorPoint(2, 3)
# cp

# %% tags=["keep"]
assert cp.x == 2.0
assert cp.y == 3.0
assert cp.color == "black"

# %% tags=["keep"]
cp.color = "red"

# %% tags=["keep"]
assert cp.x == 2.0
assert cp.y == 3.0
assert cp.color == "red"

# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
cp.move(2, 3)
# cp


# %% tags=["keep"]
assert cp.x == 4.0
assert cp.y == 6.0
assert cp.color == "red"

# %% tags=["keep"]
cp.randomize()
# cp

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### Probleme
#
# - Code-Duplizierung
# - Das Python Typsystem weiß nicht, dass `ColorPoint` ein `Point` ist:

# %% tags=["keep"]
isinstance(Point(0, 0), Point)

# %% tags=["keep"]
isinstance(ColorPoint(0, 0), Point)


# %% tags=["keep"]
build_rectangle(ColorPoint(0, 0), ColorPoint(1, 1))

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### Welche Lösungen gibt es?
#
# - Vererbung: `ColorPoint` erbt von `Point`
# - Protokolle: `ColorPoint` und `Point` implementieren das gleiche Protokoll
#
# Ergebnis: Subtyp- bzw. Konsistenz-Beziehung
