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
#  <b>Pandas Data Frames Basics</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 04 Pandas Data Frames Basics.py -->
# <!-- python_courses/slides/module_610_pandas/topic_130_pandas_data_frames_2.py -->

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os


# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
def create_data_frame():
    rng = np.random.default_rng(42)
    array = rng.normal(size=(5, 4), loc=5.0, scale=2.0)
    index = ["A", "B", "C", "D", "E"]
    columns = ["w", "x", "y", "z"]
    return pd.DataFrame(array, index=index, columns=columns)


# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
PANDAS_DIR_FROM_ENV = os.getenv("PANDAS_DIR_PATH")
if PANDAS_DIR_FROM_ENV:
    pandas_dir_path = Path(PANDAS_DIR_FROM_ENV)
else:
    pandas_dir_path = Path("data/pandas").absolute()
print(f"Pandas data: {pandas_dir_path}")

# %% tags=["keep"]
df_csv = pd.read_csv(pandas_dir_path / "example_data.csv")

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# ## Extrahieren von Spalten

# %% tags=["keep"]
df = create_data_frame()
df

# %%
df["x"]

# %%
type(df["x"])

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
df[["x"]]

# %%
type(df[["x"]])

# %%
df[["x", "w", "x"]]

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
# # Plotten von Data Frames

# %%
df_csv["Col 0"].hist()
plt.show()

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
df_csv.hist()
plt.show()

# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
df_csv.hist(bins=20, figsize=(12, 8))
plt.show()

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
df_csv.plot.scatter(x="Col 1", y="Col 2")
plt.show()

# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
df_csv.plot(kind="scatter", x="Col 1", y="Col 2", c="Col 3", cmap="hot")
plt.show()

# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
df_csv.plot(
    kind="scatter",
    x="Col 1",
    y="Col 2",
    c=df_csv["Col 3"],
    s=df_csv["Col 4"].abs() * 6,
    alpha=0.4,
    cmap="hot",
)
plt.show()

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# ### Indizes und Operationen
#
# - Wir können uns Data Frames als mehrere Serien vorstellen, die alle den gleichen
#   Index haben.
# - Die Spalten werden ebenfalls durch einen Pandas-Index repräsentiert.

# %% tags=["keep"]
df = create_data_frame()
df["w"]

# %%
df.index

# %%
df.index.is_monotonic_increasing

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# - Die meisten von NumPy und Serien bekannten Operationen sind für Data Frames
#   definiert.

# %%
df.size

# %%
df.ndim

# %%
df.shape

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
# ### Erzeugen, Umbenennen und Löschen von Spalten

# %% tags=["keep"]
df = create_data_frame()

# %%
df["Sum"] = df["w"] + df["y"]

# %%
df

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
df.rename(columns={"Sum": "w + y"})

# %%
df

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
df.rename(columns={"Sum": "w + y"}, index={"E": "Z"}, inplace=True)

# %%
df

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
df.drop("A")

# %%
df

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
df.drop("B", inplace=True)

# %%
df

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
df.drop("z", axis=1)

# %%
df

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
df.drop("z", axis=1, inplace=True)

# %%
df

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
type(df["y"])

# %%
del df["y"]

# %%
df

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
# ## Auswahl

# %% tags=["keep"]
df = create_data_frame()
df

# %%
df["w"]

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
df[["x", "w"]]

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
# Error!
# df["A"]

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
df.loc["B"]

# %%
type(df.loc["B"])

# %%
df.loc["B", "z"]

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
df.loc[["B"]]

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
df.loc[["A", "C"]]

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
df.loc[["A", "C"], ["x", "y"]]

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
df.loc[:, ["x", "w"]]

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
df.iloc[0]

# %%
df.iloc[0, 0]

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
df.iloc[[0, 3]]

# %%
df.iloc[[1, 2], [0, 3]]

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
# ## Bedingte Auswahl

# %% tags=["keep"]
df = create_data_frame()
df

# %%
df > 5

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
df[df > 5]

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
df["w"] > 5

# %%
df[df["w"] > 5]

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
df[df["w"] > 5][["x", "y"]]

# %%
df[(df["w"] > 5) & (df["x"] < 5)]

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# # Information über Data Frames

# %% tags=["keep"]
df = create_data_frame()
df["txt"] = list("abcde")
df.iloc[1, [1, 2]] = np.nan
df

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
df.describe()

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
df.info()

# %%
df.dtypes

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
# ## Der Index eines Data Frames

# %% tags=["keep"]
df = create_data_frame()
df["txt"] = list("abcde")
df

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
df.reset_index()

# %%
df

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
df.reset_index(inplace=True)

# %%
df

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
df.rename(columns={"index": "old_index"}, inplace=True)

# %%
df

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
df.set_index("txt")

# %%
df

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
df.set_index("txt", inplace=True)
df

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
df.set_index("old_index", inplace=True)
df

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
df.info()

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# ## Mini-Workshop: Wine Data Frame
#
# In der Datei `pandas_dir_path / "wines.csv"` sind Daten über verschiedene Weinsorten
# gespeichert.
#
# - Laden Sie die Datei in einen Pandas Data Frame.
# - Wie viele Zeilen und Spalten hat der Data Frame?
# - Analysieren Sie, welche Spalten der Data Frame hat und welchen Typ sie haben.
# - Was sind Minima, Maxima, Mittelwert und Quantilen der numerischen Spalten?


# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
wine_df = pd.read_csv(pandas_dir_path / "wines.csv", index_col=0)
wine_df

# %%
wine_df.info()

# %%
wine_df.describe()

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# - Fügen Sie eine Spalte `normal_proline` ein, deren Werte die in den Bereich $[0, 1]$
#   skalierten Werte von `proline` sind.
# - Überprüfen Sie, dass die Werte der neuen Spalte im gewünschten Bereich sind.

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
proline = wine_df["proline"]
wine_df["normal_proline"] = (proline - proline.min()) / (proline.max() - proline.min())

# %%
wine_df

# %%
wine_df["normal_proline"].min(), wine_df["normal_proline"].max()

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# - Plotten Sie Histogramme der `alcohol` und `total_phenols` Spalten.
# - Plotten Sie einen Scatterplot der `total_phenols` gegen `nonflavanoid_phenols`
#   Werte.
# - Plotten Sie einen Scatterplot der `total_phenols` gegen `nonflavanoid_phenols`
#   Werte, bei dem Sie den Punkten eine unterschiedliche Farbe je nach Wert von
#   `target` zuordnen und die Marker mit der Größe des `proline`-Attributs / 75
#   darstellen.

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
wine_df.hist(column="alcohol", bins=15)
plt.show()

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
wine_df.hist(column="total_phenols", bins=15)
plt.show()

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
wine_df.plot(kind="scatter", x="total_phenols", y="nonflavanoid_phenols")
plt.show()

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
wine_df.plot(
    kind="scatter",
    x="total_phenols",
    y="nonflavanoid_phenols",
    s=wine_df["proline"] / 75,
    c="target",
    cmap="brg",
)
plt.show()
