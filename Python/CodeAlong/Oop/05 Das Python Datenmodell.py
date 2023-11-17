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
#  <b>Das Python Datenmodell</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 05 Das Python Datenmodell.py -->
# <!-- python_courses/slides/module_200_object_orientation/topic_134_python_data_model.py -->

# %% tags=["slide", "keep"] slideshow={"slide_type": "slide"}
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx=0.0, dy=0.0):
        self.x += dx
        self.y += dy


# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
p = Point(2, 5)


# %%

# %%

# %%

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# # Das Python Datenmodell
#
# Mit Dunder-Methoden können benutzerdefinierten Datentypen benutzerfreundlicher
# gestaltet werden.

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Durch Definition der Methode `__repr__(self)` kann der von `repr`
# zurückgegebene String für benutzerdefinierte Klassen angepasst werden: Der
# Funktionsaufruf `repr(x)` überprüft, ob `x` eine Methode `__repr__` hat und
# ruft diese auf, falls sie existiert.

# %% tags=["subslide", "start"] slideshow={"slide_type": "subslide"}
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx=0, dy=0):
        self.x += dx
        self.y += dy


# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Entsprechend kann eine `__str__()` Methode definiert werden, die von `str()`
# verwendet wird. Die Funktion `str()` delegiert an `__repr__()`, falls keine
# `__str__()`-Methode definiert ist:
#

# %% tags=["keep"]
p = Point(2, 5)
print(repr(p))

# %% tags=["keep"]
print(str(p))


# %% tags=["subslide", "start"] slideshow={"slide_type": "subslide"}
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x!r}, {self.y!r})"

    def move(self, dx=0, dy=0):
        self.x += dx
        self.y += dy


# %% tags=["keep"]
p = Point(2, 5)
print(repr(p))

# %% tags=["keep"]
print(str(p))


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Python bietet viele Dunder-Methoden an: siehe das
# [Python Datenmodell](https://docs.python.org/3/reference/datamodel.html)
# in der Dokumentation.


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Durch Definition der Methode `__eq__()` kann das Verhalten von Tests mit `==`
# angepasst werden:

# %% tags=["subslide", "start"] slideshow={"slide_type": "subslide"}
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x!r}, {self.y!r})"

    def move(self, dx=0, dy=0):
        self.x += dx
        self.y += dy


# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
p = Point(2, 5)

# %%

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# # Kraftfahrzeuge (Teil 3)
#
# In Teil 2 haben wir die folgende Klasse `Kfz` definiert:
#
# ```python
# >>> class Kfz:
# ...     def __init__(self, hersteller, kennzeichen):
# ...         self.hersteller = hersteller
# ...         self.kennzeichen = kennzeichen
# ...
# ...     def melde_um(self, neues_kennzeichen):
# ...         self.kennzeichen = neues_kennzeichen
# ```
#


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Verbessern Sie die Klasse `Kfz` indem Sie
# - Eine `__repr__()` Methode implementieren, die eine geeignete Repräsentation
#   des Fahrzeugs zurückgibt.
# - Eine `__eq__()` Methode implementieren, die die Werte der Attribute zweier
#   Fahrzeuge vergleicht.
#
# Führen Sie die Beispiele mit der verbesserten Klasse aus.

# %% lang="de" tags=["subslide", "start"] slideshow={"slide_type": "subslide"}
class Kfz:
    def __init__(self, hersteller, kennzeichen):
        self.hersteller = hersteller
        self.kennzeichen = kennzeichen

    def melde_um(self, neues_kennzeichen):
        self.kennzeichen = neues_kennzeichen


# %% lang="de" tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
bmw = Kfz("BMW", "M-BW 123")
bmw

# %% lang="de" tags=["keep"]
bmw2 = Kfz("BMW", "M-BW 123")
bmw2

# %% lang="de" tags=["keep"]
assert bmw == bmw2

# %% lang="de" tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
vw = Kfz("VW", "WOB-VW 246")
vw

# %% lang="de" tags=["keep"]
vw.melde_um("BGL-A 9")
vw

# %% lang="de" tags=["keep"]
assert vw.kennzeichen == "BGL-A 9" and vw.hersteller == "VW"

# %% lang="de" tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
bmw.melde_um("F-B 21")
bmw

# %% lang="de" tags=["keep"]
assert bmw != bmw2

