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
#  <b>Kontrollstrukturen (Teil 2)</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 07 Kontrollstrukturen (Teil 2).py -->
# <!-- python_courses/slides/module_140_control_flow/topic_122_b1_control_flow_part2.py -->

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Einseitiges `if`

# %% lang="de" tags=["keep"]
def einseitiges_if(zahl):
    print("Vorher")
    if zahl == 7:
        print(zahl, "ist eine Glückszahl")
        print("Glückwunsch!")
    print("Nachher")


# %% lang="de" tags=["keep"]
einseitiges_if(1)

# %% lang="de" tags=["keep"]
einseitiges_if(7)


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
#  ## Mehrere Zweige
#
#  - Wir wollen ein Spiel schreiben, in dem der Spieler eine Zahl zwischen 1 und
#    100 erraten muss.
#  - Nachdem er geraten hat, bekommt er die Information, ob seine Zahl zu hoch,
#    zu niedrig oder richtig war angezeigt.
#  - Später wollen wir dem Spieler mehrere Versuche erlauben.

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
#  ## Struktur einer `if`-Anweisung (vollständig):
#
# ```python
# if {Bedingung 1}:
#     Rumpf, der ausgeführt wird, wenn {Bedingung 1} wahr ist
# elif {Bedingung 2}:
#     Rumpf, der ausgeführt wird, wenn {Bedingung 2} wahr ist
# ...
# else:
#     Rumpf, der ausgeführt wird, wenn keine der Bedingungen wahr ist
# ```
# - Nur das `if` und der erste Rumpf sind notwendig
# - Falls ein `elif` oder ein `else` vorhanden ist, so darf der entsprechende
#   Rumpf nicht leer sein

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
# ## Mini-Workshop: Positiv / Negativ
#
# Schreiben Sie eine Funktion `drucke_ist_positiv(zahl)`, die
#
# - `{zahl} ist positiv.` auf dem Bildschirm ausgibt, falls `zahl > 0` ist,
# - `{zahl} ist Null.` auf dem Bildschirm ausgibt, falls `zahl == 0` ist,
# - `{zahl} ist negativ.` auf dem Bildschirm ausgibt, falls `zahl < 0` ist.

# %% lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
# Testen Sie `drucke_ist_positiv(zahl)` mit den Werten -3, 0 und 2.

# %% lang="de"
