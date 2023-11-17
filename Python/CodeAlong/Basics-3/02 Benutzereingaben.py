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


# %%

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Beispiel: Konvertierung von Temperaturen
#
# Wir wollen eine Anwendung schreiben, die den Benutzer nach einer Temperatur
# in Fahrenheit fragt und die entsprechende Temperatur in Grad Celsius
# zurückgibt.

# %% lang="de"

# %% lang="de"

# %% lang="de"

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Wir müssen den Rückgabewert von `input()` manuell in eine
# Zahl konvertieren, wenn wir damit rechnen wollen.

# %%

# %% lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}


# %% lang="de"


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
#  Wir können eine Meldung ausgeben, wenn der Benutzer nichts eingibt (und die
#  Ausgabe etwas schöner gestalten):


# %% lang="de"

# %% lang="de"

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

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
# Testen Sie `konvertiere_km_nach_meilen(km)` für 1 und 5 km.

# %% lang="de"

# %% lang="de"

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


# %% lang="de"


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


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
# Testen Sie die Funktion `kinopreis()` für einige repräsentative Werte.

# %% lang="de"

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

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
# Testen Sie `drucke_kinopreis()` für repräsentative Werte.

# %% lang="de"

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

# %% lang="de"

# %%
