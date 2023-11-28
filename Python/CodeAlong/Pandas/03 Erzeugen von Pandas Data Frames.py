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
#  <b>Erzeugen von Pandas Data Frames</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 03 Erzeugen von Pandas Data Frames.py -->
# <!-- python_courses/slides/module_610_pandas/topic_120_pandas_data_frames_1.py -->

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
import os
from pathlib import Path

import numpy as np
import pandas as pd

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
PANDAS_DIR_FROM_ENV = os.getenv("PANDAS_DIR_PATH")
if PANDAS_DIR_FROM_ENV:
    pandas_dir_path = Path(PANDAS_DIR_FROM_ENV)
else:
    pandas_dir_path = Path("data/pandas").absolute()
print(f"Pandas data: {pandas_dir_path}")

# %% tags=["keep"]
csv_file = pandas_dir_path / "example_data.csv"
excel_file1 = pandas_dir_path / "excel_data.xlsx"
excel_file2 = pandas_dir_path / "excel_other_sheet.xlsx"

# %%

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
# ## Erzeugen von Data Frames

# %% [markdown] lang="de"
# ### Aus einer Liste oder einem NumPy Array

# %% tags=["keep"]
df = pd.DataFrame([[1, 2], [3, 4], [5, 6], [7, 8]], columns=["A", "B"])


# %%

# %%

# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
def create_data_frame():
    rng = np.random.default_rng(42)
    array = rng.normal(size=(5, 4), loc=5.0, scale=2.0)
    index = ["A", "B", "C", "D", "E"]
    columns = ["w", "x", "y", "z"]
    return pd.DataFrame(array, index=index, columns=columns)


# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
df = create_data_frame()
df

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
# ### Aus einer CSV Datei

# %%

# %%

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### Aus einer Datenbank
#
# - Mit `pd.read_sql()` kann man eine SQL Abfrage ausführen und das Ergebnis in einen
#   Data Frame laden.
# - Mit `pd.read_sql_table()` kann man eine SQL Tabelle in einen Data Frame laden.
# - In der SQLite Datenbank `example_data.db` (im Verzeichnis `data/pandas`) ist eine
#   Tabelle `example_data` gespeichert.

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %%

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# - Pandas verwendet SQLAlchemy um auf die Datenbank zuzugreifen.
# - Wir können die Query auch mit SQLAlchemy erzeugen
# - Dabei können wir
#   - die Tabellendefinition aus der Datenbank auslesen
#   - die SQLAlchemy Expression Language verwenden

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %%

# %%

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# - Query mit SQLAlchemy Expression Language

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# - Einlesen mit `pd.read_sql()` und SQLAlchemy Expression Language

# %%

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# - Einlesen mit `pd.read_sql_table()`

# %%

# %%

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
# ### Aus einer Excel Datei

# %%

# %%

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %%

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# ### Andere Formate:
#
# - `pd.read_clipboard`
# - `pd.read_html`
# - `pd.read_json`
# - `pd.read_pickle`
# - `pd.read_sql` (verwendet SQLAlchemy um auf die Datenbank zuzugreifen)
# - ...

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Mini-Workshop: Erzeugen von Data Frames
#
# In der Datei `california-housing.csv` (im Verzeichnis `data/pandas`) ist eine Tabelle
# mit Immobilienpreisen in Kalifornien gespeichert. Laden Sie diese Tabelle in einen
# Pandas DataFrame.


# %%

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Die Excel-Datei `housing-data.xlsx` (im Verzeichnis `data/pandas`) enthält zwei
# Sheets: `Boston` und `California`. Laden Sie diese Tabellen in Pandas Data Frames.

# %%

# %%

# %%

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# In der Datei "weather.db" (im Verzeichnis `data/pandas`) ist eine SQLite Datenbank
# gespeichert. Die Tabelle `weather` enthält Wetterdaten für verschiedene Städte.
# Laden Sie diese Tabelle in einen Pandas Data Frame.
#
# *Hinweis:* Der Connection-String für eine SQLite Datenbank lautet
# `sqlite:///pfad/zur/datei.db`.

# %%

# %%
