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
# <img src="img/sql-table.svg"
#      style="display:block;margin:auto;width:60%"/>

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# <img src="img/sqlalchemy-metadata.svg"
#      style="display:block;margin:auto;width:60%"/>

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Metadata
#
# - `MetaData`: "Dictionary" für Tabellen
# - `Table`: Eine Tabelle in einer Datenbank
# - `Column`: Eine Spalte in einer Tabelle

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
from sqlalchemy import MetaData

# %%
metadata_obj = MetaData()

# %%
metadata_obj

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Wir wollen im Folgenden Tabellen für ein Hotel-Reservierungssystem
# mit der SQLAlchemy Expression Language anlegen.

# %%
from sqlalchemy import Table, Column, Integer, String

# %%
guests = Table(
    "guests",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("name", String(30)),
    Column("email", String),
)

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
guests

# %%
guests.c

# %%
guests.c.keys()

# %%
guests.c["id"]

# %%
guests.c.id

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
strange_table = Table(
    "strange",
    metadata_obj,
    Column("keys", Integer),
)

# %%
strange_table.c.keys()

# %%
strange_table.c["keys"]

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
from sqlalchemy import ForeignKey, Date

# %% tags=["alt"]
hotel_reservations = Table(
    "reservations",
    metadata_obj,
    Column("guest_id", ForeignKey("guests.id", ondelete="CASCADE"), primary_key=True),
    Column("check_in_date", Date, primary_key=True),
    Column("check_out_date", Date),
    Column("room_number", Integer),
)

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
hotel_reservations.c.keys()

# %%
hotel_reservations.c.guest_id

# %%
hotel_reservations.c["check_in_date"]

# %%
hotel_reservations.primary_key

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
from sqlalchemy import create_engine

# %%
engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
metadata_obj.create_all(engine)

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
# - `rental_agreements` mit Spalten `customer_id` (Fremdschlüssel), `vehicle_id`
#    (Fremdschlüssel), `start_date` (Date) und `end_date` (Date)
#
# Implementieren Sie dieses Datenmodell in SQLAlchemy und erzeugen Sie die Tabellen.

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
from sqlalchemy import MetaData, Table, Column, Integer, String, Date, ForeignKey

# %%
car_rental_metadata = MetaData()

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
vehicles = Table(
    "vehicles",
    car_rental_metadata,
    Column("id", Integer, primary_key=True),
    Column("license_plate", String),
    Column("price_class", Integer),
)

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
customers = Table(
    "customers",
    car_rental_metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String),
    Column("credit_card_number", String),
)

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
rental_agreements = Table(
    "rental_agreements",
    car_rental_metadata,
    Column("vehicle_id", ForeignKey("vehicles.id", ondelete="CASCADE")),
    Column("customer_id", ForeignKey("customers.id")),
    Column("start_date", Date),
    Column("end_date", Date),
)

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
car_rental_engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)

# %%
car_rental_metadata.create_all(car_rental_engine)

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Ende des Workshops

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# ### Datenbank-Query mit String

# %% tags=["keep"]
from pprint import pprint

# %% tags=["keep"]
from sqlalchemy import text

# %% tags=["keep"]
with engine.connect() as conn:
    pprint(conn.execute(text("SELECT * from sqlite_master")).all())

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# ### Erzeugen einer Tabelle durch Reflection
#
# SQLAlchemy kann ein `Table`-Objekt aus einer existierenden
# Datenbank-Tabelle erzeugen:

# %%
sqlite_master = Table("sqlite_master", metadata_obj, autoload_with=engine)

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
sqlite_master

# %%
sqlite_master.c.keys()

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### Datenbank-Query mit SQLAlchemy Expression Language

# %%
from sqlalchemy import select

# %%
stmt = select(sqlite_master)
stmt

# %%
type(stmt)

# %%
print(stmt)

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
with engine.connect() as conn:
    pprint(conn.execute(stmt).fetchall())

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
with engine.connect() as conn:
    pprint(conn.execute(select(sqlite_master)).all())

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Insert Anweisungen

# %%
from sqlalchemy import insert

# %%
guests

# %%
insert(guests)

# %%
print(insert(guests))

# %%
print(insert(guests).values(id=1))

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
with engine.connect() as conn:
    conn.execute(insert(guests).values(id=1))
    conn.commit()

# %%
with engine.connect() as conn:
    pprint(conn.execute(select(guests)).all())

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
with engine.begin() as conn:
    conn.execute(insert(guests).values(name="Andre Reyes", email="andre@reyes.com"))

# %%
with engine.connect() as conn:
    pprint(conn.execute(select(guests)).all())


# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
stmt = insert(guests).values(id=1, name="Andre Reyes", email="andre@reyes.com")

# %%
compiled_stmt = stmt.compile()

# %%
compiled_stmt.string

# %%
compiled_stmt.params


# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
GUESTS = [
    {"name": "Theo Brown", "email": "theo.brown@fastmail.org"},
    {"name": "Alayna Rogers", "email": "arogers@gmail.com"},
    {"name": "June Abbott", "email": "june.abbott@yahoo.com"},
    {"name": "Langosh Kaleigh", "email": "langosh.kaleigh@kiehn.org"},
    {"name": "Andre Reyes", "email": "a.reyes@runolfsdottir.info"},
    {"name": "Xander Richardson", "email": "xander@krajcik.net"},
    {"name": "Jayla Ruiz", "email": "jayla@ruiz.net"},
]

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
with engine.begin() as conn:
    conn.execute(insert(guests), GUESTS)

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
with engine.connect() as conn:
    pprint(conn.execute(select(guests)).fetchall())

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
from datetime import date


# %%
def d(iso_string: str) -> date:
    return date.fromisoformat(iso_string)


# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
RESERVATIONS = [
    (2, d("2023-03-02"), d("2023-03-02"), 123),
    (3, d("2023-03-04"), d("2023-03-07"), 254),
    (2, d("2023-03-06"), d("2023-03-12"), 135),
    (4, d("2023-04-11"), d("2023-04-22"), 312),
    (3, d("2023-04-17"), d("2023-04-23"), 218),
    (5, d("2023-05-02"), d("2023-05-08"), 4),
]

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
RESERVATION_DICTS = [
    {
        "guest_id": guest_id,
        "check_in_date": check_in_date,
        "check_out_date": check_out_date,
        "room_number": room_number,
    }
    for guest_id, check_in_date, check_out_date, room_number in RESERVATIONS
]

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
RESERVATION_DICTS

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
with engine.begin() as conn:
    conn.execute(insert(hotel_reservations), RESERVATION_DICTS)

# %%
with engine.connect() as conn:
    pprint(conn.execute(select(hotel_reservations)).all())

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Mit der `distinct()`-Methode können mehrfach vorkommende Ergebnisse ausgefiltert
# werden:

# %% tags=["alt"]
with engine.connect() as conn:
    pprint(
        conn.execute(
            select(hotel_reservations.c.guest_id)
            .order_by(hotel_reservations.c.guest_id)
            .distinct()
        ).fetchall()
    )

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Mehrfaches Einfügen des gleichen Primärschlüssels

# %%
# with engine.begin() as conn:
#     conn.execute(
#         insert(guests),
#         {"id": 1, "name": "Aliyah Patel", "email": "ap@ward.info"}
#     )

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# ## Mini-Workshop: Autovermietung (Teil 2)
#
# Wir haben im vorhergehenden Workshop die Tabellen für eine Autovermietung
# angelegt.
#
# Fügen Sie jetzt die folgenden Daten in diese Tabellen ein. (Sie müssen
# die Daten dazu in das richtige Format bringen.)

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

# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
CUSTOMERS = [
    ("Angela Nelson", "374245455400126"),
    ("Everlee Perkins", "60115564485789458"),
    ("Bentley Tyler", "2222420000001113"),
    ("Elle Waters", "378282246310005"),
    ("Willa Schultz", "4263982640269299"),
    ("Travis Bennet", "3530111333300000"),
    ("Wren Campbell", "6034932528973614"),
]

# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
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

# %% tags=["subslide", "alt"] slideshow={"slide_type": "subslide"}
VEHICLE_DICTS = [
    {"license_plate": license_plate, "price_class": price_class}
    for license_plate, price_class in VEHICLES
]

# %% tags=["subslide", "alt"] slideshow={"slide_type": "subslide"}
CUSTOMER_DICTS = [
    {"name": name, "credit_card_number": credit_card_number}
    for name, credit_card_number in CUSTOMERS
]

# %% tags=["subslide", "alt"] slideshow={"slide_type": "subslide"}
RENTAL_DICTS = [
    {
        "vehicle_id": vehicle_id,
        "customer_id": customer_id,
        "start_date": d(start_date),
        "end_date": d(end_date),
    }
    for vehicle_id, customer_id, start_date, end_date in RENTALS
]


# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
with car_rental_engine.begin() as conn:
    conn.execute(
        insert(vehicles),
        VEHICLE_DICTS,
    )
    conn.execute(
        insert(customers),
        CUSTOMER_DICTS,
    )
    conn.execute(
        insert(rental_agreements),
        RENTAL_DICTS,
    )

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Überprüfen Sie mit Select-Anweisungen, dass die Daten in die Tabellen eingefügt
# wurden.

# %%
with car_rental_engine.connect() as conn:
    pprint(conn.execute(select(customers)).fetchall())

# %% tags=["alt", "subslide"] slideshow={"slide_type": "subslide"}
with car_rental_engine.connect() as conn:
    pprint(conn.execute(select(vehicles)).fetchall())

# %% tags=["alt", "subslide"] slideshow={"slide_type": "subslide"}
with car_rental_engine.connect() as conn:
    pprint(conn.execute(select(rental_agreements)).fetchall())

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Ende des Workshops

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Select-Anweisungen

# %%
from sqlalchemy import select

# %%
print(select(guests))

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Die Werte, die für jede Spalte zurückgegeben werden, können mit den üblichen
# Python-Operatoren modifiziert werden:

# %%
guests.c.email

# %%
"Email: " + guests.c.email

# %%
stmt = select("Email: " + guests.c.email)
stmt

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
with engine.connect() as conn:
    for (email,) in conn.execute(stmt):
        print(email)

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
stmt = select(guests.c.id * 10, guests.c.id > 3, "Email: " + guests.c.email)

# %%
with engine.connect() as conn:
    for num, test, email in conn.execute(stmt):
        print(f"num: {num}, test: {test}, {email}")

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Die Auswahl von Spalten kann durch die Angabe von `Column` statt `Table`-Objekten
# erreicht werden:

# %%
stmt = select(guests.c.name, guests.c.email)
print(stmt)

# %%
with engine.connect() as conn:
    for row in conn.execute(stmt):
        if row.name is not None:
            print(f"{row.name:17}  |  {row.email}")

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
print(select(guests.c["name", "email"]))

# %%
with engine.connect() as conn:
    for name, email in conn.execute(select(guests.c["name", "email"]).distinct()):
        if name is not None:
            print(f"{name:17}  |  {email}")

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Die Ergebnisse können mit `.where()` (und `and_()`, `or_()`) gefiltert (bzw.
# ergänzt)) werden

# %%
print(select(guests).where(guests.c.name == "Andre Reyes"))

# %%
print(select(guests).where(guests.c.name == "Andre Reyes").where(guests.c.id == 2))

# %%
print(select(guests).where(guests.c.name == "Andre Reyes", guests.c.id == 2))

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
from sqlalchemy import and_, or_

# %%
and_stmt = select(guests).where(and_(guests.c.name == "Andre Reyes", guests.c.id == 2))
print(and_stmt)

# %%
or_stmt = select(guests).where(or_(guests.c.name == "Andre Reyes", guests.c.id == 4))
print(or_stmt)

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
with engine.connect() as conn:
    pprint(conn.execute(and_stmt).fetchall())

# %%
with engine.connect() as conn:
    pprint(conn.execute(or_stmt).fetchall())

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Die `FROM`-Klausel wird typischerweise automatisch erzeugt:

# %%
stmt = select(guests.c.name)
print(stmt)

# %%
stmt = select(guests.c.name, hotel_reservations.c.check_in_date)
print(stmt)

# %% [markdown] lang="de"
#
# Mit `select_from()` kann eine `FROM`-Klausel explizit angegeben werden:

# %% tags=["keep"]
stmt = select(guests.c.name).select_from(guests, hotel_reservations)
print(stmt)

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Wenn Spalten aus mehreren Tabellen kombiniert werden wird dabei das kartesische
# Produkt der Tabellen gebildet.
#
# Normalerweise ist das nicht das gewünschte Resultat!


# %%
with engine.connect() as conn:
    pprint(conn.execute(stmt).fetchall())

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Durch eine `WHERE`-Klausel kann das Ergebnis auf die gewünschten Zeilen
# beschränkt werden:

# %% tags=["alt"]
stmt = select(guests.c.name, hotel_reservations.c.check_in_date).where(
    guests.c.id == hotel_reservations.c.guest_id
)
print(stmt)

# %%
with engine.connect() as conn:
    pprint(conn.execute(stmt).fetchall())

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Eine Alternative sind die `join_from()` und `join()` Methoden:

# %%
stmt = select(guests.c.name, hotel_reservations.c.check_in_date).join_from(
    guests, hotel_reservations
)
print(stmt)

# %%
with engine.connect() as conn:
    pprint(conn.execute(stmt).fetchall())

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
print(
    select(guests.c.name, hotel_reservations.c.check_in_date).join(hotel_reservations)
)

# %%
stmt = select(guests.c.name, hotel_reservations.c.check_in_date).join(guests)
print(stmt)

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
with engine.connect() as conn:
    pprint(conn.execute(stmt).all())

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# - Die Spalten der Joins werden durch Foreign-Key Constraints bestimmt.
# - Wir können sie aber auch explizit angeben:

# %% tags=["alt", "subslide"] slideshow={"slide_type": "subslide"}
with engine.connect() as conn:
    pprint(
        conn.execute(
            select(guests, hotel_reservations.c.room_number).join(
                hotel_reservations,
                onclause=guests.c.id == hotel_reservations.c.room_number,
            )
        ).all()
    )

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Mit der `order_by()` Methode können die Ergebnisse sortiert werden:

# %%
stmt = select(hotel_reservations).order_by(hotel_reservations.c.check_in_date)
print(stmt)

# %%
with engine.connect() as conn:
    pprint(conn.execute(stmt).fetchall())

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
stmt = select(hotel_reservations).order_by(hotel_reservations.c.room_number)
print(stmt)

# %%
with engine.connect() as conn:
    pprint(conn.execute(stmt).fetchall())

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
with car_rental_engine.connect() as conn:
    pprint(
        conn.execute(
            select(rental_agreements)
            .where(rental_agreements.c.start_date > d("2023-06-01"))
            .order_by(rental_agreements.c.start_date)
        ).fetchall()
    )

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
with car_rental_engine.connect() as conn:
    pprint(conn.execute(select(customers.c.name).order_by(customers.c.name)).fetchall())

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
with car_rental_engine.connect() as conn:
    pprint(
        conn.execute(
            select(customers.c.name)
            .distinct()
            .join(rental_agreements)
            .order_by(customers.c.name)
        ).fetchall()
    )

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
with car_rental_engine.connect() as conn:
    pprint(
        conn.execute(
            select(customers.c.name)
            .distinct()
            .where(customers.c.id == rental_agreements.c.customer_id)
            .where(rental_agreements.c.vehicle_id == vehicles.c.id)
            .where(vehicles.c.price_class == 3)
            .order_by(customers.c.name)
        ).fetchall()
    )

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Ende des Workshops

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Aggregatfunktionen und Gruppierung

# %%
from sqlalchemy import func

# %%
print(select(func.count("*")))

# %%
stmt = select(func.count(hotel_reservations.c.guest_id))
print(stmt)

# %%
with engine.connect() as conn:
    pprint(conn.execute(select(hotel_reservations.c.guest_id)).fetchall())
    pprint(conn.execute(stmt).fetchall())

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# SQL Query, die die Anzahl der Buchungen pro Gast bestimmt:

# %%
stmt = select(
    hotel_reservations.c.guest_id, func.count(hotel_reservations.c.check_in_date)
).group_by(hotel_reservations.c.guest_id)
print(stmt)

# %%
with engine.connect() as conn:
    pprint(conn.execute(stmt).fetchall())

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# - Die angegebene Query gibt uns aber nur die IDs der Gäste zurück.
# - Wenn wir den Namen des Gastes haben wollen, müssen wir mit einem Join über mehrere
#   Tabellen arbeiten:

# %%
stmt = (
    select(guests.c.name, func.count(hotel_reservations.c.check_in_date))
    .join_from(guests, hotel_reservations)
    .group_by(hotel_reservations.c.guest_id)
)
print(stmt)

# %% tags=["alt"]
with engine.connect() as conn:
    pprint(conn.execute(stmt).all())

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# ## Mini-Workshop: Autovermietung (Teil 4)
#
# Schreiben Sie eine SQLAlchemy-Anfrage, die bestimmt, wie viele Autos
# in jeder Preisklasse gemietet wurden.

# %%
with car_rental_engine.connect() as conn:
    results = conn.execute(
        select(vehicles.c.price_class, func.count(rental_agreements.c.vehicle_id))
        .join(rental_agreements)
        .group_by(vehicles.c.price_class)
    ).fetchall()
    for pc, num in results:
        print(f"Price class {pc} was rented {num} times.")

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Löschen und Ändern von Daten

# %%
with engine.connect() as conn:
    pprint(conn.execute(select(guests)).all())

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
from sqlalchemy import delete, update

# %%
with engine.begin() as conn:
    conn.execute(delete(guests).where(guests.c.id == 2))

# %%
with engine.connect() as conn:
    pprint(conn.execute(select(guests)).fetchall())

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
with engine.begin() as conn:
    conn.execute(
        update(guests)
        .where(guests.c.id == 1)
        .values(name="Ted Green", email="ted@greenery.org")
    )

# %%
with engine.connect() as conn:
    pprint(conn.execute(select(guests)).fetchall())

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# ## Mini-Workshop: Autovermietung (Teil 5)
#
# - Löschen Sie das Auto mit ID 3. Was passiert mit der `rental_agreements` Tabelle?
# - Löschen Sie alle Vorkommen von Auto 3 aus der `rental_agreements` Tabelle,
#   falls erforderlich.
# - Erhöhen Sie die `price_class` aller Autos um 1.

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
with car_rental_engine.begin() as conn:
    conn.execute(delete(vehicles).where(vehicles.c.id == 3))

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
with car_rental_engine.connect() as conn:
    pprint(conn.execute(select(vehicles)).fetchall())
    pprint(conn.execute(select(rental_agreements)).all())

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
with car_rental_engine.begin() as conn:
    conn.execute(delete(rental_agreements).where(rental_agreements.c.vehicle_id == 3))

# %%
with car_rental_engine.connect() as conn:
    pprint(conn.execute(select(rental_agreements)).fetchall())

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
with car_rental_engine.connect() as conn:
    pprint(conn.execute(select(vehicles)).fetchall())

# %%
with car_rental_engine.begin() as conn:
    pprint(
        conn.execute(update(vehicles).values(price_class=vehicles.c.price_class + 1))
    )

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
with car_rental_engine.connect() as conn:
    pprint(conn.execute(select(vehicles)).fetchall())
