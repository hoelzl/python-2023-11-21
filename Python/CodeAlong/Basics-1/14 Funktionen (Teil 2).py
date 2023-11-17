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
#  <b>Funktionen (Teil 2)</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 14 Funktionen (Teil 2).py -->
# <!-- python_courses/slides/module_130_functions/topic_112_b1_functions_part2.py -->

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
# ## Visualisierung auf Python Tutor
#
# Visualisierung auf der
# [Python Tutor](https://pythontutor.com/render.html#code=def%20pythagoras%28a,%20b%29%3A%0A%20%20%20%20c%20%3D%20%28a**2%20%2B%20b**2%29%20**%200.5%0A%20%20%20%20return%20c%0A%0Aergebnis%20%3D%20pythagoras%283,%204%29&cumulative=false&curInstr=0&heapPrimitives=true&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)
# Webseite.

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
# ## Zurück zur Zaunlänge
#
# - Wir haben bis jetzt die Länge der dritten Seite unseres Grundstücks berechnet.
# - Wir brauchen noch eine Funktion, die die Gesamtlänge ausrechnet:

# %% lang="de" tags=["keep"]
def pythagoras(a, b):
    c = (a**2 + b**2) ** 0.5
    return c

# %% lang="de"


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
# Damit können wir unser Problem vereinfachen:

# %% lang="de"

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Visualisierung auf Python Tutor
#
# Visualisierung auf der
# [Python Tutor](https://pythontutor.com/render.html#code=def%20pythagoras%28a,%20b%29%3A%0A%20%20%20%20c%20%3D%20%28a**2%20%2B%20b**2%29%20**%200.5%0A%20%20%20%20return%20c%0A%0Adef%20gesamtl%C3%A4nge%28x,%20y%29%3A%0A%20%20%20%20z%20%3D%20pythagoras%28x,%20y%29%0A%20%20%20%20l%C3%A4nge%20%3D%20x%20%2B%20y%20%2B%20z%0A%20%20%20%20return%20l%C3%A4nge%0A%20%20%20%20%0Al%C3%A4nge_a%20%3D%2010%0Al%C3%A4nge_b%20%3D%2040%0Aprint%28gesamtl%C3%A4nge%28l%C3%A4nge_a,%20l%C3%A4nge_b%29%29&cumulative=false&curInstr=0&heapPrimitives=true&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)
# Webseite.

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Mini-Workshop: Spenden
#
# Bei einer Spendenaktion hat der Fernsehsender ZRD zugesagt, jede eingehende
# Spende zu verdoppeln. Der Regionalsender YB3 erhöht jede eingehende Spende
# um 10 Euro. (ZRD verdoppelt bevor die 10 Euro von YB3 hinzugefügt werden.)
#
# Schreiben Sie eine Python Funktion `effektive_spende(n)`, die berechnet,
# welcher Betrag effektiv gespendet wird, wenn ein Zuschauer $N$ Euro spendet.

# %% lang="de"

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
# Wie hoch ist die effektive Spende, wenn ein Zuschauer 20 Euro spendet?

# %% lang="de"

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Geben Sie die effektiven Spenden für 10, 25, 50, 100 und 500 Euro auf dem
# Bildschirm aus.
#
# *Hinweis:* Sie können Eingaben mit der `Tab`-Taste vervollständigen. Es genügt
# also, wenn Sie
#
# `pri`-*Tab* `eff`-*Tab*
#
# eingeben bevor Sie die Argumente eintippen.

# %% lang="de"
