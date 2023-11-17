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

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %%

# %%


# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %%

# %%

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %%

# %%

# %%

# %%

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Dataclasses erzwingen, dass Default-Werte unveränderlich sind
# (zumindest für einige Typen...):

# %%

# %%

# %%

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Der Test auf unveränderliche Defaults funktioniert aber nur für einige Typen aus
# der Standardbibliothek, nicht für benutzerdefinierte Typen:

# %%

# %%

# %%


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

# %%

# %%

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

# %% [markdown] lang="de"
# Erzeugen sie ein `ShoppingListItem`, das 500g Kaffee repräsentiert:

# %%

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

# %% [markdown] lang="de"
# Drucken Sie `meine_einkaufsliste` aus. Entspricht die Ausgabe Ihren Erwartungen?

# %%

# %% [markdown] lang="de"
#
# Stellen Sie fest, wie lange `meine_einkaufsliste` ist und
# was ihr erstes und zweites Element sind:

# %%

# %% [markdown] lang="de"
#
# Was ist der Effekt des folgenden Ausdrucks?
# ```python
#   for item in meine_einkaufsliste:
#       print(item)
# ```

# %%

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

# %%

# %%

# %% [markdown] lang="de"
#
# Fügen Sie  250g Butter und  1 Laib Brot zur Einkaufsliste
# `meine_einkaufsliste` hinzu.

# %%

# %% [markdown] lang="de"
# Drucken Sie die Einkaufsliste nochmal aus.

# %%

# %% [markdown] lang="de"
#
# Was passiert, wenn Sie `Butter` und `Brot` nochmals zur Einkaufsliste
# `meine_einkaufsliste` hinzufügen?

# %%

# %% [markdown] lang="de"
# *Diskussion:* Wie könnte das Verhalten der Klasse verbessert werden?
