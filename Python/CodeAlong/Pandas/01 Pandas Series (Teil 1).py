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
#  <b>Pandas Series (Teil 1)</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 01 Pandas Series (Teil 1).py -->
# <!-- python_courses/slides/module_610_pandas/topic_110_pandas_series_1.py -->

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# # Pandas Typ `Series`
#
# Eine Pandas `Series` Instanz stellt eine Folge von Werten dar, ähnlich wie
# eine Python-Liste. Die Elemente einer Serie können über ihren numerischen
# Index abgerufen werden, aber zusätzlich kann eine Serie einen semantisch
# sinnvollen Index haben (z. B. für Zeitreihen).
#
# Intern wird eine Pandas-Serie durch ein Numpy-Array unterstützt, daher sind
# die meisten der Numpy-Operationen auch auf Serien anwendbar sind.
#
# Darüber hinaus ist es einfach (und billig), Serien nach Numpy zu konvertieren.

# %%

# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
import numpy as np
import pandas as pd

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
# ## Erzeugung
#
# ### Aus Listen

# %%

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
# ### Aus Range oder Iterable

# %%

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
# ### Aus Listen mit Index

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
# ### Aus Dictionary

# %%

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# ## Indizes
#
# Im Gegensatz zu Numpy-Arrays können Serien einen Index haben, der nicht
# aus ganzen Zahlen besteht.

# %% tags=["keep"]
food = pd.Series({"Ice Cream": 2.49, "Cake": 4.99, "Fudge": 7.99})

# %%

# %%

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Zugriff auf Werte
#
# - Mit der Indexing-Notation `[]` kann man den zu einem Index gehörenden Wert
#   abrufen.
# - Das ist ähnlich wie bei einem Dictionary.

# %%

# %%

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# - Im Gegensatz zu Dictionaries kann man beim Indexing auch die Position eines
#   Elements angeben.
# - Das ist nicht empfehlenswert, da es verwirrend sein kann.
# - Man sieht es aber in älteren Code-Beispielen sehr häufig.
# - Neue Pandas-Versionen geben eine Warnung aus.

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# - Besser ist es mit `.iloc` auf die Position zuzugreifen.
# - `.iloc` ist *keine Methode* sonder ein Attribut
# - Man verwendet die Indexing-Notation `[]` nach `.iloc`

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# - Analog zu `.iloc` gibt es `.loc`, um mit dem Index auf den Wert zuzugreifen.
# - Bei Serien ist das nicht so wichtig, aber bei Data Frames kann das den Code
#   klarer machen

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# - Warum ist die direkte Indexing-Notation `[]` schlechter als `.iloc` und `.loc`?

# %%

# %%

# %%

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# - Ähnlich wie NumPy Arrays unterstützen Pandas Series auch Slices und Fancy
#   Indexing.
# - Dazu kommen wir später.

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Methoden
#
# - Series haben eine Vielzahl von Methoden:

# %%

# %%

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Operationen
#
# - Viele Operationen, die auf Numpy Arrays funktionieren, funktionieren auch
#   auf Pandas Series.
# - Die Operationen werden elementweise ausgeführt.

# %%

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Workshop: Einkäufe
#
# Die folgende Pandas Series enthält die Beträge, die Kunden eines Online-Shops
# für ihre Einkäufe bezahlt haben:

# %% tags=["keep"]
purchases = pd.Series(
    data=[10.99, 21.99, 4.99, 14.99, 2.99, 24.99, 12.99, 8.99, 1.99, 19.99],
    index=[
        "Joe",
        "Steve",
        "Linda",
        "Luke",
        "Ben",
        "Jack",
        "Wes",
        "Lisa",
        "Steph",
        "Craig",
    ],
    name="Purchases",
)


# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# - Wie viel haben die Kunden insgesamt bezahlt?
# - Was war der durchschnittliche Betrag?
# - Was waren der höchste und der niedrigste Betrag?
# - Wie viel hat der Kunde "Luke" bezahlt?
# - An welchen Positionen wurden die höchsten und niedrigsten Beträge bezahlt?
# - Welcher Kunde hat diesen Betrag bezahlt?
#   - *Hinweise:*
#     - `purchases.index` gibt den Index der Serie zurück
#     - Indizes erlauben Indexing mit `[]`

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# (Ende des Workshops.)

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# - Neben den Methoden, die fixe Funktionen berechnen, gibt es auch solche, die
#   es uns erlauben, die Werte der Serie zu transformieren.
# - Diese Methoden geben typischerweise eine neue Serie zurück.

# %% tags=["keep"]
def discount(price):
    return price * 0.9


# %%

# %%

# %% tags=["keep"]
food

# %%

# %%

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %%

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Namen von Serien

# %%

# %%

# %%

# %%

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# ## Plotten von Serien

# %% tags=["keep"]
weather_data = [3.3, 4.4, 8.9, 13.9, 19.4, 21.7, 24.4, 23.3, 18.9, 13.3, 7.8, 3.9]

# %% tags=["keep"]
weather = pd.Series(data=weather_data, index=range(1, 13), name="Berlin High")

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# - Pandas Series haben eine `plot`-Methode, die ein Diagramm der Werte erzeugt.
# - Die `plot`-Methode verwendet Matplotlib, um das Diagramm zu erzeugen.
# - Sie gibt ein Matplotlib `Axes`-Objekt zurück.
# - Die `plot`-Methode hat viele Parameter, um das Aussehen des Diagramms zu
#   steuern.
# - Mit `kind` kann die Art des Diagramms ausgewählt werden.

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Beispiel: Balkendiagramm

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Beispiel: Horizontales Balkendiagramm

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Beispiel: Liniendiagramm

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Beispiel: Flächendiagramm

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Beispiel: Pie-Chart
#
# Pie-Charts sind nicht besonders nützlich, da die Werte nicht gut verglichen
# werden können. Für dieses Beispiel sind sie besonders schlecht.

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Beispiel: Histogramm
#
# - Wir haben zu wenige Werte, um ein sinnvolles Histogramm zu erzeugen.
# - Daher erzeugen wir eine Serie mit zufälligen Werten.

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
import random

# %% tags=["keep"]
data = pd.Series(data=[random.gauss(0.0, 10.0) for _ in range(5_000)])

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# - `plot` ist nicht nur eine Methode, sondern auch ein Namensraum, der
#   individuelle Funktionen für die verschiedenen Diagrammtypen enthält.
# - Wir können die Diagramme also auch in der folgenden Art erzeugen:

# %%

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Workshop: Plotten von Einkäufen
#
# Unser Online-Shop hat mittlerweile mehr Kunden gewonnen. Die folgende Pandas-Series
# enthält die Beträge, die Kunden des Online-Shops für ihre Einkäufe bezahlt haben:

# %% tags=["keep"]
purchases = pd.Series(
    data=np.abs(
        np.random.exponential(scale=100.0, size=10_000)
        + np.random.normal(loc=25.0, scale=25.0, size=10_000)
    ),
    name="Purchases",
)

# %% [markdown] lang="de"
#
# - Berechnen Sie den Durchschnittlichen Betrag eines Einkaufs.
# - Erzeugen Sie ein Histogramm der Beträge.

# %%

# %%

# %%
