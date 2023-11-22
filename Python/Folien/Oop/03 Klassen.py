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
#  <b>Klassen</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 03 Klassen.py -->
# <!-- python_courses/slides/module_200_object_orientation/topic_120_a2_classes.py -->

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
# # Benutzerdefinierte Datentypen
#
# Wir wollen uns jetzt der Definition von benutzerdefinierten Datentypen (Klassen)
# zuwenden:


# %%
class PointV0:
    pass


# %% [markdown] lang="de"
#
# Klassennamen werden in Pascal-Case (d.h. groß und mit Großbuchstaben zur
# Trennung von Namensbestandteilen) geschrieben, z.B. `MyVerySpecialClass`.

# %% [markdown] lang="de"
#
# Wir verwenden im Folgenden [Python Tutor](https://tinyurl.com/python-classe-point-v0)
# um die Klasse `Point` zu implementieren.

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Instanzen von benutzerdefinierten Klassen werden erzeugt, indem man den
# Klassennamen als Funktion aufruft. Manche der Python Operatoren und
# Funktionen können verwendet werden ohne, dass zusätzliche Implementierungsarbeit
# nötig ist:

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
p1 = PointV0()
p1

# %%
print(p1)

# %%
p2 = PointV0()
p1 == p2

# %%
# Fehler
# p1 < p2

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Ähnlich wie Dictionaries neue Einträge zugewiesen werden können, kann man
# benutzerdefinierten Datentypen neue *Attribute* zuweisen, allerdings verwendet
# man die `.`-Notation statt der Indexing Notation `[]`:

# %%
# Möglich, aber nicht gut... / Possible but not good...
p1.x = 1.0
p1.y = 2.0
print(p1.x)
print(p1.y)


# %%
# Error!
# p2.x

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Im Gegensatz zu Dictionaries werden Instanzen von Klassen typischerweise
# *nicht* nach der Erzeugung beliebige Attribute zugewiesen!
#
# Statt dessen sollen allen Instanzen die gleiche Form haben. Deswegen werden
# die Attribute eines Objekts bei seiner Konstruktion initialisiert. Das geht
# über die `__init__()` Methode.
#
# Die `__init__()`-Methode hat immer
# (mindestens) einen Parameter, der per Konvention `self` heißt:

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
class PointV1:
    def __init__(self):
        self.x = 0.0
        self.y = 0.0


# %%
def print_point(name, p):
    print(f"{name}: x = {p.x}, y = {p.y}")


# %%
p1 = PointV1()
p2 = PointV1()
print_point("p1", p1)
print_point("p2", p2)

# %%
p1 == p2

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Die Werte von Attributen können verändert werden:

# %%
p1.x = 1.0
p1.y = 2.0
print_point("p1", p1)
print_point("p2", p2)


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# In vielen Fällen wäre es besser, bei der Konstruktion eines Objekts Werte für
# die Attribute anzugeben. Das ist möglich, indem man der `__init__()`-Methode
# zusätzliche Parameter gibt.

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
class PointV2:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# %%
p1 = PointV2(2.0, 3.0)
p2 = PointV2(0.0, 0.0)
print_point("p1", p1)
print_point("p2", p2)


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# # Kraftfahrzeuge (Teil 1)
#
# Definieren Sie eine Klasse `Kfz`, deren Instanzen Kraftfahrzeuge beschreiben.
# Jedes KFZ soll Attribute `hersteller` und `kennzeichen` haben.


# %% lang="de"
class Kfz:
    def __init__(self, hersteller, kennzeichen):
        self.hersteller = hersteller
        self.kennzeichen = kennzeichen


# %% [markdown] lang="de"
#
# Erzeugen Sie zwei Kraftfahrzeuge:
# - einen BMW mit Kennzeichen "M-BW 123"
# - einen VW mit Kennzeichen "WOB-VW 246"
# und speichern Sie sie in Variablen `bmw` und `vw`

# %% lang="de"
bmw = Kfz("BMW", "M-BW 123")
vw = Kfz("VW", "WOB-VW 246")

# %% [markdown] lang="de"
#
# Erzeugen Sie eine neue Instanz von `Kfz` mit Hersteller BMW und Kennzeichen
# "M-BW 123" und speichern Sie sie in einer Variablen `bmw2`.

# %% lang="de"
bmw2 = Kfz("BMW", "M-BW 123")

# %% [markdown] lang="de"
#
# Wie können Sie feststellen, ob `bmw` und `bmw2` (bzw. `bmw` und `vw`) das
# gleiche Fahrzeug beschreiben?

# %% lang="de"
bmw.hersteller == bmw2.hersteller and bmw.kennzeichen == bmw2.kennzeichen

# %% lang="de"
bmw.hersteller == vw.hersteller and bmw.kennzeichen == vw.kennzeichen
