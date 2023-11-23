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
#  <b>Kontrollstrukturen (Teil 3)</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 01 Kontrollstrukturen (Teil 3).py -->
# <!-- python_courses/slides/module_140_control_flow/topic_140_b1_more_control_flow.py -->

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
#  ## Bessere Klassifizierung
#
# In einem der letzten Videos hatten wir die folgende Funktion zur Klassifizierung
# von Zahlen eingeführt:

# %% lang="de" tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
def klassifiziere_zahl(geratene_zahl, lösung):
    if geratene_zahl < lösung:
        print("Die geratene Zahl ist zu klein!")
    elif geratene_zahl > lösung:
        print("Die geratene Zahl ist zu groß!")
    else:
        print("Sie haben gewonnen!")


# %% lang="de" tags=["keep"]
klassifiziere_zahl(10, 12)

# %% lang="de" tags=["keep"]
klassifiziere_zahl(14, 12)

# %% lang="de" tags=["keep"]
klassifiziere_zahl(12, 12)


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Wir wollen dem Spieler jetzt etwas mehr Information geben, wie nahe er an der
# richtigen Lösung ist:
#
# - Teile dem Spieler mit, wenn die geratene Zahl sehr weit von der gesuchten Zahl
#   entfernt ist
# - Ausgabe: "Die geratene Zahl ist viel zu klein/zu groß!", wenn der Unterschied
#   größer als 10 ist

# %% lang="de" tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
def klassifiziere_zahl_2(geratene_zahl, lösung):
    if geratene_zahl < lösung - 10:
        print("Die geratene Zahl ist viel zu klein!")
    elif geratene_zahl < lösung:
        print("Die geratene Zahl ist zu klein!")
    elif geratene_zahl > lösung + 10:
        print("Die geratene Zahl ist viel zu groß!")
    elif geratene_zahl > lösung:
        print("Die geratene Zahl ist zu groß!")
    else:
        print("Sie haben gewonnen!")


# %% lang="de" tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
klassifiziere_zahl_2(1, 12)

# %% lang="de" tags=["keep"]
klassifiziere_zahl_2(10, 12)

# %% lang="de" tags=["keep"]
klassifiziere_zahl_2(14, 12)

# %% lang="de" tags=["keep"]
klassifiziere_zahl_2(24, 12)

# %% lang="de" tags=["keep"]
klassifiziere_zahl_2(12, 12)


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
#  Die Reihenfolge der `if`- und `elif`-Zweige ist wichtig:

# %% lang="de" tags=["keep"]
def klassifiziere_zahl_3(geratene_zahl, lösung):
    if geratene_zahl < lösung:
        print("Die geratene Zahl ist zu klein!")
    elif geratene_zahl < lösung - 10:
        print("Die geratene Zahl ist viel zu klein!")
    elif geratene_zahl > lösung:
        print("Die geratene Zahl ist zu groß!")
    elif geratene_zahl > lösung + 10:
        print("Die geratene Zahl ist viel zu groß!")
    else:
        print("Sie haben gewonnen!")


# %% lang="de" tags=["keep"]
klassifiziere_zahl_3(1, 12)

# %% lang="de" tags=["keep"]
klassifiziere_zahl_3(100, 12)


# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
#  ## Return aus einem `if`-Statement
#
#  Die Zweige eines `if`-Statements können `return` Anweisungen enthalten um
#  einen Wert aus einer Funktion zurückzugeben:

# %% lang="de"
def klassifiziere_zahl_4(zahl):
    if zahl > 100:
        return "groß"
    else:
        return "klein"


# %% lang="de"
klassifiziere_zahl_4(1)

# %% lang="de"
klassifiziere_zahl_4(200)


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Mini-Workshop: Signum
#
# Schreiben Sie eine Funktion `signum(zahl)`, die
#
# - 1 zurückgibt, falls `zahl > 0` ist,
# - 0 zurückgibt, falls `zahl == 0` ist,
# - -1 zurückgibt, falls `zahl < 0` ist.

# %% lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
def signum(zahl):
    if zahl > 0:
        return 1
    elif zahl == 0:
        return 0
    else:
        return -1


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
# Testen Sie die Funktion für repräsentative Werte.

# %% lang="de"
assert signum(-10) == -1

# %% lang="de"
assert signum(0) == 0

# %% lang="de"
assert signum(2) == 1
