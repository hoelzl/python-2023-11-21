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
from sqlalchemy import MetaData
from pprint import pprint

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

# %%
guests

# %%
guests.c

# %%
guests.c.keys()

# %%
guests.c["id"]

# %%
guests.c.id

# %%
strange_table = Table(
    "strange",
    metadata_obj,
    Column("keys", Integer),
)

# %%
strange_table.c.keys()

# %%
strange_table.c["keys"]

# %%
from sqlalchemy import ForeignKey, Date

# %%
hotel_reservations = Table(
    "reservations",
    metadata_obj,
    Column("guest_id", ForeignKey("guests.id"), primary_key=True),
    Column("check_in_date", Date, primary_key=True),
    Column("check_out_date", Date),
    Column("room_number", Integer),
)

# %%
hotel_reservations.c.keys()

# %%
hotel_reservations.c.guest_id

# %%
hotel_reservations.c["check_in_date"]

# %%
hotel_reservations.primary_key

# %%
from sqlalchemy import create_engine

# %%
engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)

# %%
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
# - `rental_agreements` mit Spalten `customer_id`, `vehicle_id`,
#   `start_date`, `end_date`
#
# Implementieren Sie dieses Datenmodell in SQLAlchemy und erzeugen Sie die Tabellen.

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
from sqlalchemy import MetaData, Table, Column, Integer, String, Date, ForeignKey

# %%
car_rental_metadata = MetaData()

# %%
vehicles = Table(
    "vehicles",
    car_rental_metadata,
    Column("id", Integer, primary_key=True),
    Column("license_plate", String),
    Column("price_class", Integer),
)

# %%
customers = Table(
    "customers",
    car_rental_metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String),
    Column("credit_card_number", String),
)

# %%
rental_agreements = Table(
    "rental_agreements",
    car_rental_metadata,
    Column("vehicle_id", ForeignKey("vehicles.id")),
    Column("customer_id", ForeignKey("customers.id")),
    Column("start_date", Date),
    Column("end_date", Date),
)

# %%
car_rental_engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)

# %%
car_rental_metadata.create_all(car_rental_engine)

# %% [markdown] lang="de"
#
# Ende des Workshops

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### Datenbank-Query mit String

# %%
from sqlalchemy import text

# %%
with engine.connect() as conn:
    pprint(conn.execute(text("SELECT * from sqlite_master")).fetchall())

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### Erzeugen einer Tabelle durch Reflection
#
# SQLAlchemy kann ein `Table`-Objekt aus einer existierenden
# Datenbank-Tabelle erzeugen:

# %%
sqlite_master = Table("sqlite_master", metadata_obj, autoload_with=engine)

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### Datenbank-Query mit SQLAlchemy Expression Language

# %%
from sqlalchemy import select

# %%
stmt = select(sqlite_master)
stmt

# %%
print(stmt)

# %%
with engine.connect() as conn:
    pprint(conn.execute(stmt).fetchall())

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Insert Anweisungen

# %%
from sqlalchemy import insert

# %%
insert(guests)

# %%
print(insert(guests))

# %%
print(insert(guests).values(id=1))

# %%
stmt = insert(guests).values(id=1)

# %%
compiled_stmt = stmt.compile()

# %%
compiled_stmt.string

# %%
compiled_stmt.params

# %%
with engine.connect() as conn:
    conn.execute(insert(guests).values(id=1))
    conn.commit()

# %%
with engine.connect() as conn:
    pprint(conn.execute(select(guests)).fetchall())

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
with engine.begin() as conn:
    conn.execute(insert(guests), GUESTS)

# %%
with engine.connect() as conn:
    pprint(conn.execute(select(guests)).fetchall())

# %%
from datetime import date


# %%
def d(iso_string: str) -> date:
    return date.fromisoformat(iso_string)


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
with engine.begin() as conn:
    conn.execute(insert(hotel_reservations), RESERVATIONS)

# %%
with engine.connect() as conn:
    pprint(conn.execute(select(hotel_reservations)).fetchall())

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
#         insert(guest_table),
#         {"id": 1, "name": "Aliyah Patel", "email": "ap@ward.info"}
#     )

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
with car_rental_engine.begin() as conn:
    conn.execute(
        insert(vehicles),
        [
            {"license_plate": license_plate, "price_class": price_class}
            for license_plate, price_class in VEHICLES
        ],
    )
    conn.execute(
        insert(customers),
        [
            {"name": name, "credit_card_number": credit_card_number}
            for name, credit_card_number in CUSTOMERS
        ],
    )
    conn.execute(
        insert(rental_agreements),
        [
            {
                "vehicle_id": vehicle_id,
                "customer_id": customer_id,
                "start_date": d(start_date),
                "end_date": d(end_date),
            }
            for vehicle_id, customer_id, start_date, end_date in RENTALS
        ],
    )

# %%
with car_rental_engine.connect() as conn:
    pprint(conn.execute(select(customers)).fetchall())
    pprint(conn.execute(select(vehicles)).fetchall())
    pprint(conn.execute(select(rental_agreements)).fetchall())

# %% [markdown] lang="de"
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
stmt = select("Email: " + guests.c.email)

# %%
with engine.connect() as conn:
    for (email,) in conn.execute(stmt):
        print(email)

# %%
stmt = select(guests.c.id > 3, "Email: " + guests.c.email)

# %%
with engine.connect() as conn:
    for test, email in conn.execute(stmt):
        print(test, email)

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Die Auswahl von Spalten kann durch die Angabe von `Column` statt `Table`-Objekten
# erreicht werden:

# %%
stmt = select(guests.c.name, guests.c.email).where(guests.c.id >= 2)
print(stmt)

# %%
with engine.connect() as conn:
    for row in conn.execute(stmt):
        print(f"{row.name:17}  |  {row.email}")

# %%
print(select(guests.c["name", "email"]).where(guests.c.id >= 2))

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

# %% tags=["keep"]
from sqlalchemy import and_, or_

# %%
and_stmt = select(guests).where(and_(guests.c.name == "Andre Reyes", guests.c.id == 2))
print(and_stmt)

# %%
or_stmt = select(guests).where(or_(guests.c.name == "Andre Reyes", guests.c.id == 2))
print(or_stmt)

# %%
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

# %%
stmt = select(guests.c.name).select_from(guests)
print(stmt)

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Wenn Spalten aus mehreren Tabellen kombiniert werden wird dabei das kartesische
# Produkt der Tabellen gebildet.
#
# Normalerweise ist das nicht das gewünschte Resultat!


# %%
# with engine.connect() as conn:
#     pprint(conn.execute(stmt).fetchall())

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Durch eine `WHERE`-Klausel kann das Ergebnis auf die gewünschten Zeilen
# beschränkt werden:

# %%
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

# %%
print(
    select(guests.c.name, hotel_reservations.c.check_in_date).join(hotel_reservations)
)

# %%
stmt = select(guests.c.name, hotel_reservations.c.check_in_date).join(guests)
print(stmt)

# %%
with engine.connect() as conn:
    pprint(conn.execute(stmt).fetchall())

# %% [markdown] lang="de"
#
# Die Spalten der Joins werden durch Foreign-Key Constraints bestimmt.

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Mit der `order_by()` Methode können die Ergebnisse sortiert werden:

# %%
stmt = select(hotel_reservations).order_by(hotel_reservations.c.check_in_date)
print(stmt)

# %%
with engine.connect() as conn:
    pprint(conn.execute(stmt).fetchall())

# %%
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

# %%
with car_rental_engine.connect() as conn:
    pprint(conn.execute(select(customers.c.name).order_by(customers.c.name)).fetchall())

# %%
with car_rental_engine.connect() as conn:
    pprint(
        conn.execute(
            select(customers.c.name)
            .distinct()
            .join(rental_agreements)
            .order_by(customers.c.name)
        ).fetchall()
    )

# %%
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

# %% [markdown] lang="de"
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

# %%
stmt = select(
    hotel_reservations.c.guest_id, func.count(hotel_reservations.c.check_in_date)
).group_by(hotel_reservations.c.guest_id)

# %%
with engine.connect() as conn:
    pprint(conn.execute(stmt).fetchall())

# %% tags=["alt"]
stmt = (
    select(guests.c.name, func.count(hotel_reservations.c.check_in_date))
    .join_from(guests, hotel_reservations)
    .group_by(hotel_reservations.c.guest_id)
)
print(stmt)

# %% tags=["alt"]
with engine.connect() as conn:
    pprint(conn.execute(stmt).fetchall())

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
    pprint(conn.execute(select(guests)).fetchall())

# %%
from sqlalchemy import delete, update

# %%
with engine.begin() as conn:
    conn.execute(delete(guests).where(guests.c.id == 2))

# %%
with engine.connect() as conn:
    pprint(conn.execute(select(guests)).fetchall())

# %%
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
# - Löschen Sie alle Vorkommen von Auto 3 aus der `rental_agreements` Tabelle.
# - Erhöhen Sie die `price_class` aller Autos um 1.

# %%
with car_rental_engine.begin() as conn:
    conn.execute(delete(vehicles).where(vehicles.c.id == 3))

# %%
with car_rental_engine.connect() as conn:
    pprint(conn.execute(select(vehicles)).fetchall())
    pprint(conn.execute(select(rental_agreements)).fetchall())

# %%
with car_rental_engine.begin() as conn:
    conn.execute(delete(rental_agreements).where(rental_agreements.c.vehicle_id == 3))

# %%
with car_rental_engine.connect() as conn:
    pprint(conn.execute(select(rental_agreements)).fetchall())

# %% tags=["alt"]
with car_rental_engine.connect() as conn:
    pprint(conn.execute(select(vehicles)).fetchall())

# %%
with car_rental_engine.begin() as conn:
    pprint(
        conn.execute(update(vehicles).values(price_class=vehicles.c.price_class + 1))
    )

# %%
with car_rental_engine.connect() as conn:
    pprint(conn.execute(select(vehicles)).fetchall())
