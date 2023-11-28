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
np.NaN

# %%
np.nan + 1

# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
food1 = pd.Series({"Ice Cream": 2.99, "Cake": 5.99, "Fudge": 6.99})
food2 = pd.Series({"Cake": 4.99, "Ice Cream": 2.99, "Pie": 3.49, "Cheese": 4.99})

# %%
food_sum = food1 + food2
food_sum

# %%
food1

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# - Rechenoperationen sind auch mit Skalaren möglich
# - Die Operation wird dann auf alle Elemente der Series angewendet

# %%
food1 + 0.5

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### Konkatenieren von Serien
#
# - Wir können Serien mit `pd.concat` konkatenieren
# - Dabei können duplizierte Werte im Index entstehen
# - Auch hier werden die ursprünglichen Serien nicht verändert

# %%
pd.concat([food1, food2])

# %%
food1

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# - Bei der Selektion von Werten aus einer Serie mit duplizierten Index-Werten
#   wird eine Teilserie zurückgegeben
# - Das macht den Umgang mit Serien in Programmen schwieriger

# %% tags=["keep"]
all_food = pd.concat([food1, food2])

# %%
all_food

# %%
all_food["Cake"]

# %%
all_food["Pie"]

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# - Wir können eine Liste mit einem Element als Index verwenden, um immer eine Serie
#   zurückzubekommen

# %% tags=["alt"]
all_food[["Cake"]]

# %% tags=["alt"]
all_food[["Pie"]]

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# - Mit Listen-Indexing können wir auch mehrere Werte auswählen
# - Das Ergebnis ist wieder eine Serie

# %%
all_food[["Cake", "Pie"]]

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# ## Fehlende Werte
#
# - Viele Pandas Operationen ignorieren fehlende Werte
# - Das Attribut `hasnans` gibt an, ob eine Serie fehlende Werte enthält
# - Die Methoden `isna()`, `notna()` und `dropna()` erlauben den Umgang mit fehlenden
#   Werten

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
food = food1 + food2
food

# %%
food.hasnans

# %%
food.isna()

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Feststellen wie viele Werte `NaN`s sind:

# %%
food.isna().sum()

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Entfernen von `NaN`s:

# %%
food.dropna()

# %%
food

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
measurements.size

# %% tags=["alt"]
measurements.hasnans

# %% tags=["alt"]
measurements.isna().sum()

# %% tags=["alt"]
measurements.dropna()

# %% tags=["alt"]
measurements[[3, 7, 8]]

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### Slices und Fancy Indexing
#
# - Serien erlauben Slices und Fancy Indexing

# %%
all_food[0:2]

# %%
all_food.iloc[0:2]

# %%
all_food.iloc[[0, 2]]

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# - Zuweisungen mit Slices und Fancy Indexing verändern die ursprüngliche Serie

# %%
all_food.iloc[0:3] = 2.99

# %%
all_food

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
all_food.iloc[[0, 2]] = 3.99

# %%
all_food

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Man kann auch ein Series-Objekt mit Booleschen Werten zum Indexing
# verwenden. Dann wird eine Teilfolge der Series ausgewählt:

# %% tags=["keep"]
food1

# %% tags=["keep"]
food1[pd.Series({"Ice Cream": False, "Cake": True, "Fudge": True})]

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
all_food < 4

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
all_food[all_food < 4]

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# ### Mehrfach vorkommende Werte
#
# - Das Attribut `is_unique` gibt an, ob alle Werte in einer Serie eindeutig sind
# - Das bezieht sich auf die Werte, nicht auf die Indizes!

# %%
s1 = pd.Series([1, 2], index=["a", "b"])

# %%
s1.is_unique

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
s2 = pd.Series([1, 2], index=["a", "a"])

# %%
s2.is_unique

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
s3 = pd.Series([1, 1], index=["a", "b"])

# %%
s3.is_unique

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
s4 = pd.Series([1, 1], index=["a", "a"])

# %%
s4.is_unique

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# - Mit der Methode `unique()` können wir die eindeutigen Werte einer Serie
#   bestimmen
# - Mit der Methode `value_counts()` können wir feststellen, wie oft jeder Wert
#   vorkommt

# %%
all_food.unique()

# %%
all_food.value_counts()

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# ### Mehrfach vorkommende Index-Werte
#
# - Genauso kann man feststellen, ob die Index-Werte eindeutig sind

# %%
food1.index

# %%
food1.index.is_unique

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
all_food.index

# %%
all_food.index.is_unique

# %%
all_food.index.value_counts()

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
measurements.is_unique

# %% tags=["alt"]
measurements.value_counts()

# %% tags=["alt"]
measurements.dropna().is_unique

# %% tags=["alt"]
measurements.index.is_unique

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
all_food.groupby(level=0)

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
all_food.groupby(level=0).indices

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# - Mit der `aggregate()`-Methode können wir eine Funktion auf die Gruppen anwenden

# %%
all_food.groupby(level=0).aggregate(list)

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
all_food.groupby(level=0).aggregate(set)

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
all_food.groupby(level=0).aggregate(np.mean)

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# - `GroupBy`-Objekte haben viele weitere Methoden, die die Gruppen aggregieren:

# %%
all_food.groupby(level=0).min()

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
all_food.groupby(level=0).mean()

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# ### Sortierte und unsortierte Serien
#
# - Werte und Indizes können sortiert oder unsortiert sein
# - Das mann man mit `is_monotonic_increasing()` überprüfen
# - Mit der `sort_values()`-Methode werden Serien nach den Werten sortiert
# - Mit der `sort_index()`-Methode werden Serien nach den Indizes sortiert

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
all_food

# %%
all_food.is_monotonic_increasing

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
sorted_food = all_food.sort_values()
sorted_food

# %%
sorted_food.is_monotonic_increasing

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
all_food.index.is_monotonic_increasing

# %%
sorted_food = all_food.sort_index()

# %%
sorted_food

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
sorted_food.index.is_monotonic_increasing

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Slicing und sortierte Indizes
#
# - Slicing ist nur möglich, wenn die Indizes sortiert sind

# %%
all_food

# %%
all_food.iloc[1:3]

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
# all_food.loc["Cake":"Fudge"]

# %%
sorted_food = all_food.sort_index()

# %%
sorted_food.loc["Cake":"Fudge"]

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
measurements.index.is_monotonic_increasing

# %%
measurements.is_monotonic_increasing

# %%
measurements.is_monotonic_decreasing

# %%
measurements.index.is_unique

# %%
measurements.is_unique

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# - Was ist der Mittelwert, Median und Standardabweichung der Messwerte?

# %%
measurements.mean()

# %%
measurements.median()

# %%
measurements.std()

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Erzeugen Sie drei neue Serien, die folgende Messwerte enthalten:
# - Für Zeiten mit einem eindeutigen Messwert soll dieser Wert enthalten sein
# - Für Zeiten mit mehreren Messungen soll
#   - der größte Wert
#   - der kleinste Wert
#   - der Mittelwert der Messungen zu diesem Zeitpunkt

# %%
min_measurements = measurements.groupby(measurements.index).min()
min_measurements

# %%
max_measurements = measurements.groupby(measurements.index).max()
max_measurements

# %%
avg_measurements = measurements.groupby(measurements.index).mean()
avg_measurements

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# - Erzeugen Sie eine neue Serie, die alle Messungen enthält, die zwischen
#   3 und 7 Sekunden stattfanden (einschließlich der Grenzen).
# - Erzeugen Sie eine neue Serie, die alle Messungen zwischen der 2. und der 6. Messung
#   enthält (einschließlich der Grenzen).

# %%
measurements

# %%
measurements.loc[3:7]

# %% tags=["alt"]
# measurements[3:9]

# %%
measurements.iloc[1:6]

# %% [markdown] lang="de"
#
# - Erzeugen Sie eine Serie, die alle Messungen enthält, deren Wert größer als 10 ist.
# - Erzeugen Sie eine Serie, die alle Messungen enthält, deren Wert zwischen 8 und 11
#   ist.

# %%
measurements[measurements > 10]

# %%
measurements[(8 < measurements) & (measurements < 11)]
