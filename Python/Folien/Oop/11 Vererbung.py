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
#  <b>Vererbung</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 11 Vererbung.py -->
# <!-- python_courses/slides/module_200_object_orientation/topic_192_inheritance.py -->

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
#  ## Vererbung
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


# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# Wie können wir farbige Punkte einführen, ohne die komplette Funktionalität
# von `Point` neu implementieren zu müssen?

# %%
class ColorPoint(Point):
    def __init__(self, x=0, y=0, color="black"):
        super().__init__(x, y)
        self.color = color

    def __repr__(self):
        return f"ColorPoint({self.x:.1f}, {self.y:.1f}, {self.color!r})"

    def randomize(self):
        super().randomize()
        self.color = random.choice(["black", "red", "green", "blue", "yellow", "white"])


# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
cp = ColorPoint(2, 3)
assert isinstance(cp, Point)
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

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# ## Workshop: Mitarbeiter
#
# Im Folgenden soll eine Klassenhierarchie für Mitarbeiter einer Firma erstellt
# werden:
#
# - Mitarbeiter können entweder Arbeiter oder Manager sein
# - Jeder Mitarbeiter der Firma hat einen Namen, eine Personalnummer und ein
#   Grundgehalt
# - Für jeden Arbeiter werden die angefallenen Überstunden und der Stundenlohn
#   gespeichert.
# - Das Gehalt eines Arbeiters berechnet sich als das 13/12-fache des
#   Grundgehalts plus der Bezahlung für die Überstunden
# - Jeder Manager hat einen individuellen Bonus
# - Das Gehalt eines Managers berechnet sich als das 13/12-fache des
#   Grundgehalts plus Bonus
#
# Implementieren Sie Python Klassen `Mitarbeiter`, `Arbeiter` und `Manager` mit
# geeigneten Attributen und einer Methode `gehalt()`, die das Gehalt berechnet.
#

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
from dataclasses import dataclass

# %%
@dataclass
class Mitarbeiter:
    name: str
    pers_nr: str
    grundgehalt: float

    def gehalt(self):
        return 13 / 12 * self.grundgehalt


# %%
@dataclass
class Arbeiter(Mitarbeiter):
    überstunden: float = 0.0
    stundensatz: float = 0.0

    def gehalt(self):
        return super().gehalt() + self.überstunden * self.stundensatz


# %%
@dataclass
class Manager(Mitarbeiter):
    bonus: float

    def gehalt(self):
        return super().gehalt() + self.bonus


# %% [markdown]
#
# Erzeugen Sie einen Arbeiter mit Namen Hans, Personalnummer 123, einem
# Grundgehalt von  36000.0 Euro, der 3.5 Überstunden zu je 40.0 Euro gearbeit
# hat. Drucken Sie das Gehalt aus.

# %%
a = Arbeiter("Hans", "123", 36_000, 3.5, 40.0)
print(a.gehalt())
a

# %% [markdown]
#
# Schreiben sie Assertions, die die Funktionalität der Klasse `Arbeiter` testen.

# %%
# Diese Assertions sind überflüssig!
assert a.name == "Hans"
assert a.pers_nr == "123"
assert a.grundgehalt == 36_000
assert a.überstunden == 3.5
assert a.stundensatz == 40.0

# Diese Assertion sollte vorhanden sein
assert a.gehalt() == 39_140.0

# %% [markdown]
#
# Erzeugen Sie einen Manager mit Namen Sepp, Personalnummer 843, der ein
# Grundgehalt von 60000.0 Euro und einen Bonus von 30000.0 Euro hat. Drucken Sie
# das Gehalt aus.

# %%
m = Manager("Sepp", "843", 60_000.0, 30_000.0)
print(m.gehalt())
m

# %% [markdown] lang="de"
# Testen Sie die Funktionalität der `Manager` Klasse.

# %%
assert m.gehalt() == 95_000.0


# %% [markdown] tags=["alt"]
# ## Lösung ohne Dataclasses:

# %% tags=["alt"]
class Mitarbeiter:
    def __init__(self, name, pers_nr, grundgehalt):
        self.name = name
        self.pers_nr = pers_nr
        self.grundgehalt = grundgehalt

    def gehalt(self):
        return 13 / 12 * self.grundgehalt


# %% tags=["alt"]
class Arbeiter(Mitarbeiter):
    def __init__(self, name, pers_nr, grundgehalt, überstunden, stundensatz):
        super().__init__(name, pers_nr, grundgehalt)
        self.überstunden = überstunden
        self.stundensatz = stundensatz

    def __repr__(self):
        return (
            f"Arbeiter({self.name!r}, {self.pers_nr!r}, {self.grundgehalt}, "
            f"{self.überstunden}, {self.stundensatz})"
        )

    def gehalt(self):
        return super().gehalt() + self.überstunden * self.stundensatz


# %% tags=["alt"]
class Manager(Mitarbeiter):
    def __init__(self, name, pers_nr, grundgehalt, bonus):
        super().__init__(name, pers_nr, grundgehalt)
        self.bonus = bonus

    def __repr__(self):
        return (
            f"Manager({self.name!r}, {self.pers_nr!r}, {self.grundgehalt}, "
            f"{self.bonus})"
        )

    def gehalt(self):
        return super().gehalt() + self.bonus


# %% tags=["alt"]
a = Arbeiter("Hans", 123, 36_000, 3.5, 40)

# %%
assert a.gehalt() == 39_140.0


# %% tags=["alt"]
m = Manager("Sepp", 843, 60_000, 30_000)

# %%
assert m.gehalt() == 95_000.0
# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Eine Visualisierung für `super()`-Aufrufe bei Vererbung mit Python Tutor
# ist [hier](shorturl.at/efDKW).
