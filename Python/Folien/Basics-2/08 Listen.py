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
#  <b>Listen</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 08 Listen.py -->
# <!-- python_courses/slides/module_150_collections/topic_110_b1_lists.py -->

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Listen
#
# - Wir können mittlerweile Programme schreiben, die viele Arten von
#   Berechnungen ausführen, aber wir haben noch keine Möglichkeit, mehrere
#   Objekte zusammenzufassen.
# - Wenn wir beispielsweise eine Einkaufsliste erstellen wollen, müssen wir
#   uns im Moment mit folgender Lösung behelfen:

# %% lang="de" tags=["keep"]
produkt_1 = "Haferflocken"
produkt_2 = "Kaffeebohnen"
produkt_3 = "Orangenmarmelade"

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Diese Vorgehensweise hat viele Probleme:
#
# - Wir müssen genau wissen, wie viele Produkte wir kaufen wollen
# - Es gibt keine Möglichkeit Operationen auf allen Produkten auszuführen,
#   z.B. alle Produkte auszudrucken
# - Python weiß nicht, dass die Produkte zusammengehören
# - ...

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Die Lösung: Listen

# %% lang="de"
einkaufsliste = ["Haferflocken", "Kaffeebohnen", "Orangenmarmelade"]

# %% [markdown] lang="de"
# Der Typ von Listen ist `list`.

# %% lang="de"
type(einkaufsliste)

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
# ## Erzeugen von Listen
#
# - Listen werden erzeugt, indem man ihre Elemente in eckige Klammern
#   einschließt.
# - Die Elemente einer Liste können beliebige Python-Werte sein.
# - Eine Liste kann Elemente mit verschiedenen Typen enthalten.

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
list_1 = [1, 2, 3, 4, 5]

# %%
list_1

# %%
list_2 = ["string1", "another string"]

# %%
list_2

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
list_3 = []

# %%
list_3

# %%
list_4 = [1, 0.4, "ein String", True, None]

# %%
list_4

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Die Elemente einer Liste müssen keine Literale sein, man kann auch Werte von
# Variablen in einer Liste speichern:

# %% lang="de" tags=["keep"]
produkt_1 = "Haferflocken"
produkt_2 = "Kaffeebohnen"
produkt_3 = "Orangenmarmelade"

# %% lang="de"
einkaufsliste = [produkt_1, produkt_2, produkt_3, "Erdbeermarmelade"]
einkaufsliste

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Nachdem eine Liste erzeugt ist hat sie keine Verbindung zu den Variablen, die
# in ihrer Konstruktion verwendet wurden:

# %% lang="de"
produkt_1 = "Dinkelflocken"
produkt_2 = "Teebeutel"
einkaufsliste

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
# ## Zugriff auf Listenelemente

# %% tags=["keep"]
numbers = [2, 4, 6, 8]

# %%
numbers[0]

# %%
numbers[3]

# %%
numbers[-1]

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Andere Möglichkeiten, Listen zu erzeugen
#
# Mit dem Additionsoperator `+` können Listen konkateniert werden:

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
[1, 2, 3] + [4, 5, 6]

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# Durch den Multiplikationsoperator `*` können die Elemente einer Liste
# wiederholt werden:

# %%
[1, 2] * 3

# %%
3 * ["a", "b"]

# %%
[0] * 10

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
# Mit der Funktion `list()` können manche andere Datentypen in Listen umgewandelt
# werden.
#
# Im Moment kennen wir nur Listen und Strings als mögliche Argumenttypen:

# %%
list("abc")

# %%
list([1, 2, 3])


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Mini-Workshop: Farben (Teil 1)
#
# - Definieren Sie eine Variable `grundfarben`, die eine Liste mit den Strings
#   `"Rot"`, `"Grün"` und `"Blau"` enthält.
# - Definieren Sie eine Variable `mischfarben`, die eine Liste mit den Strings
#   `"Cyan"`, `"Gelb"` und `"Magenta"` enthält.

# %% lang="de"
grundfarben = ["Rot", "Grün", "Blau"]

# %% lang="de"
mischfarben = ["Cyan", "Gelb", "Magenta"]


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Erzeugen Sie eine Liste `farben`, die die Elemente von `grundfarben` gefolgt von
# den Elementen von `mischfarben` enthält.

# %% lang="de"
farben = grundfarben + mischfarben
farben


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Erzeugen Sie eine Liste, die 15-mal die Zahl `1` enthält.

# %%
[1] * 15


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Erzeugen Sie die Liste `["r", "g", "b"]` aus dem String `"rgb"`.

# %%
list("rgb")
