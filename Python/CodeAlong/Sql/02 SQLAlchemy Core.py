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
#  <b>SQLAlchemy Core</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 02 SQLAlchemy Core.py -->
# <!-- python_courses/slides/module_310_working_with_data/topic_320_sqlalchemy_core.py -->

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# - DB-API 2.0:
#   - Unterstützt viele Datenbanken
#   - Programmierer schreibt SQL-Anweisungen textuell
#   - Sichere Übergabe von Parametern
#   - ...
# - Aber:
#   - Relativ niedriger Abstraktionsgrad
#   - Unterschiede zwischen Datenbanken (z.B.
#     [`sqlite3.paramstyle`](https://peps.python.org/pep-0249/#paramstyle))
#   - ...


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## SQLAlchemy
#
# - Umfassende Sammlung von Tools zum Arbeiten mit Datenbanken:
#   - Abstraktion von der konkreten (SQL-)Datenbank
#   - Connection Pooling
#   - SQL Expression Language
#   - SQL Schema
#   - Objekt-Relationales Mapping (ORM)

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# <img src="img/sqla_arch_small.png"
#      style="display:block;margin:auto;width:60%"/>


# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# <img src="img/sqlalchemy-types.svg"
#      style="display:block;margin:auto;width:60%"/>

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Die Engine
#
# - Typischerweise ein globales Objekt
# - Verwaltet die Verbindungen zur Datenbank
# - Unterhält einen Connection-Pool

# %%

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# - `sqlite`: Wir verwenden eine SQLite Datenbank...
# - `pysqlite`: ... mit dem `pysqlite` (= `sqlite3`) DB-API
# - `:memory:` ... und einer In-Memory Datenbank
# - `echo`: SQL-Anweisungen werden geloggt
#
# Die Engine kommuniziert erst bei Bedarf mit der Datenbank.

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## `Connection` und `Result`
#
# - Die `Connection`-Klasse repräsentiert eine Verbindung zu einer
#   Datenbank
# - Mit `connection.execute()` werden SQL-Anweisungen ausgeführt
# - Das Ergebnis einer Datenbank-Interaktion ist vom Type `Result` (oder einem
#   Subtyp)
# - Wir verwenden für die ersten Beispiele `text()` zum Schreiben von
#   SQL-Anweisungen
# - Normalerweise ist besser, statt dessen die SQLAlchemy Expression-Language
#   zu verwenden

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Transaktionen
#
# In SQLAlchemy gibt es zwei Arten Transaktionen zu managen:
#
# - Mit `engine.connect()`, `conn.execute()` und `engine.commit()` (commit as you go)
# - Mit `engine.begin()` und `conn.execute()` (begin once)

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %%

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %%

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Parameter
#
# - Parameter werden mit einer "benannten" Syntax übergeben `:x` statt `?`:
# - Die Argumente werden als Dictionary oder Sequenz von Dictionaries übergeben
# - Es gibt keinen Unterschied zwischen `.execute()` und `.executemany()`:

# %% tags=["subslide", "start"] slideshow={"slide_type": "subslide"}
with engine.connect() as conn:
    conn.execute(text("INSERT INTO students VALUES(1, 'Jack')"))
    conn.commit()
    conn.execute(text("INSERT INTO students VALUES(2, 'Jane')"))
    conn.commit()

# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
STUDENTS = [
    {"id": 1, "name": "Jack Bradley"},  # https://xkcd.com/327/
    {"id": 2, "name": "Robert'); DROP TABLE students; --"},
    {"id": 845, "name": "Samantha Jones"},
    {"id": 210, "name": "Jill McGee"},
    {"id": 62, "name": "Doug Caisson"},
]

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# *Hinweis:* Die Daten für SQLAlchemy müssen als Dictionaries oder Liste von
# Dictionaries übergeben werden. Falls Sie als andere Datenstruktur vorliegen,
# müssen Sie diese entsprechend umwandeln.

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
STUDENTS_TUPLES = [
    (1, "Jack Bradley"),
    (2, "Robert'); DROP TABLE students; --"),
    (845, "Samantha Jones"),
    (210, "Jill McGee"),
    (62, "Doug Caisson"),
]

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
STUDENTS_DICTS = []
for id_, name in STUDENTS_TUPLES:
    STUDENTS_DICTS.append({"id": id_, "name": name})

# %%

# %% tags=["subslide', "keep"]

# %%


# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %% tags=["subslide", "start]

# %% tags=["subslide", "start]

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# ## Mini-Workshop: Sportergebnisse
#
# Verwenden Sie SQLAlchemy für die folgenden Aufgaben:
#
# - Erzeugen Sie eine Tabelle für Sportergebnisse mit den folgenden Spalten:
#   - `event_id`
#   - `sport`
#   - `event_date`
#   - `winner`

# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
from sqlalchemy import create_engine, text

# %%

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Fügen Sie die folgenden Einträge in die Tabelle ein:

# %% tags=["keep"]
DATA = [
    (2, "soccer", "2022-08-07", "Mean Dwarves"),
    (4, "basketball", "2022-08-09", "Swift Waves"),
    (5, "soccer", "2022-10-11", "Lightning Legends"),
    (8, "soccer", "2022-08-12", "Fantastic Infernos"),
    (11, "basketball", "2022-09-12", "Loco Vikings"),
    (13, "basketball", "2022-09-04", "Storm Bears"),
    (24, "soccer", "2022-09-06", "Strange Brewers"),
    (3, "soccer", "2022-09-16", "Odd Gophers"),
    (6, "basketball", "2022-09-24", "Epic Clouds"),
    (35, "soccer", "2022-10-21", "Psychodelic Peacocks"),
    (18, "basketball", "2022-10-30", "Neon Braves"),
    (7, "soccer", "2022-10-25", "Silent Droids"),
]

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# *Hinweis:* Sie müssen dazu das Datenformat anpassen. SQLAlchemy erwartet die Daten
# als Liste von Dictionaries:
#
# ```python
# [
#     {
#         "event_id": 2,
#         "sport": "soccer",
#         "event_date": "2022-08-07",
#         "winner": "Mean Dwarves"
#     },
#     ...
# ]
# ```

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Überprüfen Sie, dass die Werte in die Datenbank eingefügt wurden.

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Erzeugen Sie eine Liste mit den Namen aller Basketball-Teams, die einen Wettbewerb
# gewonnen haben

# %%

# %%
