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
#  <b>Datenbanken: DB-API 2.0</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 01 Datenbanken DB-API 20.py -->
# <!-- python_courses/slides/module_310_working_with_data/topic_310_db_api.py -->

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# # Datenbanken: DB-API 2.0
#
# - Python hat ein standardisiertes API für SQL-Datenbanken
# - Die Spezifikation ist in [PEP-249](https://peps.python.org/pep-0249/)
# - Wir verwenden beispielhaft das `sqlite3` Modul
#   - Dieses Modul ist in der Standard-Installation von Python enthalten
#   - Es bietet einen Modus, in dem die Datenbank nur im Arbeitsspeicher gehalten wird
#   - Andere SQL-Datenbanken funktionieren ähnlich, haben aber gewisse Variationen


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Grundlegende Konzepte
#
# - Datenbanken werden über eine *Verbindung* *("Connection")* angesprochen
# - Zum Ausführen von Anweisungen (und Zugriff auf die Ergebnisse) benötigen
#   wir einen *Cursor*
# - Weitere Klassen, wie `Row` oder `Blob` dienen zum Umgang mit Ergebnissen.

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Erzeugen einer Verbindung
#
# - Eine `Connection`-Instanz wird mit `sqlite3.connect()` erzeugt
# - Argumente zu `connect()` beschreiben die Konfiguration der Datenbank
# - Mit `":memory:"` wird eine In-Memory-Datenbank erzeugt
# - Connections verwalten Transaktionen, falls die Datenbank das unterstützt:
#   - `connection.commit()` existiert immer, macht möglicherweise nichts
#   - `connection.rollback()` existiert nur, falls die DB Transaktionen unterstützt

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Wir erstellen eine temporäre Datei für eine sqlite3-Datenbank, damit die Daten
# erhalten bleiben, wenn wir eine Verbindung trennen und wiederherstellen.
#
# Wenn dies Probleme verursacht, können Sie entweder
#
# - den Pfad, unter dem die Datenbank gespeichert werden soll in der Variable
#   `DB` speichern oder
# - die Variable `DB` auf den speziellen Namen `:memory:` setzen, um eine
#   In-Memory-Datenbank zu erstellen. In diesem Fall sollten Sie die Befehle
#   nicht ausführen, die die die Datenbankverbindung trennen und wieder
#   herstellen.

# %% tags=["keep"]
import tempfile

# %% tags=["keep"]
DB_DIR = globals().get("DB_DIR") or tempfile.TemporaryDirectory()
DB = DB_DIR.name + "/sqlite-test.db"
# DB = ":memory:"
# DB = "/tmp/sqlite3-test.db"
print(f"Database path: {DB}")

# %% tags=["keep"]
import sqlite3

# %%

# %%

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Erzeugen eines Cursors
#
# - Die meisten Operationen im DB-API werden nicht auf der Connection ausgeführt,
#   sondern auf einem Cursor:
# - Commit und Rollback erfolgen direkt auf der Connection

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Ausführen von SQL-Anweisungen
#
# - `cursor.execute()` führt eine (parametrisierte) SQL-Anweisung aus
#   - Je nach Wert von `connection.isolation_level` wird eine Transaktion eröffnet
#   - Parameter werden korrekt "maskiert" um SQL-Injektionen zu vermeiden
#   - [`sqlite3.paramstyle`](https://peps.python.org/pep-0249/#paramstyle)
#     bestimmt, wie Parameter im Query-String gekennzeichnet werden
# - `cursor.executemany()`
#   - Wie `.execute()` aber mit einem Iterator von Parametern
# - `cursor.executescript()` führt mehrere SQL-Anweisungen aus
#   - Transaktionen müssen manuell verwaltet werden

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Bevorzuge `executemany()` mit Argumentensubstitution statt manuell erstellten
# SQL-Abfragen . Der folgende Code ist anfällig für einen SQL-Injection-Angriff:


# %%


# %%

# %%

# %%

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Schließen von Verbindungen
#
# Wenn eine Verbindung nicht mehr benötigt wird, kann sie mit `close()` geschlossen
# werden:

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Zugriff auf Ergebnisse
#
# - `cursor.fetchall()` für alle Ergebnisse
# - `cursor.fetchone()` für einzelne Ergebnisse
# - `cursor.fetchmany()` für eine bestimmte Anzahl an Ergebnissen
# - Iteration über einen Ergebnis-Cursor

# %% tags=["keep"]
con = sqlite3.connect(DB)

# %% tags=["keep"]
cur = con.cursor()

# %% tags=["keep"]
cur.execute("SELECT * FROM students ORDER BY id")

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Ein Cursor kan nur einmal verwendet werden, um Ergebnisse zu bekommen:

# %%

# %% tags=["keep"]
cur = cur.execute("SELECT * FROM students ORDER BY id")

# %%

# %%

# %%

# %%

# %%

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### Shortcut-Methoden
#
# - Um das explizite Erzeugen von Cursor-Instanzen zu umgehen, kann man
#   die Shortcut-Methoden auf dem Connection-Objekt verwenden:

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Mehrere Verbindungen
#
# - Mehrere Verbindungen zur gleichen Datenbank sind möglich
# - Mehrere Cursors zur gleichen Verbindung sind möglich
#   - Aber: In beiden Fällen führen mehrere gleichzeitig aktive
#     Transaktionen zu Timeouts
# - Cursors zur gleichen Verbindung sind nicht isoliert
# - Wie isoliert Threads voneinander sind, wird durch
#   [`connection.threadsafety`](https://peps.python.org/pep-0249/#threadsafety)
#   beschrieben.

# %% tags=["keep"]
con.close()

# %% tags=["keep"]
con = sqlite3.connect(DB)

# %% tags=["keep"]
cur = con.cursor()

# %% tags=["keep"]
con2 = sqlite3.connect(DB)

# %% tags=["keep"]
cur.execute("INSERT INTO students VALUES(2, 'Deborah Winter')")

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %% tags=["keep"]
con = sqlite3.connect(DB)

# %%

# %%

# %%

# %%

# %%

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Zugriff auf Metadaten
#
# - Erfolgt typischerweise mit DB-spezifischen Tabellen:

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# ## Mini-Workshop: Mitarbeiter-Datenbank
#
# Sie wollen Daten für die Mitarbeiter einer Firma in einer SQLite Datenbank
# speichern. Jeder Mitarbeiter wird dabei durch folgende Daten beschrieben:
#
# - Personalnummer
# - Name
# - Abteilungs-Nummer
# - Wochenarbeitszeit in Stunden
#
# Jede Abteilung wird repräsentiert durch folgende Daten:
#
# - Abteilungs-Nummer
# - Name der Abteilung
#
# Schreiben Sie folgende Funktionen:
#
# - `create_employee_db(...)`, die die Tabellen erzeugt
# - `create_department(...)`, die eine neue Abteilung in die Datenbank einfügt.
# - `create_employee(...)`, die einen neuen Mitarbeiter in die Datenbank einfügt.
# - `create_employee(...)`, die mehrere neue Mitarbeiter in die Datenbank einfügt.
# - `get_employee_data(db, id)`, die die Daten für den Mitarbeiter mit
#    Personalnummer `id` zurückgibt. (Falls Sie SQL Joins kennen, können Sie statt
#    der Abteilungs-Nummer den Namen der Abteilung zurückgeben.)
# - `find_part_time_employees(...)`, die die Personalnummern alle Mitarbeiter
#    zurückgibt, die weniger als 30 Stunden pro Woche arbeiten.
# - `print_employees_in_department(con: sqlite3.Connection, name: str)`,
#    die die Daten aller Mitarbeiter in
#    der Abteilung mit Namen `name` ausdruckt. (Falls sie SQL-Joins nicht kennen,
#    können Sie auch die Abteilungs-Nummer an die Funktion übergeben.)

# %% tags=["keep"]
import sqlite3

# %% tags=["keep"]
con = sqlite3.connect(":memory:")

# %%

# %% tags=["keep"]
create_employee_db(con)

# %%

# %% tags=["keep"]
create_department(con, 1, "Marketing")
create_department(con, 2, "R&D")
create_department(con, 3, "Accounting")

# %% tags=["keep"]
assert con.execute("SELECT * FROM departments ORDER BY id").fetchall() == [
    (1, "Marketing"),
    (2, "R&D"),
    (3, "Accounting"),
]

# %%

# %% tags=["keep"]
create_employee(con, 1, "Geraldine E. Stegner", 1, 40)

# %% tags=["keep"]
assert con.execute("SELECT * FROM employees").fetchall() == [
    (1, "Geraldine E. Stegner", 1, 40)
]

# %%

# %%

# %% tags=["keep"]
EMPLOYEES = [
    (2, "Tammy T. Selby", 2, 42),
    (3, "Pam Adams", 3, 24),
    (4, "Bobby A. Skaggs", 1, 38),
    (5, "Sandra A. Finley", 2, 26),
]

# %% tags=["keep"]
create_employees(con, EMPLOYEES)

# %%

# %%

# %% tags=["keep"]
assert get_employee_data(con, 1) == (1, "Geraldine E. Stegner", "Marketing", 40)

# %% tags=["keep"]
assert get_employee_data(con, 10) is None

# %%

# %% tags=["keep"]
assert get_part_time_employees(con) == [3, 5]

# %%

# %%

# %% [markdown] lang="de"
#
# Ausgabe:
# ```
# Geraldine E. Stegner: id = 1, dep = Marketing, hours = 40
# Bobby A. Skaggs: id = 4, dep = Marketing, hours = 38
# ```
