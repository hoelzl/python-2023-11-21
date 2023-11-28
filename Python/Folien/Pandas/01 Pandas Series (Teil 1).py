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
import matplotlib.pyplot as plt

# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
import numpy as np
import pandas as pd

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
# ## Erzeugung
#
# ### Aus Listen

# %%
pd.Series(data=[10, 20, 30, 40])

# %%
pd.Series(["a", "b", "c"])

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
# ### Aus Range oder Iterable

# %%
pd.Series(data=range(1, 201, 2))

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
data = pd.Series(data=range(1, 201, 2))
data.head()

# %%
data.tail()

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
# ### Aus Listen mit Index

# %%
pd.Series(data=[1, 2, 3, 4], index=["w", "x", "y", "z"])

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
# ### Aus Dictionary

# %%
pd.Series(data={"Ice Cream": 2.49, "Cake": 4.99, "Fudge": 7.99})

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# ## Indizes
#
# Im Gegensatz zu Numpy-Arrays können Serien einen Index haben, der nicht
# aus ganzen Zahlen besteht.

# %% tags=["keep"]
food = pd.Series({"Ice Cream": 2.49, "Cake": 4.99, "Fudge": 7.99})

# %%
food

# %%
food.index

# %%
food.size

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Zugriff auf Werte
#
# - Mit der Indexing-Notation `[]` kann man den zu einem Index gehörenden Wert
#   abrufen.
# - Das ist ähnlich wie bei einem Dictionary.

# %%
food["Cake"]

# %%
food.loc["Cake"]

# %%
# Error!
# food["Pie"]

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# - Im Gegensatz zu Dictionaries kann man beim Indexing auch die Position eines
#   Elements angeben.
# - Das ist nicht empfehlenswert, da es verwirrend sein kann.
# - Man sieht es aber in älteren Code-Beispielen sehr häufig.
# - Neue Pandas-Versionen geben eine Warnung aus.

# %%
food[0]

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# - Besser ist es mit `.iloc` auf die Position zuzugreifen.
# - `.iloc` ist *keine Methode* sonder ein Attribut
# - Man verwendet die Indexing-Notation `[]` nach `.iloc`

# %%
food.iloc[0]

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# - Analog zu `.iloc` gibt es `.loc`, um mit dem Index auf den Wert zuzugreifen.
# - Bei Serien ist das nicht so wichtig, aber bei Data Frames kann das den Code
#   klarer machen

# %%
food.loc["Cake"]

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# - Warum ist die direkte Indexing-Notation `[]` schlechter als `.iloc` und `.loc`?

# %%
confusing = pd.Series(data=np.arange(-1, 5), index=np.arange(-3, 3))
confusing

# %%
confusing[0]

# %%
confusing.loc[0]

# %%
confusing.iloc[0]

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
food.sum()

# %%
food.mean()

# %%
food.argmin()

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Operationen
#
# - Viele Operationen, die auf Numpy Arrays funktionieren, funktionieren auch
#   auf Pandas Series.
# - Die Operationen werden elementweise ausgeführt.

# %%
food * 2

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
food > 6

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
purchases

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
purchases.sum()

# %% tags=["alt"]
purchases.mean()

# %% tags=["alt"]
purchases.max()

# %% tags=["alt"]
purchases.min()

# %% tags=["alt"]
purchases.argmax()

# %% tags=["alt"]
purchases.argmin()

# %%
purchases.index[purchases.argmax()]

# %% tags=["alt"]
purchases["Luke"]


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
discount(10.0)

# %%
discount

# %% tags=["keep"]
food

# %%
food.apply(discount)

# %%
food

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
anonymous_discount = lambda price: price * 0.9  # noqa

# %%
anonymous_discount(10.0)

# %%
food.apply(lambda price: price * 0.9)

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Namen von Serien

# %%
food.name

# %%
food.name = "Deserts"

# %%
food.name

# %%
food

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# ## Plotten von Serien

# %% tags=["keep"]
weather_data = [3.3, 4.4, 8.9, 13.9, 19.4, 21.7, 24.4, 23.3, 18.9, 13.3, 7.8, 3.9]

# %% tags=["keep"]
weather = pd.Series(data=weather_data, index=range(1, 13), name="Berlin High")

# %%
weather

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
weather.plot(kind="bar")
plt.show()

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Beispiel: Horizontales Balkendiagramm

# %%
weather.plot(kind="barh")
plt.show()

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Beispiel: Liniendiagramm

# %%
weather.plot(kind="line")
plt.show()

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Beispiel: Flächendiagramm

# %%
weather.plot(kind="area")
plt.show()

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Beispiel: Pie-Chart
#
# Pie-Charts sind nicht besonders nützlich, da die Werte nicht gut verglichen
# werden können. Für dieses Beispiel sind sie besonders schlecht.

# %%
weather.plot(kind="pie")
plt.show()

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
data.plot(kind="hist", bins=20)
plt.show()

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# - `plot` ist nicht nur eine Methode, sondern auch ein Namensraum, der
#   individuelle Funktionen für die verschiedenen Diagrammtypen enthält.
# - Wir können die Diagramme also auch in der folgenden Art erzeugen:

# %%
weather.plot.bar()
plt.show()

# %%
data.plot.hist(legend=False, bins=20)
plt.show()

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
purchases.mean()

# %%
purchases.median()

# %%
purchases.plot.hist(bins=100)
plt.show()
