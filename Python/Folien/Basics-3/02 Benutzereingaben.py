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
#  <b>Benutzereingaben</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 02 Benutzereingaben.py -->
# <!-- python_courses/slides/module_140_control_flow/topic_150_a3_user_input.py -->

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
#  # Benutzereingaben
#
#  - Die Funktion `input()` erlaubt es dem Benutzer einen Text einzugeben.
#  - Optional kann sie einen Eingabeprompt ausgeben.
#  - Die Funktion gibt den vom Benutzer eingegebenen Text *als String* zurück.

# %%
# input("What is your name? ")


# %%
def query_name():
    name = input("What is your name? ")
    print(f"You entered {name}.")


# %%
# query_name()

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Beispiel: Konvertierung von Temperaturen
#
# Wir wollen eine Anwendung schreiben, die den Benutzer nach einer Temperatur
# in Fahrenheit fragt und die entsprechende Temperatur in Grad Celsius
# zurückgibt.

# %% lang="de"
def konvertiere_fahrenheit_nach_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


# %% lang="de"
assert konvertiere_fahrenheit_nach_celsius(32) == 0.0

# %% lang="de"
import math

assert math.isclose(konvertiere_fahrenheit_nach_celsius(90), 32.222, abs_tol=0.001)

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Wir müssen den Rückgabewert von `input()` manuell in eine
# Zahl konvertieren, wenn wir damit rechnen wollen.

# %%
float("1.23")


# %% lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
def konvertiere_temperatur_1():
    fahrenheit = input("Bitte geben Sie die Temperatur in Fahrenheit ein: ")
    celsius = konvertiere_fahrenheit_nach_celsius(float(fahrenheit))
    print(f"{fahrenheit}F sind {celsius}°C")


# %% lang="de"
# konvertiere_temperatur_1()


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
#  Wir können eine Meldung ausgeben, wenn der Benutzer nichts eingibt (und die
#  Ausgabe etwas schöner gestalten):


# %% lang="de"
def konvertiere_temperatur_2():
    fahrenheit = input("Bitte geben Sie die Temperatur in Fahrenheit ein: ")
    if fahrenheit != "":
        celsius = konvertiere_fahrenheit_nach_celsius(float(fahrenheit))
        print(f"{float(fahrenheit):.1f}F sind {celsius:.1f}°C")
    else:
        print("Bitte geben Sie eine gültige Temperatur ein.")


# %% lang="de"
# konvertiere_temperatur_2()

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Wir können in der `if`-Anweisung Truthiness ausnutzen:

# %% lang="de" tags=["keep"]
def konvertiere_temperatur_3():
    fahrenheit = input("Bitte geben Sie die Temperatur in Fahrenheit ein: ")
    if fahrenheit:
        celsius = konvertiere_fahrenheit_nach_celsius(float(fahrenheit))
        print(f"{float(fahrenheit):.1f}F sind {celsius:.1f}°C")
    else:
        print("Bitte geben Sie eine gültige Temperatur ein.")


# %% lang="de"
# konvertiere_temperatur_3()


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Mini-Workshop: Umrechnung in Meilen
#
# Schreiben Sie eine Funktion `konvertiere_km_nach_meilen(km)` die den Wert
# `km` von Kilometer in Meilen umrechnet (d.h. die den Wert in Meilen
# zurückgibt).
#
# *Hinweis:*
# - Ein Kilometer entspricht $0,621371$ Meilen

# %% lang="de"
def konvertiere_km_nach_meilen(km):
    return km * 0.621371


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
# Testen Sie `konvertiere_km_nach_meilen(km)` für 1 und 5 km.

# %% lang="de"
import math

assert math.isclose(konvertiere_km_nach_meilen(1), 0.621371)

# %% lang="de"
assert math.isclose(konvertiere_km_nach_meilen(5), 3.107, abs_tol=0.001)


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Schreiben Sie eine Funktion `meilen_app()`, die eine Länge in Kilometern einliest
# und die äquivalente Entfernung in Meilen ausgibt. Wenn die Eingabe ein leerer
# String ist, soll der String `Bitte geben Sie eine gültige Entfernung in km ein.`
# ausgegeben werden.
#
# *Hinweise*
# - Ein String kann mit `float()` in einen Float-Wert umgewandelt werden.
# - Verwenden Sie Truthiness in der Bedingung der `if`-Anweisung.

# %% lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
def meilen_app():
    km = input("Bitte geben Sie eine Entfernung in km ein: ")
    if km:
        meilen = konvertiere_km_nach_meilen(float(km))
        print(f"{km} km sind {meilen} Meilen.")
    else:
        print("Bitte geben Sie eine gültige Entfernung in km ein.")


# %% lang="de"
# meilen_app()


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Mini-Workshop: Kino-Preis
#
# Das Python-Lichtspielhaus hat folgende Eintrittspreise:
#
# - Kleinkinder unter 2 Jahren sind frei.
# - Kinder von 2 bis 12 Jahren zahlen 2 Euro.
# - Teenager von 13 bis 17 Jahren zahlen 5 Euro.
# - Erwachsene zahlen 10 Euro.
# - Rentner (ab 65) zahlen 6 Euro.
#
# Schreiben Sie eine Funktion `kinopreis(alter)`, die den Preis in Abhängigkeit vom
# Alter berechnet und zurückgibt.


# %% lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
def kinopreis(alter):
    if alter < 2:
        return 0
    elif alter <= 12:
        return 2
    elif alter <= 17:
        return 5
    elif alter < 65:
        return 10
    else:
        return 6


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
# Testen Sie die Funktion `kinopreis()` für einige repräsentative Werte.

# %% lang="de"
assert kinopreis(1) == 0
assert kinopreis(7) == 2
assert kinopreis(15) == 5
assert kinopreis(25) == 10
assert kinopreis(70) == 6


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Schreiben Sie eine Funktion `drucke_kinopreis(alter)`,
# die einen Text der folgenden Art auf dem Bildschirm ausgibt:
#
# ```
# Sie sind 1 Jahr alt. Ihr Preis beträgt 0 Euro.
# Sie sind 15 Jahre alt. Ihr Preis beträgt 5 Euro.
# ```

# %% lang="de"
def drucke_kinopreis(alter):
    preis = kinopreis(alter)
    if alter == 1:
        print(f"Sie sind 1 Jahr alt. Ihr Preis beträgt {preis} Euro.")
    else:
        print(f"Sie sind {alter} Jahre alt. Ihr Preis beträgt {preis} Euro.")


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
# Testen Sie `drucke_kinopreis()` für repräsentative Werte.

# %% lang="de"
drucke_kinopreis(1)
drucke_kinopreis(7)
drucke_kinopreis(15)
drucke_kinopreis(25)
drucke_kinopreis(70)


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Schreiben Sie eine Funktion `kino_app()`, die ein Alter einliest und den
# Kinopreis für eine Person dieses Alters im gerade beschriebenen Format
# ausgibt. Zwei Beispielinteraktionen:
#
# ```
# Wie alt sind Sie? 37
# Sie sind 37 Jahre alt. Ihr Preis beträgt 10 Euro.
#
# Wie alt sind Sie? 12
# Sie sind 12 Jahre alt. Ihr Preis beträgt 2 Euro.
# ```

# %% lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
def kino_app():
    alter = input("Wie alt sind Sie? ")
    if alter:
        drucke_kinopreis(int(alter))
    else:
        print("Bitte geben Sie ein gültiges Alter ein.")

# %% lang="de"
# kino_app()

# %%
