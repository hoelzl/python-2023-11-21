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
#  <b>Methoden</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 04 Methoden.py -->
# <!-- python_courses/slides/module_200_object_orientation/topic_130_a2_methods.py -->

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
# ## Methoden
#
# - Klassen können Methoden enthalten.
# - Methoden sind Funktionen, die "zu einem Objekt gehören".
# - In Python gibt es kein implizites `this`.
# - Methoden werden mit der "Dot-Notation" aufgerufen: `my_object.method()`.

# %% tags=["keep"]
class MyClass:
    def method(self):
        print(f"Called method on {self}")


# %% tags=["keep"]
my_object = MyClass()
my_object.method()
print(repr(my_object))

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Wir können eine Methode zum Verschieben eines Punktes zu unserer `Point`
# Klasse hinzufügen:

# %% tags=["alt"]
# noinspection PyRedeclaration
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx=0.0, dy=0.0):
        self.x += dx
        self.y += dy


# %% tags=["keep"]
def print_point(p):
    print(f"Point: x = {p.x}, y = {p.y}")


# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
p = Point(2, 3)
print_point(p)

# %%
p.move(3, 5)
print_point(p)


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Workshop: Kraftfahrzeuge (Teil 2)
#
# In Teil 1 haben wir die folgende Klasse `Kfz` definiert:
#
# ```python
# class Kfz:
#     def __init__(self, hersteller, kennzeichen):
#         self.hersteller = hersteller
#         self.kennzeichen = kennzeichen
# ```


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Erweitern Sie diese Klasse um eine Methode
#
# `melde_um(self, neues_kennzeichen)`,
#
# die das Kennzeichen des Fahrzeugs ändert.


# %% lang="de" tags=["alt"]
class Kfz:
    def __init__(self, hersteller, kennzeichen):
        self.hersteller = hersteller
        self.kennzeichen = kennzeichen

    def melde_um(self, neues_kennzeichen):
        self.kennzeichen = neues_kennzeichen


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Mit der folgenden Funktion können wir Fahrzeuge ausdrucken:

# %% lang="de" tags=["keep"]
def drucke_kfz(kfz: Kfz):
    print(f"Kfz: {kfz.hersteller} mit Kennzeichen {kfz.kennzeichen!r}")


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Wir können dann wieder folgende Instanzen erzeugen:

# %% lang="de" tags=["keep"]
bmw = Kfz("BMW", "M-BW 123")
bmw2 = Kfz("BMW", "M-BW 123")
vw = Kfz("VW", "WOB-VW 246")

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Melden Sie den oben erzeugten VW um, so dass er das neue Kennzeichen "BGL-A
# 9" hat. Wie können Sie feststellen ob das Ummelden die gewünschte Änderung
# hatte?

# %% lang="de"
vw.melde_um("BGL-A 9")

# %% lang="de"
# Z.B
assert vw.kennzeichen == "BGL-A 9" and vw.hersteller == "VW"
# Oder
drucke_kfz(vw)

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Melden Sie den in `bmw` gespeicherten BMW um (mit Kennzeichen "F-B 21"). Wirkt
# sich die Änderung auf das in `bmw2` gespeicherte KFZ aus?

# %% lang="de"
bmw.melde_um("F-B 21")

# %% lang="de"
drucke_kfz(bmw)
drucke_kfz(bmw2)
