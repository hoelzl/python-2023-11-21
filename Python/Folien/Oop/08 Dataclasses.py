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
#  <b>Dataclasses</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 08 Dataclasses.py -->
# <!-- python_courses/slides/module_200_object_orientation/topic_140_a3_dataclasses.py -->

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
# ## Dataclasses
#
# Definition einer Klasse, in der Attribute besser sichtbar sind, Repräsentation
# und Gleichheit vordefiniert sind, etc.
#
# Die [Dokumentation](https://docs.python.org/3/library/dataclasses.html)
# beinhaltet weitere Möglichkeiten.

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
from dataclasses import dataclass


# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
@dataclass
class DataPoint:
    x: float
    y: float


# %%
dp = DataPoint(2, 3)
dp

# %%
dp1 = DataPoint(1, 1)
dp2 = DataPoint(1, 1)
print(dp1 == dp2)
print(dp1 is dp2)


# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
from dataclasses import field


@dataclass
class Point3D:
    x: float = field(default=0.0)
    y: float = field(default=0.0)
    z: float = 0.0  # Python >= 3.10

    def move(self, dx=0.0, dy=0.0, dz=0.0):
        self.x += dx
        self.y += dy
        self.z += dz


# %%
p3d = Point3D(1.0, 2.0)
p3d

# %%
p3d.move(dy=1.0, dz=5.0)
p3d

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
@dataclass(frozen=True)
class FrozenPoint:
    x: float = field(default=0.0)
    y: float = field(default=0.0)


# %%
fp = FrozenPoint()
fp

# %%
# fp.x = 1.0

# %%
import dataclasses

# %%
dataclasses.replace(fp, x=1.0)

# %%
fp2 = dataclasses.replace(fp, x=1.0, y=2.0)
fp2

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Dataclasses erzwingen, dass Default-Werte unveränderlich sind
# (zumindest für einige Typen...):

# %%
from dataclasses import dataclass, field


# %%
@dataclass
class DefaultDemo:
    # items: list = []
    items: list = field(default_factory=list)


# %%
d1 = DefaultDemo()
d2 = DefaultDemo()

# %%
d1.items.append(1234)
print(d1)
print(d2)


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Der Test auf unveränderliche Defaults funktioniert aber nur für einige Typen aus
# der Standardbibliothek, nicht für benutzerdefinierte Typen:

# %%
@dataclass
class BadDefault:
    point: Point3D = Point3D(0.0, 0.0)


# %%
bd1 = BadDefault()
bd2 = BadDefault()
bd1, bd2

# %%
bd1.point.move(1.0, 2.0)
bd1, bd2


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Es ist möglich, komplexere Initialisierungen vorzunehmen:
#
# - Die `__post_init__()` Methode kann Code zur Initialisierung von Objekten
#   enthalten, der nach der generierten `__init__()` Methode ausgeführt wird.
# - Der Typ `InitVar[T]` deklariert, dass ein Klassen-Attribut als Argument an
#   `__post_init__()` übergeben und nicht als Instanz-Attribut verwendet wird.
# - Das Keyword-Argument `init=False` für `field()` bewirkt, dass ein Attribut
#   nicht in der generierten `__init__()` Methode initialisiert wird.

# %%
from dataclasses import dataclass, field, InitVar

# %% tags=["keep"]
@dataclass
class DependentInit:
    x: InitVar[float] = 0.0
    y: InitVar[float] = 0.0
    z: InitVar[float] = 0.0
    point: Point3D = field(init=False)

    def __post_init__(self, x, y, z):
        self.point = Point3D(x, y, z)


# %%
bd1 = DependentInit()
bd1

# %%
bd2 = DependentInit(1.0, 2.0, 3.0)
bd2

# %%
bd1.point.move(3.0, 5.0)
bd1, bd2

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
# # Workshop: Einkaufsliste
#
# In dieser Aufgabe wollen wir eine Einkaufsliste definieren, die geplante
# Einkäufe verwalten kann. Eine Einkaufsliste soll aus Einträgen bestehen, die
# ein Produkt und die davon benötigte Menge enthalten.
#
# Es sollen sowohl die Einkaufsliste selber als auch die Einträge durch
# benutzerdefinierte Datentypen repräsentiert werden.
#
# Falls Sie die Lösung als Python-Projekt statt als Notebook implementieren wollen,
# ist in `examples/ShoppingListStarterKit` in Projektgerüst, das Sie als
# Startpunkt hernehmen können. In `examples/ShoppingList` ist ein Lösungsvorschlag.
#
# Definieren Sie zunächst eine Klasse `ShoppingListItem`, die Attribute
# `product: str` und `amount: str` hat.
# Verwenden Sie dazu den `@dataclass` Decorator

# %%
from dataclasses import dataclass


@dataclass
class ShoppingListItem:
    product: str
    amount: str = "1"


# %% [markdown] lang="de"
# Erzeugen sie ein `ShoppingListItem`, das 500g Kaffee repräsentiert:

# %%
ShoppingListItem("Kaffee", "500g")

# %% [markdown] lang="de"
#
# Definieren Sie eine Klasse `ShoppingList`, die eine Liste von
# `ShoppingListItem`-Instanzen beinhaltet:
#
# - Verwenden Sie den `@dataclass` Decorator
# - Die Klasse hat ein Attribut `items` vom Typ `list`
#   (oder `list[ShoppingListItem]`, falls
#   Sie Python 3.9 oder neuer verwenden), das mit einer leeren Liste
#   Initialisiert wird.
# - Die Methode `add_item(self, item: ShoppingListItem)` fügt ein
#   `ShoppingListItem` zur Einkaufsliste hinzu.
#
# Implementieren Sie eine
# [`__str__()`-Methode](https://docs.python.org/3/reference/datamodel.html#object.__str__),
# so dass das folgende Programm:
#
# ```python
# meine_einkaufsliste = ShoppingList([ShoppingListItem('Tee', '2 Pakete'),
#                                     ShoppingListItem('Kaffee', '1 Paket')])
# print(str(meine_einkaufsliste))
# print(repr(meine_einkaufsliste))
# ```
#
# Folgende Ausgabe erzeugt:
#
# ```
# Einkaufsliste
#   Tee, (2 Pakete)
#   Kaffee, (1 Paket)
#
# ShoppingList(items=[ShoppingListItem(product='Tee', amount='2 Pakete'), ShoppingListItem(product='Kaffee', amount='1 Paket')])
# ```
#
# Implementieren Sie eine Methode für `__len__()`, die die Länge der
# Einkaufsliste zurückgibt, und für `__getitem__()`, die den Zugriff auf
# Einträge über ihren numerischen Index erlaubt.

# %%
from dataclasses import field


@dataclass
class ShoppingList:
    items: list[ShoppingListItem] = field(default_factory=list)

    def __str__(self):
        result = "Einkaufsliste\n"
        for item in self.items:
            result += f"  {item.product}, ({item.amount})\n"
        return result

    def __len__(self):
        return len(self.items)

    def __getitem__(self, n):
        return self.items[n]

    def add_item(self, item):
        self.items.append(item)


# %% [markdown] lang="de"
#
# Definieren Sie Variable `meine_einkaufsliste`, die eine Einkaufsliste mit
# folgenden ShoppingListItems repräsentiert:
#
# - 2 Pakete Tee,
# - 1 Paket Kaffee
#
# Überprüfen Sie, dass sich `str()` und `repr()` wie oben beschrieben verhalten.

# %%
meine_einkaufsliste = ShoppingList(
    [ShoppingListItem("Tee", "2 Pakete"), ShoppingListItem("Kaffee", "1 Paket")]
)
print(str(meine_einkaufsliste))
print(repr(meine_einkaufsliste))

# %% [markdown] lang="de"
# Drucken Sie `meine_einkaufsliste` aus. Entspricht die Ausgabe Ihren Erwartungen?

# %%
print(meine_einkaufsliste)

# %% [markdown] lang="de"
#
# Stellen Sie fest, wie lange `meine_einkaufsliste` ist und
# was ihr erstes und zweites Element sind:

# %%
print(len(meine_einkaufsliste))
print(meine_einkaufsliste[0])
print(meine_einkaufsliste[1])

# %% [markdown] lang="de"
#
# Was ist der Effekt des folgenden Ausdrucks?
# ```python
#   for item in meine_einkaufsliste:
#       print(item)
# ```

# %%
for item in meine_einkaufsliste:
    print(item)

# %% [markdown] lang="de"
#
# Erweitern Sie die Definition der Klasse `ShoppingList`, so dass der Indexing
# Operator `[]` auch mit einem String aufgerufen werden kann, und das Shopping List
# Item mit dem entsprechenden `product` Attribut zurückgibt, falls es existiert,
# oder `None` falls kein solches Item existiert.
#
# Verifizieren Sie, dass ihre neue Implementierung des Indexing Operators für Integer
# und String Argumente funktioniert.
#
# *Hinweis:* Sie können die `isinstance()` Funktion verwenden um zu überprüfen,
# ob ein Objekt ein String ist:

# %%
print(isinstance("abc", str))
print(isinstance(123, str))


# %%
@dataclass
class ShoppingList:
    items: list[ShoppingListItem] = field(default_factory=list)

    def __str__(self):
        result = "Einkaufsliste\n"
        for item in self.items:
            result += f"  {item.product}, ({item.amount})\n"
        return result

    def __len__(self):
        return len(self.items)

    def __getitem__(self, n):
        if isinstance(n, str):
            return self.find_product(n)
        return self.items[n]

    def find_product(self, product: str):
        for item in self.items:
            if item.product == product:
                return item
        return None

    def add_item(self, item):
        self.items.append(item)


# %%
meine_einkaufsliste = ShoppingList(
    [ShoppingListItem("Tee", "2 Pakete"), ShoppingListItem("Kaffee", "1 Paket")]
)
print(meine_einkaufsliste[0])
print(meine_einkaufsliste["Tee"])
print(meine_einkaufsliste["Marmelade"])

# %% [markdown] lang="de"
#
# Fügen Sie  250g Butter und  1 Laib Brot zur Einkaufsliste
# `meine_einkaufsliste` hinzu.

# %%
meine_einkaufsliste.add_item(ShoppingListItem("Butter", "250g"))
meine_einkaufsliste.add_item(ShoppingListItem("Brot", "1 Laib"))
meine_einkaufsliste

# %% [markdown] lang="de"
# Drucken Sie die Einkaufsliste nochmal aus.

# %%
print(meine_einkaufsliste)

# %% [markdown] lang="de"
#
# Was passiert, wenn Sie `Butter` und `Brot` nochmals zur Einkaufsliste
# `meine_einkaufsliste` hinzufügen?

# %%
meine_einkaufsliste.add_item(ShoppingListItem("Butter", "250g"))
meine_einkaufsliste.add_item(ShoppingListItem("Brot", "1 Laib"))
print(meine_einkaufsliste)

# %% [markdown] lang="de"
# *Diskussion:* Wie könnte das Verhalten der Klasse verbessert werden?
