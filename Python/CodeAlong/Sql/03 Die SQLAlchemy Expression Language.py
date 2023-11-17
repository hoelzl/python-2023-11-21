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
#  <b>Die SQLAlchemy Expression Language</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 03 Die SQLAlchemy Expression Language.py -->
# <!-- python_courses/slides/module_310_working_with_data/topic_330_sqlalchemy_expressions.py -->

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# # Die SQLAlchemy Expression Language
#
# - Beschreibung der Datenbank durch Python Objekte (Metadata)
# - Kompositionale Syntax für SQL Anweisungen

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Metadata
#
# - `MetaData`: "Dictionary" für Tabellen
# - `Table`: Eine Tabelle in einer Datenbank
# - `Column`: Eine Spalte in einer Tabelle

# %%

# %%

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Wir wollen im Folgenden Tabellen für ein Hotel-Reservierungssystem
# mit der SQLAlchemy Expression Language anlegen.

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

# %%

# %%

# %%

# %%

# %%

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# ## Mini-Workshop: Autovermietung (Teil 1)
#
# Eine Autovermietung verwendet mehrere Tabellen in ihrem Verwaltungssystem:
#
# - `vehicles` mit Spalten `id` (Integer, Primärschlüssel), `license_plate` (String) und
#   `price_class` (Integer)
# - `customers` mit Spalten `id` (Integer, Primärschlüssel), `name` (String)
#    und `credit_card_number` (String)
# - `rental_agreements` mit Spalten `customer_id`, `vehicle_id`,
#   `start_date`, `end_date`
#
# Implementieren Sie dieses Datenmodell in SQLAlchemy und erzeugen Sie die Tabellen.

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %%

# %%

# %%

# %%

# %%

# %%

# %% [markdown] lang="de"
#
# Ende des Workshops

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### Datenbank-Query mit String

# %%

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### Erzeugen einer Tabelle durch Reflection
#
# SQLAlchemy kann ein `Table`-Objekt aus einer existierenden
# Datenbank-Tabelle erzeugen:

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### Datenbank-Query mit SQLAlchemy Expression Language

# %%

# %%

# %%

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Insert Anweisungen

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

# %% tags=["keep"]
GUESTS = [
    {"name": "Theo Brown", "email": "theo.brown@fastmail.org"},
    {"name": "Alayna Rogers", "email": "arogers@gmail.com"},
    {"name": "June Abbott", "email": "june.abbott@yahoo.com"},
    {"name": "Langosh Kaleigh", "email": "langosh.kaleigh@kiehn.org"},
    {"name": "Andre Reyes", "email": "a.reyes@runolfsdottir.info"},
    {"name": "Xander Richardson", "email": "xander@krajcik.net"},
    {"name": "Jayla Ruiz", "email": "jayla@ruiz.net"},
]

# %%

# %%

# %%

# %%

# %% tags=["keep"]
RESERVATIONS = [
    {
        "guest_id": 2,
        "check_in_date": d("2023-03-02"),
        "check_out_date": d("2023-03-02"),
        "room_number": 123,
    },
    {
        "guest_id": 3,
        "check_in_date": d("2023-03-04"),
        "check_out_date": d("2023-03-07"),
        "room_number": 254,
    },
    {
        "guest_id": 2,
        "check_in_date": d("2023-03-06"),
        "check_out_date": d("2023-03-12"),
        "room_number": 135,
    },
    {
        "guest_id": 4,
        "check_in_date": d("2023-04-12"),
        "check_out_date": d("2023-04-22"),
        "room_number": 312,
    },
    {
        "guest_id": 3,
        "check_in_date": d("2023-04-17"),
        "check_out_date": d("2023-04-23"),
        "room_number": 218,
    },
    {
        "guest_id": 5,
        "check_in_date": d("2023-05-02"),
        "check_out_date": d("2023-05-08"),
        "room_number": 142,
    },
]

# %%

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Mit der `distinct()`-Methode können mehrfach vorkommende Ergebnisse ausgefiltert
# werden:

# %% tags=["start"]
# with engine.connect() as conn:
#     pprint(
#         conn.execute(
#             select(hotel_reservations.c.guest_id).order_by(
#                 hotel_reservations.c.guest_id
#             )
#         ).fetchall()
#     )

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Mehrfaches Einfügen des gleichen Primärschlüssels

# %%

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# ## Mini-Workshop: Autovermietung (Teil 2)
#
# Fügen Sie doe folgende Daten in die entsprechenden Tabellen ein. (Sie müssen die
# Daten dazu in das richtige Format bringen.)

# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
VEHICLES = [
    ("7HAC145", 1),
    ("CSD0201", 3),
    ("KVS4864", 1),
    ("KTH5512", 2),
    ("1213395", 2),
    ("6MEL208", 1),
    ("CP08523", 1),
]

# %% tags=["keep"]
CUSTOMERS = [
    ("Angela Nelson", "374245455400126"),
    ("Everlee Perkins", "60115564485789458"),
    ("Bentley Tyler", "2222420000001113"),
    ("Elle Waters", "378282246310005"),
    ("Willa Schultz", "4263982640269299"),
    ("Travis Bennet", "3530111333300000"),
    ("Wren Campbell", "6034932528973614"),
]

# %% tags=["keep"]
RENTALS = [
    # vehicle_id, customer_id, start and end date
    (3, 6, "2023-02-12", "2023-03-09"),
    (7, 1, "2023-02-18", "2023-03-16"),
    (2, 6, "2023-04-04", "2023-04-28"),
    (1, 2, "2023-07-05", "2023-08-03"),
    (7, 2, "2023-05-05", "2023-07-24"),
    (2, 5, "2023-05-06", "2023-05-07"),
    (2, 7, "2023-05-21", "2023-05-21"),
    (3, 7, "2023-06-30", "2023-07-06"),
    (4, 7, "2023-03-23", "2023-04-01"),
    (3, 1, "2023-07-02", "2023-07-04"),
    (1, 4, "2023-10-23", "2023-11-11"),
    (3, 4, "2023-07-23", "2023-07-28"),
    (5, 1, "2023-09-04", "2023-09-05"),
    (2, 5, "2023-11-14", "2023-11-15"),
]

# %%

# %%

# %% [markdown] lang="de"
#
# Ende des Workshops

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Select-Anweisungen

# %%

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Die Werte, die für jede Spalte zurückgegeben werden, können mit den üblichen
# Python-Operatoren modifiziert werden:

# %%

# %%

# %%

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Die Auswahl von Spalten kann durch die Angabe von `Column` statt `Table`-Objekten
# erreicht werden:

# %%

# %%

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Die Ergebnisse können mit `.where()` (und `and_()`, `or_()`) gefiltert (bzw.
# ergänzt)) werden

# %%

# %%

# %%

# %% tags=["keep"]
from sqlalchemy import and_, or_

# %%

# %%

# %%

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Die `FROM`-Klausel wird typischerweise automatisch erzeugt:

# %%

# %%

# %% [markdown] lang="de"
#
# Mit `select_from()` kann eine `FROM`-Klausel explizit angegeben werden:

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Wenn Spalten aus mehreren Tabellen kombiniert werden wird dabei das kartesische
# Produkt der Tabellen gebildet.
#
# Normalerweise ist das nicht das gewünschte Resultat!


# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Durch eine `WHERE`-Klausel kann das Ergebnis auf die gewünschten Zeilen
# beschränkt werden:

# %%

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Eine Alternative sind die `join_from()` und `join()` Methoden:

# %%

# %%

# %%

# %%

# %%

# %% [markdown] lang="de"
#
# Die Spalten der Joins werden durch Foreign-Key Constraints bestimmt.

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Mit der `order_by()` Methode können die Ergebnisse sortiert werden:

# %%

# %%

# %%

# %%

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# ## Mini-Workshop: Autovermietung (Teil 3)
#
# Schreiben Sie Select-Anweisungen für die folgenden Anfragen:
#
# - Buchungen von Autos, die nach dem 1.6.2023 begonnen haben, nach Startdatum geordnet
# - Die Namen aller Kunden, alphabetisch geordnet
# - Die Namen aller Kunden, die ein Auto ausgeliehen haben
# - Die Namen aller Kunden, die ein Auto der Preisklasse 3 ausgeliehen haben

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %%

# %%

# %%

# %% [markdown] lang="de"
#
# Ende des Workshops

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Aggregatfunktionen und Gruppierung

# %%

# %%

# %%

# %%

# %%

# %%

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# ## Mini-Workshop: Autovermietung (Teil 4)
#
# Schreiben Sie eine SQLAlchemy-Anfrage, die bestimmt, wie viele Autos
# in jeder Preisklasse gemietet wurden.

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Löschen und Ändern von Daten

# %%

# %%

# %%

# %%

# %%

# %%

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# ## Mini-Workshop: Autovermietung (Teil 5)
#
# - Löschen Sie das Auto mit ID 3. Was passiert mit der `rental_agreements` Tabelle?
# - Löschen Sie alle Vorkommen von Auto 3 aus der `rental_agreements` Tabelle.
# - Erhöhen Sie die `price_class` aller Autos um 1.

# %%

# %%

# %%

# %%

# %%

# %%
