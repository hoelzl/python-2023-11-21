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
#  <b>Pandas Series (Teil 2)</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 02 Pandas Series (Teil 2).py -->
# <!-- python_courses/slides/module_610_pandas/topic_112_pandas_series_2.py -->

# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
import numpy as np
import pandas as pd

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# ## Operationen auf mehreren Serien
#
# - Wir können Rechenoperationen auf Serien anwenden
# - Die Operationen werden elementweise ausgeführt
# - Die Indizes werden bei der Ausführung der Operationen berücksichtigt
# - Fehlende Werte werden mit `NaN` aufgefüllt

# %%

# %%

# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
food1 = pd.Series({"Ice Cream": 2.99, "Cake": 5.99, "Fudge": 6.99})
food2 = pd.Series({"Cake": 4.99, "Ice Cream": 2.99, "Pie": 3.49, "Cheese": 4.99})

# %%

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# - Rechenoperationen sind auch mit Skalaren möglich
# - Die Operation wird dann auf alle Elemente der Series angewendet

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### Konkatenieren von Serien
#
# - Wir können Serien mit `pd.concat` konkatenieren
# - Dabei können duplizierte Werte im Index entstehen
# - Auch hier werden die ursprünglichen Serien nicht verändert

# %%

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# - Bei der Selektion von Werten aus einer Serie mit duplizierten Index-Werten
#   wird eine Teilserie zurückgegeben
# - Das macht den Umgang mit Serien in Programmen schwieriger

# %% tags=["keep"]
all_food = pd.concat([food1, food2])

# %%

# %%

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# - Wir können eine Liste mit einem Element als Index verwenden, um immer eine Serie
#   zurückzubekommen

# %% tags=["start"]
all_food["Cake"]

# %% tags=["start"]
all_food["Pie"]

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# - Mit Listen-Indexing können wir auch mehrere Werte auswählen
# - Das Ergebnis ist wieder eine Serie

# %%

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# ## Fehlende Werte
#
# - Viele Pandas Operationen ignorieren fehlende Werte
# - Das Attribut `hasnans` gibt an, ob eine Serie fehlende Werte enthält
# - Die Methoden `isna()`, `notna()` und `dropna()` erlauben den Umgang mit fehlenden
#   Werten

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %%

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Feststellen wie viele Werte `NaN`s sind:

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Entfernen von `NaN`s:

# %%

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Workshop: Selektieren von Werten, Fehlende Werte
#
# Gegeben sei die folgende Serie `measurements` mit Messwerten:

# %% tags=["keep"]
measurements_1 = pd.Series(
    [13.78, 13.41, 13.21, 10.24, 9.84, 9.35, 6.23, 5.78, 5.26, 3.44],
    index=[1, 4, 5, 6, 6, 7, 8, 8, 9, 11],
)

# %% tags=["keep"]
measurements_2 = pd.Series(
    [8.2, 8.1, 7.9, 7.8, 7.1, 8.6, 9.5, 7.4, 5.3, 7.2, 5.2],
    index=[1, 3, 4, 5, 6, 7, 7, 8, 8, 9, 10],
)

# %% tags=["keep"]
measurements = measurements_1 + measurements_2

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# - Wie viele Messwerte sind in der Serie enthalten?
# - Enthält die Serie fehlende Werte? Wenn ja, wie viele?
# - Entfernen Sie alle fehlenden Werte aus der Serie
# - Geben Sie die zu den Zeiten 3, 7 und 8 gemessenen Werte aus

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### Slices und Fancy Indexing
#
# - Serien erlauben Slices und Fancy Indexing

# %%

# %%

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# - Zuweisungen mit Slices und Fancy Indexing verändern die ursprüngliche Serie

# %%

# %%

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Man kann auch ein Series-Objekt mit Booleschen Werten zum Indexing
# verwenden. Dann wird eine Teilfolge der Series ausgewählt:

# %% tags=["keep"]
food1

# %% tags=["keep"]
food1[pd.Series({"Ice Cream": False, "Cake": True, "Fudge": True})]

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# ### Mehrfach vorkommende Werte
#
# - Das Attribut `is_unique` gibt an, ob alle Werte in einer Serie eindeutig sind
# - Das bezieht sich auf die Werte, nicht auf die Indizes!

# %%

# %%

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %%

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %%

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# - Mit der Methode `unique()` können wir die eindeutigen Werte einer Serie
#   bestimmen
# - Mit der Methode `value_counts()` können wir feststellen, wie oft jeder Wert
#   vorkommt

# %%

# %%

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# ### Mehrfach vorkommende Index-Werte
#
# - Genauso kann man feststellen, ob die Index-Werte eindeutig sind

# %%

# %%

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %%

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Workshop: Eindeutige Werte
#
# Wir haben im vorhergehenden Workshop die Serie `measurements` erzeugt.
#
# - Sind die Werte in der Serie eindeutig?
# - Wie oft kommt jeder Wert vor?
# - Ist das das Ergebnis, das Sie erwartet haben?
# - Mit welcher Operation können Sie eine Serie mit eindeutigen Werten erzeugen?
# - Sind die Indizes in der Serie eindeutig?

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# ## Gruppieren
#
# - Mit der `groupby()`-Methode können wir eine Serie nach Index-Werten grpupieren
# - Das Ergebnis ist ein `GroupBy`-Objekt
# - Das `GroupBy`-Objekt enthält die Indizes der Gruppen als Keys

# %% tags=["keep"]
all_food

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# - Mit der `aggregate()`-Methode können wir eine Funktion auf die Gruppen anwenden

# %%

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# - `GroupBy`-Objekte haben viele weitere Methoden, die die Gruppen aggregieren:

# %%

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# ### Sortierte und unsortierte Serien
#
# - Werte und Indizes können sortiert oder unsortiert sein
# - Das mann man mit `is_monotonic_increasing()` überprüfen
# - Mit der `sort_values()`-Methode werden Serien nach den Werten sortiert
# - Mit der `sort_index()`-Methode werden Serien nach den Indizes sortiert

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %%

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %%

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %%

# %%

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Slicing und sortierte Indizes
#
# - Slicing ist nur möglich, wenn die Indizes sortiert sind

# %%

# %%

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
# all_food.loc["Cake":"Fudge"]

# %%

# %%

# %% [markdown] lang="de"
#
# **Wichtig:** Der obere Wert der Slice, `"Fudge"` ist im Resultat enthalten!

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Mini-Workshop: Einfache Zeitreihenanalyse
#
# Wir haben folgende Zeitreihe mit Messwerten.
# - Der Index-Wert gibt die Zeit in Sekunden an, zu der die Messung stattfand


# %% tags=["keep"]
measurements = pd.Series(
    [13.78, 13.41, 13.21, 10.24, 9.84, 9.35, 6.23, 5.78, 5.26, 3.44],
    index=[1, 4, 5, 6, 6, 7, 8, 8, 9, 11],
    name="Measurements",
)

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# - Sind die Zeiten der Messungen aufsteigend geordnet?
# - Sind die Messwerte aufsteigend oder absteigend geordnet?
# - Sind die Zeiten der Messungen eindeutig?
# - Sind die Werte der Messungen eindeutig?

# %%

# %%

# %%

# %%

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# - Was ist der Mittelwert, Median und Standardabweichung der Messwerte?

# %%

# %%

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Erzeugen Sie drei neue Serien, die folgende Messwerte enthalten:
# - Für Zeiten mit einem eindeutigen Messwert soll dieser Wert enthalten sein
# - Für Zeiten mit mehreren Messungen soll
#   - der größte Wert
#   - der kleinste Wert
#   - der Mittelwert der Messungen zu diesem Zeitpunkt

# %%

# %%

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# - Erzeugen Sie eine neue Serie, die alle Messungen enthält, die zwischen
#   3 und 7 Sekunden stattfanden (einschließlich der Grenzen).
# - Erzeugen Sie eine neue Serie, die alle Messungen zwischen der 2. und der 6. Messung
#   enthält (einschließlich der Grenzen).

# %%

# %%

# %%

# %% [markdown] lang="de"
#
# - Erzeugen Sie eine Serie, die alle Messungen enthält, deren Wert größer als 10 ist.
# - Erzeugen Sie eine Serie, die alle Messungen enthält, deren Wert zwischen 8 und 11
#   ist.

# %%

# %%
